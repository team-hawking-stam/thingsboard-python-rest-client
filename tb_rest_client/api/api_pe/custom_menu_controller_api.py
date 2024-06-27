# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.7.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2024. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class CustomMenuControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_current_custom_menu_using_get(self, **kwargs):  # noqa: E501
        """Get Custom Menu configuration (getCustomMenu)  # noqa: E501

        Fetch the Custom Menu object that corresponds to the authority of the user. The API call is designed to load the custom menu items for edition. So, the result is NOT merged with the parent level configuration. Let's assume there is a custom menu configured on a system level. And there is no custom menu items configured on a tenant level. In such a case, the API call will return empty object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_custom_menu_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomMenu
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_custom_menu_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_custom_menu_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_custom_menu_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Custom Menu configuration (getCustomMenu)  # noqa: E501

        Fetch the Custom Menu object that corresponds to the authority of the user. The API call is designed to load the custom menu items for edition. So, the result is NOT merged with the parent level configuration. Let's assume there is a custom menu configured on a system level. And there is no custom menu items configured on a tenant level. In such a case, the API call will return empty object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_custom_menu_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomMenu
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_custom_menu_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customMenu/currentCustomMenu', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomMenu',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_custom_menu_using_get(self, **kwargs):  # noqa: E501
        """Get end-user Custom Menu configuration (getCustomMenu)  # noqa: E501

        Fetch the Custom Menu object for the end user. The custom menu is configured in the white labeling parameters. If custom menu configuration on the tenant level is present, it overrides the menu configuration of the system level. Similar, if the custom menu configuration on the customer level is present, it overrides the menu configuration of the tenant level.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_menu_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomMenu
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_menu_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_menu_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_custom_menu_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get end-user Custom Menu configuration (getCustomMenu)  # noqa: E501

        Fetch the Custom Menu object for the end user. The custom menu is configured in the white labeling parameters. If custom menu configuration on the tenant level is present, it overrides the menu configuration of the system level. Similar, if the custom menu configuration on the customer level is present, it overrides the menu configuration of the tenant level.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_menu_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomMenu
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_menu_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customMenu/customMenu', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomMenu',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_custom_menu_using_post(self, **kwargs):  # noqa: E501
        """Create Or Update Custom Menu (saveCustomMenu)  # noqa: E501

        Creates or Updates the Custom Menu configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_custom_menu_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomMenu body:
        :return: CustomMenu
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_custom_menu_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_custom_menu_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_custom_menu_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Or Update Custom Menu (saveCustomMenu)  # noqa: E501

        Creates or Updates the Custom Menu configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_custom_menu_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomMenu body:
        :return: CustomMenu
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_custom_menu_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customMenu/customMenu', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomMenu',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
