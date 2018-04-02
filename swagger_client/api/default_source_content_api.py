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


class DefaultSourceContentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_content(self, auth_token, namespace, server, **kwargs):  # noqa: E501
        """DefaultSourceContentResource - deleteContent  # noqa: E501

        Delete a content delivery entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_content(auth_token, namespace, server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str server: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_content_with_http_info(auth_token, namespace, server, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_content_with_http_info(auth_token, namespace, server, **kwargs)  # noqa: E501
            return data

    def delete_content_with_http_info(self, auth_token, namespace, server, **kwargs):  # noqa: E501
        """DefaultSourceContentResource - deleteContent  # noqa: E501

        Delete a content delivery entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_content_with_http_info(auth_token, namespace, server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str server: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'namespace', 'server']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `delete_content`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `delete_content`")  # noqa: E501
        # verify the required parameter 'server' is set
        if ('server' not in params or
                params['server'] is None):
            raise ValueError("Missing the required parameter `server` when calling `delete_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server' in params:
            query_params.append(('server', params['server']))  # noqa: E501

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501
        if 'namespace' in params:
            header_params['namespace'] = params['namespace']  # noqa: E501

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
            '/api/source-engine/default/register', 'DELETE',
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

    def get_all_authorized_content_paged(self, auth_token, namespace, body, **kwargs):  # noqa: E501
        """get_all_authorized_content_paged  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_authorized_content_paged(auth_token, namespace, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param PagedRequest body: (required)
        :return: PagedResponseContentRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_authorized_content_paged_with_http_info(auth_token, namespace, body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_authorized_content_paged_with_http_info(auth_token, namespace, body, **kwargs)  # noqa: E501
            return data

    def get_all_authorized_content_paged_with_http_info(self, auth_token, namespace, body, **kwargs):  # noqa: E501
        """get_all_authorized_content_paged  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_authorized_content_paged_with_http_info(auth_token, namespace, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param PagedRequest body: (required)
        :return: PagedResponseContentRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'namespace', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_authorized_content_paged" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `get_all_authorized_content_paged`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `get_all_authorized_content_paged`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_all_authorized_content_paged`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501
        if 'namespace' in params:
            header_params['namespace'] = params['namespace']  # noqa: E501

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
            '/api/source-engine/default/register/paged', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResponseContentRequest',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_content_request(self, auth_token, namespace, server, **kwargs):  # noqa: E501
        """get_content_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_content_request(auth_token, namespace, server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str server: (required)
        :return: ContentRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_content_request_with_http_info(auth_token, namespace, server, **kwargs)  # noqa: E501
        else:
            (data) = self.get_content_request_with_http_info(auth_token, namespace, server, **kwargs)  # noqa: E501
            return data

    def get_content_request_with_http_info(self, auth_token, namespace, server, **kwargs):  # noqa: E501
        """get_content_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_content_request_with_http_info(auth_token, namespace, server, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str server: (required)
        :return: ContentRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'namespace', 'server']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `get_content_request`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `get_content_request`")  # noqa: E501
        # verify the required parameter 'server' is set
        if ('server' not in params or
                params['server'] is None):
            raise ValueError("Missing the required parameter `server` when calling `get_content_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server' in params:
            query_params.append(('server', params['server']))  # noqa: E501

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501
        if 'namespace' in params:
            header_params['namespace'] = params['namespace']  # noqa: E501

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
            '/api/source-engine/default/register', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContentRequest',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_new_content(self, auth_token, namespace, body, **kwargs):  # noqa: E501
        """DefaultSourceContentResource - registerNewContent  # noqa: E501

        Set a content delivery entry for a set of content receivers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.register_new_content(auth_token, namespace, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param ContentRequest body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.register_new_content_with_http_info(auth_token, namespace, body, **kwargs)  # noqa: E501
        else:
            (data) = self.register_new_content_with_http_info(auth_token, namespace, body, **kwargs)  # noqa: E501
            return data

    def register_new_content_with_http_info(self, auth_token, namespace, body, **kwargs):  # noqa: E501
        """DefaultSourceContentResource - registerNewContent  # noqa: E501

        Set a content delivery entry for a set of content receivers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.register_new_content_with_http_info(auth_token, namespace, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param ContentRequest body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'namespace', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_new_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `register_new_content`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `register_new_content`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `register_new_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501
        if 'namespace' in params:
            header_params['namespace'] = params['namespace']  # noqa: E501

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
            '/api/source-engine/default/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_content(self, auth_token, namespace, server, body, **kwargs):  # noqa: E501
        """DefaultSourceContentResource - updateContent  # noqa: E501

        Update a content delivery entry for a set of content receivers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_content(auth_token, namespace, server, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str server: (required)
        :param ContentRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_content_with_http_info(auth_token, namespace, server, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_content_with_http_info(auth_token, namespace, server, body, **kwargs)  # noqa: E501
            return data

    def update_content_with_http_info(self, auth_token, namespace, server, body, **kwargs):  # noqa: E501
        """DefaultSourceContentResource - updateContent  # noqa: E501

        Update a content delivery entry for a set of content receivers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_content_with_http_info(auth_token, namespace, server, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str server: (required)
        :param ContentRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'namespace', 'server', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `update_content`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `update_content`")  # noqa: E501
        # verify the required parameter 'server' is set
        if ('server' not in params or
                params['server'] is None):
            raise ValueError("Missing the required parameter `server` when calling `update_content`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server' in params:
            query_params.append(('server', params['server']))  # noqa: E501

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501
        if 'namespace' in params:
            header_params['namespace'] = params['namespace']  # noqa: E501

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
            '/api/source-engine/default/register', 'PUT',
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

    def upload_file(self, auth_token, namespace, metadata, body, **kwargs):  # noqa: E501
        """DefaultSourceContentResource - uploadFile  # noqa: E501

        Uploads a file to the Ads on Top Content Network.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.upload_file(auth_token, namespace, metadata, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str metadata: (required)
        :param InputStream body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.upload_file_with_http_info(auth_token, namespace, metadata, body, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_file_with_http_info(auth_token, namespace, metadata, body, **kwargs)  # noqa: E501
            return data

    def upload_file_with_http_info(self, auth_token, namespace, metadata, body, **kwargs):  # noqa: E501
        """DefaultSourceContentResource - uploadFile  # noqa: E501

        Uploads a file to the Ads on Top Content Network.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.upload_file_with_http_info(auth_token, namespace, metadata, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str metadata: (required)
        :param InputStream body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'namespace', 'metadata', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `upload_file`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `upload_file`")  # noqa: E501
        # verify the required parameter 'metadata' is set
        if ('metadata' not in params or
                params['metadata'] is None):
            raise ValueError("Missing the required parameter `metadata` when calling `upload_file`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `upload_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'metadata' in params:
            query_params.append(('metadata', params['metadata']))  # noqa: E501

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-token'] = params['auth_token']  # noqa: E501
        if 'namespace' in params:
            header_params['namespace'] = params['namespace']  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/source-engine/default/register/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)