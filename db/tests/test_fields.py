import pytest

import db.fields as flds

TEST_FIELD_NAME = 'UserGrades'
DATA = 'Data'
TITLE = 'Title'


@pytest.fixture(scope='function')
def test_get_fields():
    field = flds.get_field(TEST_FIELD_NAME)
    assert field is not None
    assert field[TITLE] is TEST_FIELD_NAME
    assert field[DATA] is not None
