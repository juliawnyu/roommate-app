import db.db as dbc

import pytest

dbc.MONGO_ENV = 'LOCAL'

TEST_DB = dbc.USERS
TEST_NETID = 'bm2815'
TEST_PASSWORD = 'password'
TEST_GRADE = 'senior'


@pytest.fixture(scope='function')
def temp_rec():
    if dbc.MONGO_ENV == 'LOCAL':
        db = dbc.DB_Manager()
        db.add_user(TEST_NETID, TEST_PASSWORD, TEST_GRADE)
        yield
        db.remove_user(TEST_NETID)


@pytest.mark.skip(reason="pymongo error in github actions")
def test_reset_db(temp_rec):
    db = dbc.DB_Manager()
    db.reset_db()
    assert not db.get_all()


@pytest.mark.skip(reason="pymongo error in github actions")
def test_get_user(temp_rec):
    db = dbc.DB_Manager()
    assert db.get_user(TEST_NETID)


@pytest.mark.skip(reason="pymongo error in github actions")
def test_get_all(temp_rec):
    db = dbc.DB_Manager()
    assert db.get_all()


@pytest.mark.skip(reason="pymongo error in github actions")
def test_login_correct(temp_rec):
    db = dbc.DB_Manager()
    assert db.login_correct(TEST_NETID, TEST_PASSWORD)


@pytest.mark.skip(reason="pymongo error in github actions")
def test_login_incorrect(temp_rec):
    db = dbc.DB_Manager()
    assert not db.login_correct(TEST_NETID, "WRONG PASSWORD")
