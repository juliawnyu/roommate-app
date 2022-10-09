
import pytest

import server.app as ep

TEST_CLIENT = ep.app.test_client()


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


def test_get_grade():
    """
    See if we can get a user grade type list properly.
    Return should look like:
        {USER_GRADE_NW: [list of user grades...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_GRADES).get_json()
    assert isinstance(resp_json[ep.USER_GRADES_NM], list)


def test_get_user_grade_list_not_empty():
    """
    See if we can get a user grade type list not empty.
    Return should look like:
        {USER_GRADE_NW: [list of user grades...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_GRADES).get_json()
    assert len(resp_json[ep.USER_GRADES_NM]) > 0

def test_home():
    response = TEST_CLIENT.get("/")
    assert b"Welcome to Roommate Finder!" in response.data