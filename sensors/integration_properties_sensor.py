import logging


LOGGER = logging.getLogger(__name__)

from st2reactor.sensor.base import PollingSensor
from base_sensors.base_poll_sensor import ApiPollingSensorBase


class ApiPollingSensor2(ApiPollingSensorBase):
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
        super().__init__(sensor_service=sensor_service, config=config,
                         endpoint='http://www.google.com',
                         trigger='hello_st2.event1',
                         greeting='2 - STILL WORKING, YAY!!')
        self._poll_interval = poll_interval