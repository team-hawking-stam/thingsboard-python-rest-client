# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class EntityQueryControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def count_entities_by_query_using_post(self, query, **kwargs):  # noqa: E501
        """countEntitiesByQuery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_entities_by_query_using_post(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EntityCountQuery query: query (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.count_entities_by_query_using_post_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.count_entities_by_query_using_post_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def count_entities_by_query_using_post_with_http_info(self, query, **kwargs):  # noqa: E501
        """countEntitiesByQuery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_entities_by_query_using_post_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EntityCountQuery query: query (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method count_entities_by_query_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `query` when calling `count_entities_by_query_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/entitiesQuery/count', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_alarm_data_by_query_using_post(self, query, **kwargs):  # noqa: E501
        """findAlarmDataByQuery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_alarm_data_by_query_using_post(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AlarmDataQuery query: query (required)
        :return: PageDataAlarmData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_alarm_data_by_query_using_post_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.find_alarm_data_by_query_using_post_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def find_alarm_data_by_query_using_post_with_http_info(self, query, **kwargs):  # noqa: E501
        """findAlarmDataByQuery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_alarm_data_by_query_using_post_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AlarmDataQuery query: query (required)
        :return: PageDataAlarmData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_alarm_data_by_query_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `query` when calling `find_alarm_data_by_query_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarmsQuery/find', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataAlarmData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_entity_data_by_query_using_post(self, query, **kwargs):  # noqa: E501
        """findEntityDataByQuery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_entity_data_by_query_using_post(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EntityDataQuery query: query (required)
        :return: PageDataEntityData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_entity_data_by_query_using_post_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.find_entity_data_by_query_using_post_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def find_entity_data_by_query_using_post_with_http_info(self, query, **kwargs):  # noqa: E501
        """findEntityDataByQuery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_entity_data_by_query_using_post_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EntityDataQuery query: query (required)
        :return: PageDataEntityData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_entity_data_by_query_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `query` when calling `find_entity_data_by_query_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/entitiesQuery/find', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataEntityData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_entity_timeseries_and_attributes_keys_by_query_using_post(self, query, timeseries, attributes,
                                                                       **kwargs):  # noqa: E501
        """findEntityTimeseriesAndAttributesKeysByQuery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_entity_timeseries_and_attributes_keys_by_query_using_post(query, timeseries, attributes, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EntityDataQuery query: query (required)
        :param bool timeseries: timeseries (required)
        :param bool attributes: attributes (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_entity_timeseries_and_attributes_keys_by_query_using_post_with_http_info(query, timeseries,
                                                                                                      attributes,
                                                                                                      **kwargs)  # noqa: E501
        else:
            (data) = self.find_entity_timeseries_and_attributes_keys_by_query_using_post_with_http_info(query,
                                                                                                        timeseries,
                                                                                                        attributes,
                                                                                                        **kwargs)  # noqa: E501
            return data

    def find_entity_timeseries_and_attributes_keys_by_query_using_post_with_http_info(self, query, timeseries,
                                                                                      attributes,
                                                                                      **kwargs):  # noqa: E501
        """findEntityTimeseriesAndAttributesKeysByQuery  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_entity_timeseries_and_attributes_keys_by_query_using_post_with_http_info(query, timeseries, attributes, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EntityDataQuery query: query (required)
        :param bool timeseries: timeseries (required)
        :param bool attributes: attributes (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'timeseries', 'attributes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_entity_timeseries_and_attributes_keys_by_query_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `query` when calling `find_entity_timeseries_and_attributes_keys_by_query_using_post`")  # noqa: E501
        # verify the required parameter 'timeseries' is set
        if self.api_client.client_side_validation and ('timeseries' not in params or
                                                       params['timeseries'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `timeseries` when calling `find_entity_timeseries_and_attributes_keys_by_query_using_post`")  # noqa: E501
        # verify the required parameter 'attributes' is set
        if self.api_client.client_side_validation and ('attributes' not in params or
                                                       params['attributes'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `attributes` when calling `find_entity_timeseries_and_attributes_keys_by_query_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'timeseries' in params:
            query_params.append(('timeseries', params['timeseries']))  # noqa: E501
        if 'attributes' in params:
            query_params.append(('attributes', params['attributes']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/entitiesQuery/find/keys{?timeseries,attributes}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)