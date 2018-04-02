# coding: utf-8

"""
    Dynamix

    Sign up for Dynamix & grab your token.  # noqa: E501

    OpenAPI spec version: v0.1.0
    Contact: david@theadsontop.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CatalogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_catalog_item(self, auth_token, body, **kwargs):  # noqa: E501
        """Create a catalog item  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_catalog_item(auth_token, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param CatalogItem body: (required)
        :return: CatalogItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_catalog_item_with_http_info(auth_token, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_catalog_item_with_http_info(auth_token, body, **kwargs)  # noqa: E501
            return data

    def create_catalog_item_with_http_info(self, auth_token, body, **kwargs):  # noqa: E501
        """Create a catalog item  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_catalog_item_with_http_info(auth_token, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param CatalogItem body: (required)
        :return: CatalogItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_catalog_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `create_catalog_item`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_catalog_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/catalog/item', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogItem',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_catalog_item(self, auth_token, item_rid, **kwargs):  # noqa: E501
        """Delete a Catalog entry  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_catalog_item(auth_token, item_rid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str item_rid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_catalog_item_with_http_info(auth_token, item_rid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_catalog_item_with_http_info(auth_token, item_rid, **kwargs)  # noqa: E501
            return data

    def delete_catalog_item_with_http_info(self, auth_token, item_rid, **kwargs):  # noqa: E501
        """Delete a Catalog entry  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_catalog_item_with_http_info(auth_token, item_rid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str item_rid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'item_rid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_catalog_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `delete_catalog_item`")  # noqa: E501
        # verify the required parameter 'item_rid' is set
        if ('item_rid' not in params or
                params['item_rid'] is None):
            raise ValueError("Missing the required parameter `item_rid` when calling `delete_catalog_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_rid' in params:
            query_params.append(('itemRid', params['item_rid']))  # noqa: E501

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/catalog/item', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_catalog_item(self, auth_token, item_rid, **kwargs):  # noqa: E501
        """Get a single Catalog Item  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_catalog_item(auth_token, item_rid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str item_rid: (required)
        :return: CatalogItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_catalog_item_with_http_info(auth_token, item_rid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_catalog_item_with_http_info(auth_token, item_rid, **kwargs)  # noqa: E501
            return data

    def get_catalog_item_with_http_info(self, auth_token, item_rid, **kwargs):  # noqa: E501
        """Get a single Catalog Item  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_catalog_item_with_http_info(auth_token, item_rid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str item_rid: (required)
        :return: CatalogItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'item_rid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `get_catalog_item`")  # noqa: E501
        # verify the required parameter 'item_rid' is set
        if ('item_rid' not in params or
                params['item_rid'] is None):
            raise ValueError("Missing the required parameter `item_rid` when calling `get_catalog_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_rid' in params:
            query_params.append(('itemRid', params['item_rid']))  # noqa: E501

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/catalog/item', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogItem',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_catalog_items(self, auth_token, body, **kwargs):  # noqa: E501
        """Get Catalog Items Paged  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_catalog_items(auth_token, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param CatalogItemPagedRequest body: (required)
        :return: list[CatalogItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_catalog_items_with_http_info(auth_token, body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_catalog_items_with_http_info(auth_token, body, **kwargs)  # noqa: E501
            return data

    def get_catalog_items_with_http_info(self, auth_token, body, **kwargs):  # noqa: E501
        """Get Catalog Items Paged  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_catalog_items_with_http_info(auth_token, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param CatalogItemPagedRequest body: (required)
        :return: list[CatalogItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `get_catalog_items`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_catalog_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/catalog/item/bulk/get', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CatalogItem]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_catalog(self, auth_token, body, **kwargs):  # noqa: E501
        """List the Catalog entries  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_catalog(auth_token, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param PagedSearchQuery body: (required)
        :return: PagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_catalog_with_http_info(auth_token, body, **kwargs)  # noqa: E501
        else:
            (data) = self.list_catalog_with_http_info(auth_token, body, **kwargs)  # noqa: E501
            return data

    def list_catalog_with_http_info(self, auth_token, body, **kwargs):  # noqa: E501
        """List the Catalog entries  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_catalog_with_http_info(auth_token, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param PagedSearchQuery body: (required)
        :return: PagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_catalog" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `list_catalog`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `list_catalog`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/catalog/list/search', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_catalog_0(self, auth_token, type, body, **kwargs):  # noqa: E501
        """List the Catalog entries  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_catalog_0(auth_token, type, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str type: (required)
        :param PagedRequest body: (required)
        :return: PagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_catalog_0_with_http_info(auth_token, type, body, **kwargs)  # noqa: E501
        else:
            (data) = self.list_catalog_0_with_http_info(auth_token, type, body, **kwargs)  # noqa: E501
            return data

    def list_catalog_0_with_http_info(self, auth_token, type, body, **kwargs):  # noqa: E501
        """List the Catalog entries  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_catalog_0_with_http_info(auth_token, type, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str type: (required)
        :param PagedRequest body: (required)
        :return: PagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'type', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_catalog_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `list_catalog_0`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `list_catalog_0`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `list_catalog_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/catalog/list/type', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_catalog_item(self, auth_token, item_rid, body, **kwargs):  # noqa: E501
        """Update a Catalog entry  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_catalog_item(auth_token, item_rid, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str item_rid: (required)
        :param CatalogItem body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_catalog_item_with_http_info(auth_token, item_rid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_catalog_item_with_http_info(auth_token, item_rid, body, **kwargs)  # noqa: E501
            return data

    def update_catalog_item_with_http_info(self, auth_token, item_rid, body, **kwargs):  # noqa: E501
        """Update a Catalog entry  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_catalog_item_with_http_info(auth_token, item_rid, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str item_rid: (required)
        :param CatalogItem body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'item_rid', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_catalog_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `update_catalog_item`")  # noqa: E501
        # verify the required parameter 'item_rid' is set
        if ('item_rid' not in params or
                params['item_rid'] is None):
            raise ValueError("Missing the required parameter `item_rid` when calling `update_catalog_item`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_catalog_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_rid' in params:
            query_params.append(('itemRid', params['item_rid']))  # noqa: E501

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/catalog/item', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
