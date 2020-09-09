import json
import requests
import io
import logging
import time
from typing import Union
from urllib import parse


LOGGER = logging.getLogger(__name__)

from st2reactor.sensor.base import PollingSensor
from sensors.sample_polling_sensor import ApiPollingSensor


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
            # poll_interval=poll_interval,
            # endpoint='http://www.google.com',
            # trigger='hello_st2.integration_property_fetch',
            # greeting='FINALLY WORKING!!')
        self._poll_interval = poll_interval
        # self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._endpoint = 'https://zeroday-onboard.default.abattery.appbattery.nss1.tn.akamai.com/zeroday/v1/integration'
        self._trigger = trigger or 'hello_st2.integration_property_fetch'
        self._greeting = greeting

    def poll(self):
        # self._logger.debug('WorkingSensor dispatching trigger...')
        payload = {
            'greeting': self._greeting or 'API Polling Sensor 2',
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

    # def make_request_with_retry(
    #         self,
    #         method: str,
    #         url: str,
    #         headers: dict,
    #         data: Union[dict, str] = None,
    #         params: dict = None,
    #         retry_count: int = None,
    #         retry_wait_time: int = None,
    #         verify: str = False,
    #         cert: tuple = None,
    #         timeout: tuple = None,
    #         extra_logging_args: dict = None,
    # ):
    #     """
    #     Retry a HTTP request with a configured retry count and timeout.

    #     :param extra_logging_args:
    #     :param params:
    #     :param retry_wait_time:
    #     :param retry_count:
    #     :param method:
    #     :param url:
    #     :param headers:
    #     :param data:
    #     :param verify:
    #     :param cert:
    #     :return:
    #     """
    #     if data is None:
    #         data = {}
    #     try:
    #         if retry_count is None:
    #             retry_count = 3
    #         if retry_wait_time is None:
    #             retry_wait_time = 4000
    #         if timeout is None:
    #             read_timeout = 6000
    #             timeout = (6000, read_timeout)

    #         err_msg = (
    #             "Request Failed with status code {status_code}, method: {method}, url: {url}, "
    #             "headers: {headers}, params: {params}, data: {data}, verify: {verify}, "
    #             "cert: {cert}, response: {response}"
    #         )
    #         report_id = None
    #         api_struct = None
    #         response = None

    #         if extra_logging_args is not None and isinstance(
    #                 extra_logging_args, dict
    #         ):
    #             report_id = extra_logging_args.get("report_id")
    #             api_struct = extra_logging_args.get("api_structure")
    #             extra_msg = ", "
    #             for _key, _val in extra_logging_args.items():
    #                 if isinstance(_val, dict):
    #                     pass
    #                 extra_msg += "%s: %s " % (_key, _val)
    #             extra_msg = extra_msg.strip()
    #             err_msg += extra_msg

    #         start_time = time.time()
    #         parsed_uri = parse.urlparse(url)
    #         cur_retry_wait_time = retry_wait_time

    #         request_args = {
    #             "method": method,
    #             "url": url,
    #             "headers": headers,
    #             "params": params,
    #             "data": data,
    #             "verify": verify,
    #             "cert": cert,
    #             "timeout": timeout,
    #         }
    #         request_exception_occurred = False
    #         try:
    #             response = requests.request(**request_args)
    #             LOGGER.info("%s", response.status_code)
    #         except (
    #                 requests.exceptions.HTTPError,
    #                 requests.exceptions.ConnectionError,
    #                 requests.exceptions.ConnectTimeout,
    #                 requests.exceptions.ChunkedEncodingError,
    #         ) as exc:
    #             print(
    #                 "cannot complete request due to %s for report_id %s api structure %s",
    #                 str(exc),
    #                 report_id,
    #                 api_struct,
    #             )
    #             request_exception_occurred = True

    #         while retry_count > 0 and (
    #                 request_exception_occurred
    #                 or (response is not None and response.status_code >= 500)
    #         ):
    #             if response is not None:
    #                 LOGGER.error(
    #                     err_msg.format(
    #                         status_code=response.status_code,
    #                         method=method,
    #                         url=url,
    #                         headers=headers,
    #                         params=params,
    #                         data=data,
    #                         verify=verify,
    #                         cert=cert,
    #                         response=response.content,
    #                     )
    #                 )
    #             print(
    #                 "sleeping for %s seconds, report_id %s api structure %s retry count=%s",
    #                 cur_retry_wait_time,
    #                 report_id,
    #                 api_struct,
    #                 retry_count
    #             )
    #             time.sleep(cur_retry_wait_time)
    #             LOGGER.info(
    #                 "making request now for report_id %s api structure %s, remaining retry counts %s",
    #                 report_id,
    #                 api_struct,
    #                 retry_count - 1,
    #             )
    #             start_time = time.time()
    #         if response is None:
    #             raise requests.exceptions.ConnectionError(
    #                 "cannot complete request due to HTTP connection error"
    #             )
    #         if response.status_code in [200, 201]:
    #             LOGGER.info(
    #                 "Total time taken for api structure %s report_id %s is %s seconds",
    #                 api_struct,
    #                 report_id,
    #                 int(time.time() - start_time),
    #             )
    #         elif response.status_code < 500:
    #             LOGGER.error(
    #                 err_msg.format(
    #                     status_code=response.status_code,
    #                     method=method,
    #                     url=url,
    #                     headers=headers,
    #                     params=params,
    #                     data=data,
    #                     verify=verify,
    #                     cert=cert,
    #                     response=response.content,
    #                 )
    #             )
    #         return response
    #     except Exception as exc:
    #         if type(exc).__name__ != requests.exceptions.ConnectionError.__name__:

    #             LOGGER.exception("Unhandled exception in make_request_with_retry")
    #         raise