import pytest

import db.dorms as dm


def test_get_dorms():
    drms = dm.get_dorms()
    assert isinstance(drms, list)
    assert len(drms) > 1


def test_get_dorm_details():
    drm_dts = dm.get_dorm_details(dm.TEST_DORM_NAME)
    assert isinstance(drm_dts, dict)


# def test_dorm_exists():
#     return None


# def test_dorm_not_exists():
#     return None


# def test_add_wrong_name_type():
#     return None


# def test_add_wrong_details_type():
#     return None


# def test_add_missing_field():
#     return None


# def test_add_dorm():
#     return None