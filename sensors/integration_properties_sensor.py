import json
import requests
import io
import logging
import time
from typing import Union
from urllib import parse


LOGGER = logging.getLogger(__name__)

from sample_polling_sensor import ApiPollingSensor


class IntegrationPropertiesSensor(ApiPollingSensor):
    def __init__(self, sensor_service, config, poll_interval=60, endpoint=''):
        super(IntegrationPropertiesSensor, self).__init__(
            sensor_service=sensor_service,
            config=config,
            poll_interval=poll_interval,
            endpoint='http://www.google.com',
            trigger='hello_st2.integration_property_fetch',
            greeting='Integration Property Sensor works!'
        )

    def poll(self):
        self.sensor_service.dispatch(trigger=self._trigger, payload={'greeting': 'Polling from integration properties'})