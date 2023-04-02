import pytest

import db.dorm_types as dtyp

NEW_DORM_TYPE = 'Carlyle'
DORM_TRAITS = {'location': 'Manhattan', 'type': 'upperclassmen'}


@pytest.fixture(scope='function')
def new_dorm_type():
    dtyp.add_dorm_type(NEW_DORM_TYPE, DORM_TRAITS)
    yield
    dtyp.del_dorm_type(NEW_DORM_TYPE)


@pytest.fixture(scope='function')
def test_del_dorm_type():
    dtyp.add_dorm_type(NEW_DORM_TYPE, DORM_TRAITS)
    assert dtyp.dorm_type_exists(NEW_DORM_TYPE) is not False
    dtyp.del_dorm_type(NEW_DORM_TYPE)
    assert dtyp.dorm_type_exists(NEW_DORM_TYPE) is False
