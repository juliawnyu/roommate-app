"""
This module encapsulates details about dorms.
"""

TEST_DORM_NAME = 'Test dorm'
NAME = 'name'
LOCATION = 'location'

# Expect database to change frequently:
# For now, consider NAME and LOCATIOn to be
# mandatory fields.
REQUIRED_FLDS = [NAME, LOCATION]
dorms = {
    'handle1': {
        NAME: 'Othmer',
        LOCATION: 'Downtown Brooklyn'
    },
    'handle2': {
        NAME: 'Clark Hall',
        LOCATION: 'Brooklyn Heights'
    },
    'handle3': {
        NAME: 'Carlyle Court',
        LOCATION: 'Union Square West'
    },
    'handle4': {
        NAME: 'Gramercy',
        LOCATION: 'Gramercy Park'
    }
}


def dorm_exists(name):
    """
    Returns whether or not a dorm exists.
    """
    return name in dorms


def get_dorm_dict():
    return dorms


def get_dorms():
    return list(dorms.keys())


def get_dorm_details(dorm):
    return dorms.get(dorm, None)


def add_dorm(name, details):
    if not isinstance(name, str):
        raise TypeError("Wrong type for name, must be a string")
    if not isinstance(details, dict):
        raise TypeError("Wrong type for details, must be a dict")
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError("Required field missing from details: ", field)
    dorms[name] = details


def del_dorm(name):
    del dorms[name]


def main():
    dorms = get_dorms()
    print(dorms)


if __name__ == '__main__':
    main()
