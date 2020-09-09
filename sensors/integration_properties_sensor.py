import json
import requests
import io
import logging
import time
from typing import Union
from urllib import parse


LOGGER = logging.getLogger(__name__)

from sensors.sample_polling_sensor import ApiPollingSensor
from st2reactor.sensor.base import PollingSensor


class IntegrationPropertiesSensor(PollingSensor):
    def __init__(self, sensor_service, config=None, poll_interval=10):
        super(IntegrationPropertiesSensor, self).__init__(
            sensor_service=sensor_service,
            config=config
            # poll_interval=poll_interval,
            # endpoint='http://www.google.com',
            # trigger='hello_st2.integration_property_fetch',
            # greeting='Integration Property Sensor works!'
        )
        self._poll_interval = poll_interval

    def poll(self):
        print('In here')
        self.sensor_service.dispatch(trigger='hello_st2.integration_property_fetch_2', payload={'greeting': 'Integration greeting'})

    def setup(self):
        """
        Run the sensor initialization / setup code (if any).
        """
        pass

    def cleanup(self):
        """
        Run the sensor cleanup code (if any).
        """
        pass

    def add_trigger(self, trigger):
        """
        Runs when trigger is created
        """
        pass

    def update_trigger(self, trigger):
        """
        Runs when trigger is updated
        """
        pass

    def remove_trigger(self, trigger):
        """
        Runs when trigger is deleted
        """
        pass