# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3PAAS-RC1
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class WidgetsBundleControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_widgets_bundle_using_delete(self, widgets_bundle_id, **kwargs):  # noqa: E501
        """Delete widgets bundle (deleteWidgetsBundle)  # noqa: E501

        Deletes the widget bundle. Referencing non-existing Widget Bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_widgets_bundle_using_delete(widgets_bundle_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widgets_bundle_id: A string value representing the widget bundle id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_widgets_bundle_using_delete_with_http_info(widgets_bundle_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_widgets_bundle_using_delete_with_http_info(widgets_bundle_id, **kwargs)  # noqa: E501
            return data

    def delete_widgets_bundle_using_delete_with_http_info(self, widgets_bundle_id, **kwargs):  # noqa: E501
        """Delete widgets bundle (deleteWidgetsBundle)  # noqa: E501

        Deletes the widget bundle. Referencing non-existing Widget Bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_widgets_bundle_using_delete_with_http_info(widgets_bundle_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widgets_bundle_id: A string value representing the widget bundle id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['widgets_bundle_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_widgets_bundle_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'widgets_bundle_id' is set
        if ('widgets_bundle_id' not in params or
                params['widgets_bundle_id'] is None):
            raise ValueError("Missing the required parameter `widgets_bundle_id` when calling `delete_widgets_bundle_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'widgets_bundle_id' in params:
            path_params['widgetsBundleId'] = params['widgets_bundle_id']  # noqa: E501

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
            '/api/widgetsBundle/{widgetsBundleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_widgets_bundle_by_id_using_get(self, widgets_bundle_id, **kwargs):  # noqa: E501
        """Get Widget Bundle (getWidgetsBundleById)  # noqa: E501

        Get the Widget Bundle based on the provided Widget Bundle Id. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.   Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundle_by_id_using_get(widgets_bundle_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widgets_bundle_id: A string value representing the widget bundle id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: WidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_widgets_bundle_by_id_using_get_with_http_info(widgets_bundle_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_widgets_bundle_by_id_using_get_with_http_info(widgets_bundle_id, **kwargs)  # noqa: E501
            return data

    def get_widgets_bundle_by_id_using_get_with_http_info(self, widgets_bundle_id, **kwargs):  # noqa: E501
        """Get Widget Bundle (getWidgetsBundleById)  # noqa: E501

        Get the Widget Bundle based on the provided Widget Bundle Id. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.   Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundle_by_id_using_get_with_http_info(widgets_bundle_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widgets_bundle_id: A string value representing the widget bundle id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: WidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['widgets_bundle_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_widgets_bundle_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'widgets_bundle_id' is set
        if ('widgets_bundle_id' not in params or
                params['widgets_bundle_id'] is None):
            raise ValueError("Missing the required parameter `widgets_bundle_id` when calling `get_widgets_bundle_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'widgets_bundle_id' in params:
            path_params['widgetsBundleId'] = params['widgets_bundle_id']  # noqa: E501

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
            '/api/widgetsBundle/{widgetsBundleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WidgetsBundle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_widgets_bundles_using_get(self, **kwargs):  # noqa: E501
        """Get all Widget Bundles (getWidgetsBundles)  # noqa: E501

        Returns an array of Widget Bundle objects that are available for current user.Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.    Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundles_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[WidgetsBundle]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_widgets_bundles_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_widgets_bundles_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_widgets_bundles_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all Widget Bundles (getWidgetsBundles)  # noqa: E501

        Returns an array of Widget Bundle objects that are available for current user.Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.    Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundles_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[WidgetsBundle]
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
                    " to method get_widgets_bundles_using_get" % key
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
            '/api/widgetsBundles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WidgetsBundle]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_widgets_bundles_using_get1(self, page_size, page, **kwargs):  # noqa: E501
        """Get Widget Bundles (getWidgetsBundles)  # noqa: E501

        Returns a page of Widget Bundle objects available for current user. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundles_using_get1(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The case insensitive 'startsWith' filter based on the widget bundle title.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :return: PageDataWidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_widgets_bundles_using_get1_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_widgets_bundles_using_get1_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_widgets_bundles_using_get1_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """Get Widget Bundles (getWidgetsBundles)  # noqa: E501

        Returns a page of Widget Bundle objects available for current user. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widgets_bundles_using_get1_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The case insensitive 'startsWith' filter based on the widget bundle title.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :return: PageDataWidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_widgets_bundles_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_widgets_bundles_using_get1`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_widgets_bundles_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501

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
            '/api/widgetsBundles{?page,pageSize,sortOrder,sortProperty,textSearch}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataWidgetsBundle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_widgets_bundle_using_post(self, **kwargs):  # noqa: E501
        """Create Or Update Widget Bundle (saveWidgetsBundle)  # noqa: E501

        Create or update the Widget Bundle. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  When creating the bundle, platform generates Widget Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Bundle Id will be present in the response. Specify existing Widget Bundle id to update the Widget Bundle. Referencing non-existing Widget Bundle Id will cause 'Not Found' error.  Widget Bundle alias is unique in the scope of tenant. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create bundle request is sent by user with 'SYS_ADMIN' authority.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_widgets_bundle_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidgetsBundle body:
        :return: WidgetsBundle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_widgets_bundle_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_widgets_bundle_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_widgets_bundle_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Or Update Widget Bundle (saveWidgetsBundle)  # noqa: E501

        Create or update the Widget Bundle. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  When creating the bundle, platform generates Widget Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Bundle Id will be present in the response. Specify existing Widget Bundle id to update the Widget Bundle. Referencing non-existing Widget Bundle Id will cause 'Not Found' error.  Widget Bundle alias is unique in the scope of tenant. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create bundle request is sent by user with 'SYS_ADMIN' authority.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_widgets_bundle_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidgetsBundle body:
        :return: WidgetsBundle
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
                    " to method save_widgets_bundle_using_post" % key
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
            '/api/widgetsBundle', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WidgetsBundle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
