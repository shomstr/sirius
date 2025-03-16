from api.database import Repositories
from api.database.models import User
from tests.integration.db.data import LIST_TEST_USERS, TEST_USER


async def test_create(db: AsyncSession):
    us = await repo.users.create_from_model(TEST_USER)

    assert us.id == TEST_USER.id
    assert us.username == TEST_USER.username
    assert us.id == TEST_USER.id


async def test_get(db: AsyncSession):
    us = await repo.users.create_from_model(TEST_USER)
    user = await repo.users.get(TEST_USER.id)

    assert user is not None

    assert us.id == user.id
    assert us.username == user.username
    assert us.id == user.id


async def test_update(db: AsyncSession):
    await repo.users.create_from_model(TEST_USER)
    us: User = await repo.users.get(TEST_USER.id)

    assert us is not None

    us.username = None
    await repo.users.update(us)

    us: User = await repo.users.get(TEST_USER.id)

    assert us.username is None


async def test_delete(db: AsyncSession):
    us = await repo.users.create_from_model(TEST_USER)
    await repo.users.delete(us)

    us = await repo.users.get(TEST_USER.id)
    assert us is None


async def test_get_all(db: AsyncSession):
    await repo.users.create_from_model(*LIST_TEST_USERS)

    all_users = await repo.users.get_all()

    assert len(LIST_TEST_USERS) == len(all_users)

    await repo.users.delete(*all_users)
