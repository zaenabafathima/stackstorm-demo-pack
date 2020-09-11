import unittest
import requests

from unittest import mock

from base_api_polling_sensor import ApiPollingSensorBase
from st2tests.base import BaseSensorTestCase
from st2tests.mocks.sensor import MockSensorService


class MockResponse:
    def __init__(self, json_data, status_code):
        self.content = json_data
        self.status_code = status_code


class MySensorSensorTestCase(BaseSensorTestCase):
    sensor_cls = ApiPollingSensorBase

    def test_method(self):
        print("Testing!!!!")
        sensor = self.get_sensor_instance(config={'foo': 'bar'})
        sensor.poll()
        self.assertEqual(len(self.get_dispatched_triggers()), 1)
        print("Make request method:", sensor.make_request_with_retry)
        print("Sensor poll time:", sensor._poll_interval)
        # ...

    def test_get_request_with_retry(self):
        """Something."""
        sensor = self.get_sensor_instance(config={'foo': 'bar'})
        retry_count = 3
        requests.request = mock.Mock()
        requests.request.return_value = MockResponse({}, 500)
        sensor.make_request_with_retry(
            url='http://someurl.com/test.json',
            method='GET',
            retry_wait_time=5,
            retry_count=retry_count,
            headers={},
        )
        print("Mocked request call count:", requests.request.call_count)
        self.assertEqual(requests.request.call_count, retry_count)
        requests.request.return_value = MockResponse({}, 400)
        sensor.make_request_with_retry(
            url='http://someurl.com/test.json',
            method='GET',
            retry_wait_time=5,
            retry_count=retry_count,
            headers={},
        )
        print("Mocked request call count:", requests.request.call_count)
        self.assertEqual(requests.request.call_count, 1)
        requests.request.return_value = MockResponse({}, 200)
        sensor.make_request_with_retry(
            url='http://someurl.com/test.json',
            method='GET',
            retry_wait_time=5,
            retry_count=retry_count,
            headers={},
        )
        print("Mocked request call count:", requests.request.call_count)
        self.assertEqual(requests.request.call_count, 1)
