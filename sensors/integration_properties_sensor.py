import logging

from base_api import ApiPollingSensorBase


LOGGER = logging.getLogger(__name__)


class IntegrationPropertiesSensor(ApiPollingSensorBase):
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
                         endpoint='https://zeroday-onboard.default.abattery.appbattery.nss1.tn.akamai.com/zeroday/v1/integration',
                         trigger='hello_st2.integration_property_fetch',
                         greeting='11 - STILL WORKING, YAY!!')
        self._poll_interval = poll_interval
