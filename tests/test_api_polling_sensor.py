import unittest
# from stackstorm_demo_pack.sensors.base_sensors import ApiPollingSensor
from base_poll_sensor import ApiPollingSensor
from st2tests.base import BaseSensorTestCase
from st2tests.mocks.sensor import MockSensorService


class MySensorSensorTestCase(BaseSensorTestCase):
    sensor_cls = ApiPollingSensor

    def test_method(self):
        print("TEsting!!!!")
        sensor = self.get_sensor_instance(config={'foo': 'bar'})
        sensor.poll()
        # ...
