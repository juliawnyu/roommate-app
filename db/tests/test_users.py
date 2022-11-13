import pytest

import db.users as user


def test_get_users():
    users = user.get_users()
    assert isinstance(users, list)
    assert len(users) > 1


def test_get_users_dict():
    user_details = user.get_user_details(user.TEST_USERNAME)
    assert isinstance(user_details, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        user.add_user('new user', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        user.add_user('new user', {'foo': 'bar'})


def test_add_user():
    details = {}
    for field in user.REQUIRED_FIELDS:
        details[field] = 2
    user.add_user(user.TEST_USERNAME, details)
    assert user.user_exists(user.TEST_USERNAME)
    user.del_user(user.TEST_USERNAME)
