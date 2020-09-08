import requests

from st2reactor.sensor.base import PollingSensor


class WorkingSensor(PollingSensor):
    def __init__(self, sensor_service, config, poll_interval=60):
        super(WorkingSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False
        # self._endpoint = 'https://zeroday-onboard.default.abattery.appbattery.nss1.tn.akamai.com/zeroday/v1/integration'

    def setup(self):
        pass

    def poll(self):
        self._logger.debug('WorkingSensor dispatching trigger...')
        api_response = requests.get('http://www.google.com')
        payload = {
            'greeting': 'API Polling Working!',
            'response': api_response.text
        }
        self.sensor_service.dispatch(trigger='hello_st2.eventX', payload=payload)

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
