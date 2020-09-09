import json
import requests
import io
import logging
import time
from typing import Union
from urllib import parse


LOGGER = logging.getLogger(__name__)

from st2reactor.sensor.base import PollingSensor
# from sensors.sample_polling_sensor import ApiPollingSensor


class ApiPollingSensor2(PollingSensor):
    """Poll an API and return its response with status code."""

    def __init__(self,
                 sensor_service,
                 config=None,
                 poll_interval=10,
                 endpoint='',
                 trigger='',
                 greeting=''
                 ):
        """Initialize API Polling Sensor."""
        super().__init__(sensor_service=sensor_service, config=config)
        self._poll_interval = poll_interval
        # self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._endpoint = 'https://zeroday-onboard.default.abattery.appbattery.nss1.tn.akamai.com/zeroday/v1/integration'
        self._trigger = trigger or 'hello_st2.integration_property_fetch'
        self._greeting = greeting

    def poll(self):
        # self._logger.debug('WorkingSensor dispatching trigger...')
        payload = {
            'greeting': self._greeting or 'DUPLICATE API Polling Sensor',
            'status': None,
            'response': None
        }
        self.sensor_service.dispatch(trigger='hello_st2.integration_property_fetch', payload=payload)
        # try:
        #     api_response = requests.get(self._endpoint, verify=False)
        #     payload['status'] = api_response.status_code
        #     api_response.raise_for_status()
        #     payload['response'] = api_response.json()
        # except requests.exceptions.RequestException as err:
        #     payload['response'] = str(err)
        # except json.decoder.JSONDecodeError as json_err:
        #     payload['response'] = 'JSON Decode Error! ' + str(json_err)

        # self.sensor_service.dispatch(trigger='hello_st2.integration_property_fetch', payload=payload)

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

    