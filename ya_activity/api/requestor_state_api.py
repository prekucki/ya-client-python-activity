# coding: utf-8

"""
    Yagna Activity API

    It conforms with capability level 1 of the [Activity API specification](https://docs.google.com/document/d/1BXaN32ediXdBHljEApmznSfbuudTU8TmvOmHKl0gmQM).  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ya_activity.api_client import ApiClient
from ya_activity.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RequestorStateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_activity_state(self, activity_id, **kwargs):  # noqa: E501
        """Get state of specified Activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_activity_state(activity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str activity_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ActivityState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_activity_state_with_http_info(activity_id, **kwargs)  # noqa: E501

    def get_activity_state_with_http_info(self, activity_id, **kwargs):  # noqa: E501
        """Get state of specified Activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_activity_state_with_http_info(activity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str activity_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ActivityState, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'activity_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_activity_state" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'activity_id' is set
        if self.api_client.client_side_validation and ('activity_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['activity_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `activity_id` when calling `get_activity_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activity_id' in local_var_params:
            path_params['activityId'] = local_var_params['activity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['app_key']  # noqa: E501

        return self.api_client.call_api(
            '/activity/{activityId}/state', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityState',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_activity_usage(self, activity_id, **kwargs):  # noqa: E501
        """Get usage of specified Activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_activity_usage(activity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str activity_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[float]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_activity_usage_with_http_info(activity_id, **kwargs)  # noqa: E501

    def get_activity_usage_with_http_info(self, activity_id, **kwargs):  # noqa: E501
        """Get usage of specified Activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_activity_usage_with_http_info(activity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str activity_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[float], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'activity_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_activity_usage" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'activity_id' is set
        if self.api_client.client_side_validation and ('activity_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['activity_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `activity_id` when calling `get_activity_usage`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activity_id' in local_var_params:
            path_params['activityId'] = local_var_params['activity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['app_key']  # noqa: E501

        return self.api_client.call_api(
            '/activity/{activityId}/usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[float]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_running_command(self, activity_id, **kwargs):  # noqa: E501
        """Get running command for a specified Activity.  # noqa: E501

        **Note:** This call shall get routed directly to ExeUnit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_running_command(activity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str activity_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ExeScriptCommandState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_running_command_with_http_info(activity_id, **kwargs)  # noqa: E501

    def get_running_command_with_http_info(self, activity_id, **kwargs):  # noqa: E501
        """Get running command for a specified Activity.  # noqa: E501

        **Note:** This call shall get routed directly to ExeUnit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_running_command_with_http_info(activity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str activity_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ExeScriptCommandState, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'activity_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_running_command" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'activity_id' is set
        if self.api_client.client_side_validation and ('activity_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['activity_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `activity_id` when calling `get_running_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activity_id' in local_var_params:
            path_params['activityId'] = local_var_params['activity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['app_key']  # noqa: E501

        return self.api_client.call_api(
            '/activity/{activityId}/command', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExeScriptCommandState',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
