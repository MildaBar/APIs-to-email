import sys
import pytest
from file import check_input


def test_check_input_valid_email():
    sys.argv = ["file_name.py", "test@example.com", "quotes_api"]
    assert check_input() == ("test@example.com", "quotes_api")


def test_check_input_invalid_email():
    sys.argv = ["file_name.py", "testexample.com", "quotes_api"]
    # raise a SystemExit exception because the email address is invalid
    with pytest.raises(SystemExit):
        check_input()


def test_check_input_invalid_api():
    sys.argv = ["file_name.py", "test@example.com", "invalid_api"]
    # raise a SystemExit exception because the api is invalid
    with pytest.raises(SystemExit):
        check_input()


def test_check_input_valid_api():
    sys.argv = ["file_name.py", "test@example.com", "weather_api"]
    assert check_input() == ("test@example.com", "weather_api")
    sys.argv = ["file_name.py", "test@example.com", "quotes_api"]
    assert check_input() == ("test@example.com", "quotes_api")
