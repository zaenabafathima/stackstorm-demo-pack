import eventlet

from st2reactor.sensor.base import Sensor, PollingSensor


class WorkingSensor(PollingSensor):
    def __init__(self, sensor_service, config, poll_interval=5):
        super(WorkingSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        pass

    def poll(self):
        self._logger.debug('WorkingSensor dispatching trigger...')
        count = self.sensor_service.get_value('hello_st2.count') or 0
        payload = {'greeting': 'Polling Working, StackStorm!', 'count': int(count) + 1}
        self.sensor_service.dispatch(trigger='hello_st2.eventX', payload=payload)
        self.sensor_service.set_value('hello_st2.count', payload['count'])

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
