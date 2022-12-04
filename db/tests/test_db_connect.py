import os

import pymongo as pm

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