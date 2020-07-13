import eventlet

from st2reactor.sensor.base import Sensor


class ChatopsSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(ChatopsSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        pass

    def run(self):
        while not self._stop:
            self._logger.debug('HelloSensor dispatching trigger...')
            # payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vODhiZjMyMjAtYzAzNi0xMWVhLTk0ZmEtMDFhYjAzYjFlNzc2'}
            # self.sensor_service.dispatch(trigger='cisco_spark.get_room', payload=payload)
            self.sensor_service.dispatch(trigger='hello_st2.event2')
            eventlet.sleep(60)

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
