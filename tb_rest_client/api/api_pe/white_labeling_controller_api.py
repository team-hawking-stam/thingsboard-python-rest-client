# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2023. ThingsBoard
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


class WhiteLabelingControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_current_login_white_label_params_using_get(self, **kwargs):  # noqa: E501
        """Get Login White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

        Fetch the Login  White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the Login White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_login_white_label_params_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: LoginWhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_login_white_label_params_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_login_white_label_params_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_login_white_label_params_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Login White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

        Fetch the Login  White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the Login White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_login_white_label_params_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: LoginWhiteLabelingParams
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
                    " to method get_current_login_white_label_params_using_get" % key
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
            '/api/whiteLabel/currentLoginWhiteLabelParams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoginWhiteLabelingParams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_current_white_label_params_using_get(self, **kwargs):  # noqa: E501
        """Get White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

        Fetch the White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_white_label_params_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_white_label_params_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_white_label_params_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_white_label_params_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

        Fetch the White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_white_label_params_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WhiteLabelingParams
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
                    " to method get_current_white_label_params_using_get" % key
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
            '/api/whiteLabel/currentWhiteLabelParams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WhiteLabelingParams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_login_white_label_params_using_get(self, **kwargs):  # noqa: E501
        """Get Login White Labeling parameters  # noqa: E501

        Returns login white-labeling parameters based on the hostname from request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_login_white_label_params_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logo_image_checksum: Logo image checksum. Expects value from the browser cache to compare it with the value from settings. If value matches, the 'logoImageUrl' will be null.
        :param str favicon_checksum: Favicon image checksum. Expects value from the browser cache to compare it with the value from settings. If value matches, the 'faviconImageUrl' will be null.
        :return: LoginWhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_login_white_label_params_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_login_white_label_params_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_login_white_label_params_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Login White Labeling parameters  # noqa: E501

        Returns login white-labeling parameters based on the hostname from request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_login_white_label_params_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logo_image_checksum: Logo image checksum. Expects value from the browser cache to compare it with the value from settings. If value matches, the 'logoImageUrl' will be null.
        :param str favicon_checksum: Favicon image checksum. Expects value from the browser cache to compare it with the value from settings. If value matches, the 'faviconImageUrl' will be null.
        :return: LoginWhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['logo_image_checksum', 'favicon_checksum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_login_white_label_params_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'logo_image_checksum' in params:
            query_params.append(('logoImageChecksum', params['logo_image_checksum']))  # noqa: E501
        if 'favicon_checksum' in params:
            query_params.append(('faviconChecksum', params['favicon_checksum']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/whiteLabel/loginWhiteLabelParams{?faviconChecksum,logoImageChecksum}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoginWhiteLabelingParams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_white_label_params_using_get(self, **kwargs):  # noqa: E501
        """Get White Labeling parameters  # noqa: E501

        Returns white-labeling parameters for the current user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_white_label_params_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logo_image_checksum: Logo image checksum. Expects value from the browser cache to compare it with the value from settings. If value matches, the 'logoImageUrl' will be null.
        :param str favicon_checksum: Favicon image checksum. Expects value from the browser cache to compare it with the value from settings. If value matches, the 'faviconImageUrl' will be null.
        :return: WhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_white_label_params_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_white_label_params_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_white_label_params_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get White Labeling parameters  # noqa: E501

        Returns white-labeling parameters for the current user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_white_label_params_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logo_image_checksum: Logo image checksum. Expects value from the browser cache to compare it with the value from settings. If value matches, the 'logoImageUrl' will be null.
        :param str favicon_checksum: Favicon image checksum. Expects value from the browser cache to compare it with the value from settings. If value matches, the 'faviconImageUrl' will be null.
        :return: WhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['logo_image_checksum', 'favicon_checksum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_white_label_params_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'logo_image_checksum' in params:
            query_params.append(('logoImageChecksum', params['logo_image_checksum']))  # noqa: E501
        if 'favicon_checksum' in params:
            query_params.append(('faviconChecksum', params['favicon_checksum']))  # noqa: E501

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
            '/api/whiteLabel/whiteLabelParams{?faviconChecksum,logoImageChecksum}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WhiteLabelingParams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def is_customer_white_labeling_allowed_using_get(self, **kwargs):  # noqa: E501
        """Check Customer White Labeling Allowed  # noqa: E501

        Check if the White Labeling is enabled for the customers of the current tenant  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.is_customer_white_labeling_allowed_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.is_customer_white_labeling_allowed_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.is_customer_white_labeling_allowed_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def is_customer_white_labeling_allowed_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Check Customer White Labeling Allowed  # noqa: E501

        Check if the White Labeling is enabled for the customers of the current tenant  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.is_customer_white_labeling_allowed_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
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
                    " to method is_customer_white_labeling_allowed_using_get" % key
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
            '/api/whiteLabel/isCustomerWhiteLabelingAllowed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def is_white_labeling_allowed_using_get(self, **kwargs):  # noqa: E501
        """Check White Labeling Allowed  # noqa: E501

        Check if the White Labeling is enabled for the current user owner (tenant or customer)  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.is_white_labeling_allowed_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.is_white_labeling_allowed_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.is_white_labeling_allowed_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def is_white_labeling_allowed_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Check White Labeling Allowed  # noqa: E501

        Check if the White Labeling is enabled for the current user owner (tenant or customer)  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.is_white_labeling_allowed_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
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
                    " to method is_white_labeling_allowed_using_get" % key
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
            '/api/whiteLabel/isWhiteLabelingAllowed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def preview_white_label_params_using_post(self, **kwargs):  # noqa: E501
        """Preview Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

        Merge the White Labeling configuration with the parent configuration and return the result.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.preview_white_label_params_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WhiteLabelingParams body:
        :return: WhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.preview_white_label_params_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.preview_white_label_params_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def preview_white_label_params_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Preview Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

        Merge the White Labeling configuration with the parent configuration and return the result.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.preview_white_label_params_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WhiteLabelingParams body:
        :return: WhiteLabelingParams
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
                    " to method preview_white_label_params_using_post" % key
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
            '/api/whiteLabel/previewWhiteLabelParams', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WhiteLabelingParams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_login_white_label_params_using_post(self, **kwargs):  # noqa: E501
        """Create Or Update Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

        Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_login_white_label_params_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginWhiteLabelingParams body:
        :return: LoginWhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_login_white_label_params_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_login_white_label_params_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_login_white_label_params_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Or Update Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

        Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_login_white_label_params_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginWhiteLabelingParams body:
        :return: LoginWhiteLabelingParams
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
                    " to method save_login_white_label_params_using_post" % key
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
            '/api/whiteLabel/loginWhiteLabelParams', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoginWhiteLabelingParams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_white_label_params_using_post(self, **kwargs):  # noqa: E501
        """Create Or Update White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

        Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_white_label_params_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WhiteLabelingParams body:
        :return: WhiteLabelingParams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_white_label_params_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_white_label_params_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_white_label_params_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Or Update White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

        Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_white_label_params_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WhiteLabelingParams body:
        :return: WhiteLabelingParams
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
                    " to method save_white_label_params_using_post" % key
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
            '/api/whiteLabel/whiteLabelParams', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WhiteLabelingParams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
