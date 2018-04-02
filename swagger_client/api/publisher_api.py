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


class PublisherApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bulk_resolve_publishers(self, auth_token, namespace, **kwargs):  # noqa: E501
        """PublisherResource - bulkResolvePublishers  # noqa: E501

        Grab a set of publishers by RID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bulk_resolve_publishers(auth_token, namespace, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param list[str] body:
        :return: list[Publisher]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.bulk_resolve_publishers_with_http_info(auth_token, namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_resolve_publishers_with_http_info(auth_token, namespace, **kwargs)  # noqa: E501
            return data

    def bulk_resolve_publishers_with_http_info(self, auth_token, namespace, **kwargs):  # noqa: E501
        """PublisherResource - bulkResolvePublishers  # noqa: E501

        Grab a set of publishers by RID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bulk_resolve_publishers_with_http_info(auth_token, namespace, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param list[str] body:
        :return: list[Publisher]
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
                    " to method bulk_resolve_publishers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `bulk_resolve_publishers`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `bulk_resolve_publishers`")  # noqa: E501

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
            '/api/publisher/bulk/resolve', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Publisher]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_publisher(self, auth_token, namespace, server, **kwargs):  # noqa: E501
        """PublisherResource - deletePublisher  # noqa: E501

        Deletes a publisher from the database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_publisher(auth_token, namespace, server, async=True)
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
            return self.delete_publisher_with_http_info(auth_token, namespace, server, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_publisher_with_http_info(auth_token, namespace, server, **kwargs)  # noqa: E501
            return data

    def delete_publisher_with_http_info(self, auth_token, namespace, server, **kwargs):  # noqa: E501
        """PublisherResource - deletePublisher  # noqa: E501

        Deletes a publisher from the database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_publisher_with_http_info(auth_token, namespace, server, async=True)
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
                    " to method delete_publisher" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `delete_publisher`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `delete_publisher`")  # noqa: E501
        # verify the required parameter 'server' is set
        if ('server' not in params or
                params['server'] is None):
            raise ValueError("Missing the required parameter `server` when calling `delete_publisher`")  # noqa: E501

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
            '/api/publisher', 'DELETE',
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

    def get_all_authorized_publishers(self, auth_token, namespace, body, **kwargs):  # noqa: E501
        """PublisherResource - getAllAuthorizedPublishers  # noqa: E501

        Grab all the publishers that the token is authorized for. Requires paging.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_authorized_publishers(auth_token, namespace, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param PagedRequest body: (required)
        :return: PagedResponsePublisher
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_authorized_publishers_with_http_info(auth_token, namespace, body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_authorized_publishers_with_http_info(auth_token, namespace, body, **kwargs)  # noqa: E501
            return data

    def get_all_authorized_publishers_with_http_info(self, auth_token, namespace, body, **kwargs):  # noqa: E501
        """PublisherResource - getAllAuthorizedPublishers  # noqa: E501

        Grab all the publishers that the token is authorized for. Requires paging.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_authorized_publishers_with_http_info(auth_token, namespace, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param PagedRequest body: (required)
        :return: PagedResponsePublisher
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
                    " to method get_all_authorized_publishers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `get_all_authorized_publishers`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `get_all_authorized_publishers`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_all_authorized_publishers`")  # noqa: E501

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
            '/api/publisher/authorized', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResponsePublisher',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_publisher(self, auth_token, namespace, body, **kwargs):  # noqa: E501
        """PublisherResource - registerPublisher  # noqa: E501

        Registers a content consumer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.register_publisher(auth_token, namespace, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param Publisher body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.register_publisher_with_http_info(auth_token, namespace, body, **kwargs)  # noqa: E501
        else:
            (data) = self.register_publisher_with_http_info(auth_token, namespace, body, **kwargs)  # noqa: E501
            return data

    def register_publisher_with_http_info(self, auth_token, namespace, body, **kwargs):  # noqa: E501
        """PublisherResource - registerPublisher  # noqa: E501

        Registers a content consumer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.register_publisher_with_http_info(auth_token, namespace, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param Publisher body: (required)
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
                    " to method register_publisher" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `register_publisher`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `register_publisher`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `register_publisher`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_token' in params:
            header_params['Auth-Token'] = params['auth_token']  # noqa: E501
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
            '/api/publisher', 'POST',
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

    def update_publisher(self, auth_token, namespace, server, body, **kwargs):  # noqa: E501
        """PublisherResource - updatePublisher  # noqa: E501

        Updates the publisher with the provided value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_publisher(auth_token, namespace, server, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str server: (required)
        :param Publisher body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_publisher_with_http_info(auth_token, namespace, server, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_publisher_with_http_info(auth_token, namespace, server, body, **kwargs)  # noqa: E501
            return data

    def update_publisher_with_http_info(self, auth_token, namespace, server, body, **kwargs):  # noqa: E501
        """PublisherResource - updatePublisher  # noqa: E501

        Updates the publisher with the provided value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_publisher_with_http_info(auth_token, namespace, server, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str server: (required)
        :param Publisher body: (required)
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
                    " to method update_publisher" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `update_publisher`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `update_publisher`")  # noqa: E501
        # verify the required parameter 'server' is set
        if ('server' not in params or
                params['server'] is None):
            raise ValueError("Missing the required parameter `server` when calling `update_publisher`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_publisher`")  # noqa: E501

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
            '/api/publisher', 'PUT',
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
