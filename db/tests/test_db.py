import db.db as dbc
import pymongo as pym

import pytest
import os

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