import unittest
import requests
# from stackstorm_demo_pack.sensors.base_sensors import ApiPollingSensor
from integration_properties_sensor import IntegrationPropertiesSensor
from base_api import ApiPollingSensorBase
from st2tests.base import BaseSensorTestCase
from st2tests.mocks.sensor import MockSensorService


class MySensorSensorTestCase(BaseSensorTestCase):
    sensor_cls = ApiPollingSensorBase

    def test_method(self):
        print("Testing!!!!")
        sensor = self.get_sensor_instance(
            config={
                'foo': 'bar',
                'poll_interval': 28
            })
        sensor.poll()
        self.assertEqual(len(self.get_dispatched_triggers()), 1)
        print("Make request method:", sensor.make_request_with_retry)
        print("Sensor poll time:", sensor._poll_interval)
        # ...

    def test_make_request_with_retry(self):
        sensor = self.get_sensor_instance(
            config={
                'foo': 'bar',
                'poll_interval': 28
            })
        print("Testing make request with retry")
        try:
            response = sensor.make_request_with_retry(url='localhost:8000/alias/', method='GET', headers={})
        except Exception as e:
            print("Error while hitting localhost:", str(e))

