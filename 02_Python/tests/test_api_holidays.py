import pytest
import requests
from unittest import mock
from api_holidays.api_holidays import HolidaysAPI  # Adjust import path as per your project structure

def test_pass():
  assert 1 == 1

# tests/test_api_holidays.py



@mock.patch('requests.get')
def test_api_holidays_success(mock_requests_get):
    # Mocking requests.get to simulate a successful response
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = [{'name': 'Holiday 1'}, {'name': 'Holiday 2'}]

    # Call the function under test
    api_instance = HolidaysAPI('2020')
    result = api_instance.process()

    # Assertions
    assert result == [{'name': 'Holiday 1'}, {'name': 'Holiday 2'}]

@mock.patch('requests.get')
def test_api_holidays_failure(mock_requests_get):
    # Mocking requests.get to simulate a failed response
    mock_requests_get.return_value.status_code = 404

    # Call the function under test
    api_instance = HolidaysAPI('2020')
    result = api_instance.process()

    # Assertions
    assert result is None