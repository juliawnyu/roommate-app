from typing import Type
import pytest

import db.dorms as dm


@pytest.fixture(scope='function')
def new_dorm():
    details = {}
    for field in dm.REQUIRED_FLDS:
        details[field] = 2
    dm.add_dorm(dm.TEST_DORM_NAME, details)
    yield
    dm.del_dorm(dm.TEST_DORM_NAME)


def test_get_dorms():
    drms = dm.get_dorms()
    assert isinstance(drms, list)
    assert len(drms) > 1


def test_get_dorm_details(new_dorm):
    drm_dts = dm.get_dorm_details(dm.TEST_DORM_NAME)
    assert isinstance(drm_dts, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        dm.add_dorm(0, {})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        dm.add_dorm('a new dorm', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        dm.add_dorm('a new dorm', {'foo': 'bar'})


def test_add_dorm(new_dorm):
    assert dm.dorm_exists(dm.TEST_DORM_NAME)


@pytest.mark.skip(reason="method not implemented yet")
def test_edit_dorm(dorm):
    return
