import os

import pytest

import db.db_connect as dbc

RUNNING_ON_CICD_SERVER = os.environ.get("CI", False)

TEST_DB = dbc.DORM_DB
TEST_COLLECT = "test_collect"
TEST_NAME = "test"


@pytest.fixture(scope='function')
def temp_rec():
    dbc.connect_db()
    dbc.client[TEST_DB][TEST_COLLECT].insert_one({TEST_NAME: TEST_NAME})
    yield
    dbc.client[TEST_DB][TEST_COLLECT].delete_one({TEST_NAME: TEST_NAME})


@pytest.mark.skip(reason="pymongo error in github actions")
def test_fetch_one(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: TEST_NAME})
    assert ret is not None


@pytest.mark.skip(reason="pymongo error in github actions")
def test_fetch_one_not_there(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: 'not a field'})
    assert ret is None


@pytest.mark.skip(reason="pymongo error in github actions")
def test_fetch_all(temp_rec):
    ret = dbc.fetch_all(TEST_COLLECT, {TEST_NAME: TEST_NAME})
    assert ret is not None


@pytest.mark.skip(reason="pymongo error in github actions")
def test_fetch_all_not_there(temp_rec):
    ret = dbc.fetch_all(TEST_COLLECT, {TEST_NAME: 'not a field'})
    assert ret is None
