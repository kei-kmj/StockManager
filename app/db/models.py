from datetime import date, datetime, timezone
from typing import List, Optional

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint, func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# モデルのベースクラス
class Base(DeclarativeBase):
    pass


# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-mapped-column-nullability
# 型アノテーション (Mapped[T])でデータ型とnullabilityを自動推論する


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    nickname: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )

    # https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many
    # relationship() は Mapped アノテーションから対象クラス（関連先）とコレクションの型を推論する
    # mapped_column() でカラムを定義するのと、relationship() でリレーションを定義するのは、
    # 同じ「型アノテーションから情報を推論する」仕組み

    # https://docs.sqlalchemy.org/en/20/orm/relationship_api.html#sqlalchemy.orm.relationship.params.back_populates
    # back_populates="user"を設定すると、このリレーションがUserクラスのstock_eventsに対応していることをSQLAlchemyに伝える
    # もう一方のrelationshipと同期される
    # 両方 に back_populates を書くことで、双方向の関連を明示的に定義する
    # また、このリレーションの変更が flush（データベースの書き込み）時にどのように永続化されるかを指示する

    # Unit of Work
    # 一連のオブジェクトに対して行われた変更のリストを維持し、保留中のすべての変更を定期的にデータベースに書き出す
    # https://martinfowler.com/eaaCatalog/unitOfWork.html
    # TODO:unit of workを理解する

    stock_events: Mapped[List["StockEvent"]] = relationship(back_populates="user")


class Maker(Base):
    __tablename__ = "makers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )

    items: Mapped[List["Item"]] = relationship(back_populates="maker")


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    maker_id: Mapped[int] = mapped_column(ForeignKey("makers.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )

    maker: Mapped["Maker"] = relationship(back_populates="items")
    stock_events: Mapped[List["StockEvent"]] = relationship(back_populates="item")

    __table_args__ = (
        UniqueConstraint("name", "maker_id", name="uq_items_name_maker_id"),
    )


class StockEvent(Base):
    __tablename__ = "stock_events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    actor_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    event_type: Mapped[int] = mapped_column(Integer)
    quantity: Mapped[int] = mapped_column(Integer)
    event_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    note: Mapped[Optional[str]] = mapped_column(String)

    user: Mapped["User"] = relationship(back_populates="stock_events")
    item: Mapped["Item"] = relationship(back_populates="stock_events")



class InventorySnapshot(Base):
    __tablename__ = "inventory_snapshots"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    snapshot_date: Mapped[date] = mapped_column(Date, index=True)
    stock_quantity: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        UniqueConstraint("item_id", "snapshot_date", name="uq_inventory_snapshot"),
    )


class Closing(Base):
    __tablename__ = "closings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    closing_date: Mapped[date] = mapped_column(Date, unique=True)
    is_closed: Mapped[bool] = mapped_column(Boolean, default=False)

    __table_args__ = (UniqueConstraint("closing_date", name="uq_inventory_closing"),)
