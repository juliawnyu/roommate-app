import pytest

import db.users as usr

import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()
# TEST_DB = ep.db_manager

TITLE = 'Title'
TYPE = 'Type'
DATA = 'Data'


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


SAMPLE_USER_NM = 'SampleUser'
SAMPLE_USER = {
    usr.NAME: SAMPLE_USER_NM,
    usr.EMAIL: 'abc123@nyu.edu'
}


def test_add_user():
    """
    Testing adding a user.
    """
    TEST_CLIENT.post(ep.USER_ADD, json=SAMPLE_USER)
    usr.add_user(SAMPLE_USER_NM, SAMPLE_USER)
    assert usr.user_exists(SAMPLE_USER_NM)
    usr.del_user(SAMPLE_USER_NM)


def test_get_grade():
    """
    See if we can get a user grade type list properly.
    Return should look like:
        {USER_GRADE_NW: [list of user grades...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_GRADES_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_user_grade_list_not_empty():
    """
    See if we can get a user grade type list not empty.
    Return should look like:
        {USER_GRADE_NW: [list of user grades...]}
    """
    resp_json = TEST_CLIENT.get(ep.API_PATH + ep.USER_GRADES_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_get_user_common_bedtimes():
    """
    See if we can get a user grade type list properly.
    Return should look like:
        {USER_COMMON_BEDTIMES_NW: [list of common times...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_COMMON_BEDTIMES_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_cook_preferences():
    """
    See if we can get a cook preferences type list properly.
    Return should look like:
        {COOKING_PREFERENCES_NM: [list of common times...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.COOKING_PREFERENCES_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_user_common_bedtimes_list_not_empty():
    """
    See if we can get common bedtimes list not empty.
    Return should look like:
        {USER_COMMON_BEDTIMES_NM: [list of common times...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_COMMON_BEDTIMES_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_get_user_guest_preferences():
    """
    See if we can get user guest preferences list properly.
    Return should look like:
        {USER_GUEST_PREFERENCES_NW: [list of guest prefs...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_GUEST_PREFERENCES_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_user_guest_preferences_not_emtpy():
    """
    See if we can get user guest preferences list not empty.
    Return should look like:
        {USER_GUEST_PREFERENCES_NW: [list of guest prefs...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_GUEST_PREFERENCES_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_get_user_cleaning_preferences():
    """
    See if we can get user cleaning preferences list properly.
    Return should look like:
        {USER_CLEANING_PREFERENCES_NM: [list of cleaning prefs...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_CLEANING_PREFERENCES_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_user_cleaning_preferences_not_emtpy():
    """
    See if we can get user cleaning preferences list not empty.
    Return should look like:
        {USER_CLEANING_PREFERENCES_NW: [list of cleaning prefs...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_CLEANING_PREFERENCES_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_get_user_sharing_preferences():
    """
    See if we can get user sharing preferences list properly.
    Return should look like:
        {USER_SHARING_PREFERENFES_NM: [list of sharing prefs...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_SHARING_PREFERENCES_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_user_sharing_preferences_not_empty():
    """
    See if we can get user sharing preferenes list not empty.
    Return should look like:
        {USER_SHARING_PREFERENCES_NM: [list of sharing prefs...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_SHARING_PREFERENCES_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_get_user_gender_preference_not_emtpy():
    """
    See if we can get user gender preference list not empty.
    Return should look like:
        {USER_GENDER_PREFERENCE_NW: [list of gender pref...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_GENDER_PREFERENCE_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_get_user_dorm_frequency():
    """
    See if we can get user dorm frequency list properly.
    Return should look like:
        {USER_DORM_FREQUENCY_NM: [list of dorm frequency opts...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_DORM_FREQUENCY_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_user_dorm_frequency_not_empty():
    """
    See if we can get user dorm frequency list not empty.
    Return should look like:
        {USER_DORM_FREQUENCY_NM: [list of dorm frequency opts...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_DORM_FREQUENCY_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_get_user_animal_preference():
    """
    See if we can get user service animal preference list properly.
    Return should look like:
        {USER_ANIMAL_PREFERENCES_NM: [list of service animal prefs...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_ANIMAL_PREFERENCES_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_user_animal_preferences_not_empty():
    """
    See if we can get user animal preferences list not empty.
    Return should look like:
        {USER_ANIMAL_PREFERENCES_NM: [list of service animal prefs opts...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_ANIMAL_PREFERENCES_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_get_user_alcohol_preferences():
    """
    See if we can get user alcohol preference list properly.
    Return should look like:
        {USER_ALCOHOL_PREFERENCES_NM: [list of alcohol prefs...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_ALCOHOL_PREFERENCES_NS).get_json()
    assert isinstance(resp_json[DATA], dict)


def test_get_user_alcohol_preferences_not_empty():
    """
    See if we can get user alcohol preferences list not empty.
    Return should look like:
        {USER_ALCOHOL_PREFERENCES_NM: [list of alcohol prefs opts...]}
    """
    resp_json = TEST_CLIENT.get(
                    ep.API_PATH + ep.USER_ALCOHOL_PREFERENCES_NS).get_json()
    assert len(resp_json[DATA]) > 0


def test_home():
    response = TEST_CLIENT.get("/")
    assert b"Welcome to Roommate Finder!" in response.data
    assert response.status == "200 OK"


def test_login():
    response = TEST_CLIENT.get("/login")
    assert response.status == "200 OK"


def test_logout():
    response = TEST_CLIENT.get("/logout")
    assert response.status == "302 FOUND"


def test_register_get():
    response = TEST_CLIENT.get("/register")
    assert response.status == "200 OK"


@pytest.mark.skip(reason="github actions giving error: Connection Refused")
def test_register_post():
    # TEST_DB.reset_db()
    response = TEST_CLIENT.post("register", data={
        "netID": "abc123",
        "password": "password456",
        "grade": "Sophomore"
    })
    # response code for redirect
    # -> register new user worked successfully and redirecting to home page
    assert response.status_code == 302


def test_user_homepage():
    response = TEST_CLIENT.get("/user_homepage")
    assert response.status == "200 OK"


def test_results():
    response = TEST_CLIENT.get("/results")
    assert response.status == "200 OK"


def test_questionnaire_page():
    response = TEST_CLIENT.get("/questionnaire")
    assert response.status == "200 OK"


def test_clark():
    response = TEST_CLIENT.get("/clark")
    assert response.status == "200 OK"


def test_gramercy():
    response = TEST_CLIENT.get("/gramercy")
    assert response.status == "200 OK"


def test_alumni():
    response = TEST_CLIENT.get("/alumni")
    assert response.status == "200 OK"


def test_othmer():
    response = TEST_CLIENT.get("/othmer")
    assert response.status == "200 OK"


def test_clean_up_json():
    """
    this function makes sure that the clean_up_json() method works
    takes an example json response from an endpoint and parses to list
    """
    json_resp = {
        TITLE: 'UserDormFrequency',
        TYPE: 'Data',
        DATA: {
            1: 'just to sleep',
            2: 'often',
            3: 'always'
        }
    }
    cleaned_up_json_resp = ep.clean_up_json(json_resp)
    assert isinstance(cleaned_up_json_resp, list)
    assert cleaned_up_json_resp is not None
    assert cleaned_up_json_resp[0] == 'just to sleep'
    assert cleaned_up_json_resp[1] == 'often'
    assert cleaned_up_json_resp[2] == 'always'


    def test_get_matched_users():
        """
        this function uses the session netID and matches them with other users in the db.
        returns a list of the matched users and their email 
        for display purposes in frontend.
        takes example json response and matches with another example json response.
        """
        matched_users = {
            'jw1234': ['sleep', 'guests', 'gender'],
            'abc123': ['sleep', 'gender'],
            'omk234': ['gender'],
            'bm2888': ['sleep', 'guests', 'clean', 'gender']
        }
        matched_user_lst = ep.get_matched_user_info('bm2815', matched_users)
        assert len(matched_user_lst) > 0
