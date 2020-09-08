import requests

from st2reactor.sensor.base import PollingSensor


class ApiPollingSensor(PollingSensor):
    def __init__(self, sensor_service, config, poll_interval=60, endpoint=''):
        super(ApiPollingSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._poll_interval = poll_interval
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False
        self._endpoint = endpoint or 'https://zeroday-onboard.default.abattery.appbattery.nss1.tn.akamai.com/zeroday/v1/integration'

    def setup(self):
        pass

    def poll(self):
        self._logger.debug('WorkingSensor dispatching trigger...')
        payload = {
            'greeting': 'API Polling Working!',
        }
        self._endpoint = 'http://www.google.com'
        try:
            api_response = requests.get(self._endpoint, verify=False)
            payload['response'] = api_response.json()
        except Exception as e:
            payload['response'] = 'An error occured!' + str(e)

        self.sensor_service.dispatch(trigger='hello_st2.integration_property_fetch', payload=payload)

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
