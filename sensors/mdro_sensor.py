
import os
import requests
import json
import copy
from st2reactor.sensor.base import PollingSensor


# class SamplePollingSensor(PollingSensor):
#     """
#     * self.sensor_service
#         - provides utilities like
#             get_logger() for writing to logs.
#             dispatch() for dispatching triggers into the system.
#     * self._config
#         - contains configuration that was specified as
#           config.yaml in the pack.
#     * self._poll_interval
#         - indicates the interval between two successive poll() calls.
#     """
#     def __init__(self, sensor_service, config=None, poll_interval=60):
#         super(SamplePollingSensor, self).__init__(
#             sensor_service=sensor_service, config=config, poll_interval=poll_interval
#         )

#         self._logger = self.sensor_service.get_logger(
#             name=self.__class__.__name__)
#         self._wpt_url = "https://webpagetest.org"
#         self._key = None
#         self._trigger_name = "status_checker"
#         self._trigger_pack = "st2_poc"
#         self._trigger_ref = ".".join([self._trigger_pack, self._trigger_name])

#     def setup(self):
#         # Setup stuff goes here. For example, you might establish connections
#         # to external system once and reuse it. This is called only once by the system.
#         pass

#     def poll(self):
#         # This is where the crux of the sensor work goes.
#         # This is called every self._poll_interval.
#         # For example, let's assume you want to query ec2 and get
#         # health information about your instances:
#         #   some_data = aws_client.get('')
#         #   payload = self._to_payload(some_data)
#         #   # _to_triggers is something you'd write to convert the data format you have
#         #   # into a standard python dictionary. This should follow the payload schema
#         #   # registered for the trigger.
#         #   self.sensor_service.dispatch(trigger, payload)
#         #   # You can refer to the trigger as dict
#         #   # { "name": ${trigger_name}, "pack": ${trigger_pack} }
#         #   # or just simply by reference as string.
#         #   # i.e. dispatch(${trigger_pack}.${trigger_name}, payload)
#         #   # E.g.: dispatch('examples.foo_sensor', {'k1': 'stuff', 'k2': 'foo'})
#         #   # trace_tag is a tag you would like to associate with the dispatched TriggerInstance
#         #   # Typically the trace_tag is unique and a reference to an external event.
#         pass

#     def cleanup(self):
#         # This is called when the st2 system goes down. You can perform cleanup operations like
#         # closing the connections to external system here.
#         pass

#     def add_trigger(self, trigger):
#         # This method is called when trigger is created
#         pass

#     def update_trigger(self, trigger):
#         # This method is called when trigger is updated
#         pass

#     def remove_trigger(self, trigger):
#         # This method is called when trigger is deleted
#         pass




class WebpageTestStatusSensor(PollingSensor):
    """
    Sensor will poll the status of queued Webpagetest requests
    """

    def __init__(self, sensor_service, config=None, poll_interval=60):
        super(WebpageTestStatusSensor, self).__init__(
            sensor_service=sensor_service, config=config, poll_interval=poll_interval
        )

        self._logger = self.sensor_service.get_logger(
            name=self.__class__.__name__)
        self._wpt_url = "https://webpagetest.org"
        self._key = None
        self._trigger_name = "status_checker"
        self._trigger_pack = "st2_poc"
        self._trigger_ref = ".".join([self._trigger_pack, self._trigger_name])

    def setup(self):
        self._wpt_url = self._config.get("wpt_url", "https://webpagetest.org")
        self._key = self._config.get("key", None)

    def _get_test_status(self, test_id):
        """Get test status"""
        params = {"f": "json"}
        if self._key:
            params["k"] = self._config.get("key", None)
        if test_id:
            params["test"] = test_id

        response = requests.get(
            "{0}/testStatus.php".format(self._wpt_url), params=params
        )
        return response.json()

    def poll(self):
        # wpt_queue_data = self.sensor_service.get_value(
        #     "wpt_queue", local=False)
        # wpt_queue_items = []
        # self._logger.info("WPT Queue Data " + wpt_queue_data)
        # try:
        #     wpt_queue_items = json.loads(wpt_queue_data)
        # except Exception as ex:
        #     self._logger.error("Some error occurred: " + str(ex))

        # if len(wpt_queue_items) == 0:
        #     self._logger.info("No items in queue")
        #     return

        # updated_queue = []
        # for item in wpt_queue_items:
        #     test_id = item.get("test_id")
        #     if test_id:
        #         data = self._get_test_status(test_id)
        #         self._logger.info("Test Data received: %s", json.dumps(data))
        #         if (
        #             data["statusCode"] in [200, 201, 202]
        #             and data["statusText"] == "Test Complete"
        #         ):
        #             self.sensor_service.dispatch(
        #                 trigger=self._trigger_ref,
        #                 payload={
        #                     "status": data["statusText"],
        #                     "test_id": test_id,
        #                     "issue_key": item.get("issue_key"),
        #                     "wpt_req": item.get("wpt_req"),
        #                     "wpt_response": data.get("data"),
        #                 },
        #             )
        #         else:
        #             updated_queue.append(copy.deepcopy(item))

        # self._logger.info("Updated value: " + json.dumps(updated_queue))
        # self.sensor_service.set_value(
        #     "wpt_queue", local=False, value=json.dumps(updated_queue)
        # )
        self.sensor_service.dispatch(
            trigger=self._trigger_ref,
            payload={
                "status": "TEST",
                "test_id": "ID",
                "issue_key": "ISSUE_KEY",
                "wpt_req": "WPT_REQ",
                "wpt_response": "RESP",
            }
        )

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
