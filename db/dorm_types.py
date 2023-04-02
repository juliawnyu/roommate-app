

OTHMER = 'Othmer'
CLARK = 'Clark'

dorm_types = {
    OTHMER: {
        'location': 'Brooklyn',
        'type': 'freshmen'
    },
    CLARK: {
        'location': 'Brooklyn',
        'type': 'freshmen'
    }
 }


def add_dorm_type(type_name, traits):
    if dorm_type_exists(type_name):
        raise ValueError(f'Dorm type exists: {type_name=}')
    dorm_types[type_name] = traits


def del_dorm_type(type_name):
    if dorm_type_exists(type_name):
        del dorm_types[type_name]


def dorm_type_exists(type_name):
    return type_name in dorm_types
