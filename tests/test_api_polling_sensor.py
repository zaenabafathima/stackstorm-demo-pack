import unittest
# from stackstorm_demo_pack.sensors.base_sensors import ApiPollingSensor
from integration_properties_sensor import IntegrationPropertiesSensor
from base_api import ApiPollingSensorBase
from st2tests.base import BaseSensorTestCase
from st2tests.mocks.sensor import MockSensorService


class MySensorSensorTestCase(BaseSensorTestCase):
    sensor_cls = IntegrationPropertiesSensor

    def test_method(self):
        print("TEsting!!!!")
        sensor = self.get_sensor_instance(config={'foo': 'bar'})
        sensor.poll()
        # ...
