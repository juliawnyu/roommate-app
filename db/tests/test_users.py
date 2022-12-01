import pytest

import db.users as user


@pytest.fixture(scope='function')
def new_user():
    details = {}
    for field in user.REQUIRED_FIELDS:
        details[field] = 2
    user.add_user(user.TEST_USERNAME, details)
    yield
    user.del_user(user.TEST_USERNAME)


def test_get_users():
    users = user.get_users()
    assert isinstance(users, list)
    assert len(users) > 1


def test_get_users_dict(new_user):
    user_details = user.get_user_details(user.TEST_USERNAME)
    assert isinstance(user_details, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        user.add_user('new user', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        user.add_user('new user', {'foo': 'bar'})


def test_add_user(new_user):
    assert user.user_exists(user.TEST_USERNAME)


@pytest.mark.skip(reason="method not implemented yet")
def test_edit_user(dorm):
    return
