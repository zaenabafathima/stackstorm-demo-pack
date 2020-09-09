import logging

from base_sensors.base_poll_sensor import ApiPollingSensor


LOGGER = logging.getLogger(__name__)


class IntegrationPropertiesSensor(ApiPollingSensor):
    """Poll integration_properties and return its response with status code."""

    def __init__(self,
                 sensor_service,
                 config=None,
                 poll_interval=10,
                 endpoint='',
                 params={},
                 headers={},
                 trigger='',
                 greeting=''
                 ):
        """Initialize API Polling Sensor."""
        super().__init__(sensor_service=sensor_service, config=config,
                         endpoint='http://www.google.com',
                         trigger='hello_st2.integration_property_fetch',
                         greeting='8 - STILL WORKING, YAY!!')
        self._poll_interval = poll_interval
