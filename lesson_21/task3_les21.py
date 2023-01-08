import pytest
from task1_les21 import MyOpen


# I'll use "fixtures can request other fixtures"
# Some nice theory: in this code, test_data “requests” check and when pytest sees this, it will execute
# the check fixture function and pass the object it returns into test_data as the check argument.
@pytest.fixture
def replace_file_obj():
    return "new_test.txt"


@pytest.fixture
def data_to_check(replace_file_obj):
    with MyOpen(replace_file_obj, 'r') as opened_file:
        data = opened_file.read()
        return data[:11]


def test_data(data_to_check):
    assert data_to_check == "This is all"
