"""
This module encapsulates information about users.
"""

TEST_USERNAME = 'username'
NAME = 'name'
EMAIL = 'email'

REQUIRED_FIELDS = [EMAIL]
users = {
    TEST_USERNAME: {EMAIL: 'bmac@biancamacias.com', NAME: 'Bianca'},
    'handle': {EMAIL: 'julia@juliawestphal.com', NAME: 'Julia'}
}


def user_exists(name):
    """
    Returns boolean, true if name in users dict, false otherwise.
    """
    return name in users


def get_users():
    return list(users.keys())


def get_user_details(user):
    return users.get(user, None)


def del_user(name):
    del users[name]


def add_user(name, details):
    if not isinstance(name, str):
        raise TypeError('Name needs to be a string.')
    if not isinstance(details, dict):
        raise TypeError('Details need to be a dictionary.')
    for field in REQUIRED_FIELDS:
        if field not in details:
            raise ValueError('Missing required field: ', field)
    users[name] = details


def main():
    users = get_users()
    for user in users.keys():
        print(user)


if __name__ == '__main__':
    main()
    