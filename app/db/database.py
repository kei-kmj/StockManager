from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "sqlite+aiosqlite:///./app/db/stockmanager.db"

# SQLite用エンジン
# https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine
# create_engine() はデータベースとの 接続を管理するオブジェクト (Engine) を生成。
# この Engine を通じて、SQLAlchemy はデータベースとの通信を行う。
# create_engine() は 遅延接続 (lazy initialization) を採用し、
# create_engine() を実行した時点では、実際にはデータベースに接続せず、最初の DB アクセス時に接続を確立する
engine = create_async_engine(DATABASE_URL, echo=True)

# セッションの作成
# 同期・非同期を混在させる場合はsessionmaker(engine, class_=AsyncSession)にすると汎用的
async_session = async_sessionmaker(engine)

# モデルのベースクラス
class Base(DeclarativeBase):
    pass

