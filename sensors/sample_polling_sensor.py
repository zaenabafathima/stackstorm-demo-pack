import json
import requests

from st2reactor.sensor.base import PollingSensor


class ApiPollingSensor(PollingSensor):
    def __init__(self, sensor_service, config, poll_interval=60, endpoint=''):
        super(ApiPollingSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._poll_interval = poll_interval
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False
        # self._endpoint = endpoint or 'https://zeroday-onboard.default.abattery.appbattery.nss1.tn.akamai.com/zeroday/v1/integration'
        self._endpoint = 'http://localhost:8000/alias/aliases'

    def setup(self):
        pass

    def poll(self):
        self._logger.debug('WorkingSensor dispatching trigger...')
        payload = {
            'greeting': 'Local API Polling Working!',
            'status': None,
            'response': None
        }
        self._endpoint = 'http://www.google.com'
        try:
            api_response = requests.get(self._endpoint, verify=False)
            payload['status'] = api_response.status_code
            api_response.raise_for_status()
            payload['response'] = api_response.json()
        except requests.exceptions.RequestException as err:
            payload['response'] = str(err)
        except json.decoder.JSONDecodeError as json_err:
            payload['response'] = 'JSON Decode Error! ' + str(json_err)

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
