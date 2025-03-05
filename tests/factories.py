import factory
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User


class AsyncUserFactory(factory.alchemy.SQLAlchemyModelFactory):
    """ 非同期セッションを使用するFactory """

    class Meta:
        model = User
        sqlalchemy_session_persistence = "flush"

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("name")
    nickname = factory.Faker("user_name")
    email = factory.Faker("email")

    @classmethod
    async def create_async(cls, session: AsyncSession, **kwargs):
        """ 非同期の `create` メソッド """
        instance = cls(**kwargs)
        session.add(instance)
        await session.commit()  # ✅ 非同期でコミット
        await session.refresh(instance)
        return instance
