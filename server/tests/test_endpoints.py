
import pytest

import server.endpoints as ep

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


def test_get_user_common_bedtimes():
    """
    See if we can get a user grade type list properly.
    Return should look like:
        {USER_COMMON_BEDTIMES_NW: [list of common times...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_COMMON_BEDTIMES).get_json()
    assert isinstance(resp_json[ep.USER_COMMON_BEDTIMES_NM], list)


def test_get_user_common_bedtimes_list_not_empty():
    """
    See if we can get common bedtimes list not empty.
    Return should look like:
        {USER_COMMON_BEDTIMES_NM: [list of common times...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_COMMON_BEDTIMES).get_json()
    assert len(resp_json[ep.USER_COMMON_BEDTIMES_NM]) > 0


def test_get_user_guest_preferences():
    """
    See if we can get user guest preferences list properly.
    Return should look like:
        {USER_GUEST_PREFERENCES_NW: [list of guest prefs...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_GUEST_PREFERENCES).get_json()
    assert isinstance(resp_json[ep.USER_GUEST_PREFERENCES_NM], list)


def test_get_user_guest_preferences_not_emtpy():
    """
    See if we can get user guest preferences list not empty.
    Return should look like:
        {USER_GUEST_PREFERENCES_NW: [list of guest prefs...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_GUEST_PREFERENCES).get_json()
    assert len(resp_json[ep.USER_GUEST_PREFERENCES_NM]) > 0


def test_get_user_cleaning_preferences():
    """
    See if we can get user cleaning preferences list properly.
    Return should look like:
        {USER_CLEANING_PREFERENCES_NM: [list of cleaning prefs...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_CLEANING_PREFERENCES).get_json()
    assert isinstance(resp_json[ep.USER_CLEANING_PREFERENCES_NM], list)


def test_get_user_cleaning_preferences_not_emtpy():
    """
    See if we can get user cleaning preferences list not empty.
    Return should look like:
        {USER_CLEANING_PREFERENCES_NW: [list of cleaning prefs...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_CLEANING_PREFERENCES).get_json()
    assert len(resp_json[ep.USER_CLEANING_PREFERENCES_NM]) > 0


def test_get_user_sharing_preferences():
    """
    See if we can get user sharing preferences list properly.
    Return should look like:
        {USER_SHARING_PREFERENFES_NM: [list of sharing prefs...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_SHARING_PREFERENCES).get_json()
    assert isinstance(resp_json[ep.USER_SHARING_PREFERENCES_NM], list)


def test_get_user_sharing_preferenes_not_empty():
    """
    See if we can get user sharing preferenes list not empty.
    Return should look like:
        {USER_SHARING_PREFERENCES_NM: [list of sharing prefs...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_SHARING_PREFERENCES).get_json()
    assert len(resp_json[ep.USER_SHARING_PREFERENCES_NM]) > 0


def test_home():
    response = TEST_CLIENT.get("/")
    assert b"Welcome to Roommate Finder!" in response.data
    assert response.status == "200 OK"


def test_login():
    response = TEST_CLIENT.get("/login")
    assert response.status == "200 OK"


def test_register():
    response = TEST_CLIENT.get("/register")
    assert response.status == "200 OK"

def test_quiz_page():
    response = TEST_CLIENT.get("/quiz")
    assert response.status == "200 OK"

def test_user_homepage():
    response = TEST_CLIENT.get("/user_homepage")
    assert response.status == "200 OK"