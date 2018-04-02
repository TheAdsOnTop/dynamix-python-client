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


class AdSourceAdapterApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pop(self, auth_token, namespace, publisher_rid, body, **kwargs):  # noqa: E501
        """AdSourceAdapterResource - pop  # noqa: E501

        POP to annotate the advertisement that is delivered.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.pop(auth_token, namespace, publisher_rid, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str publisher_rid: (required)
        :param PopRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.pop_with_http_info(auth_token, namespace, publisher_rid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.pop_with_http_info(auth_token, namespace, publisher_rid, body, **kwargs)  # noqa: E501
            return data

    def pop_with_http_info(self, auth_token, namespace, publisher_rid, body, **kwargs):  # noqa: E501
        """AdSourceAdapterResource - pop  # noqa: E501

        POP to annotate the advertisement that is delivered.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.pop_with_http_info(auth_token, namespace, publisher_rid, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str publisher_rid: (required)
        :param PopRequest body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'namespace', 'publisher_rid', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pop" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `pop`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `pop`")  # noqa: E501
        # verify the required parameter 'publisher_rid' is set
        if ('publisher_rid' not in params or
                params['publisher_rid'] is None):
            raise ValueError("Missing the required parameter `publisher_rid` when calling `pop`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `pop`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publisher_rid' in params:
            query_params.append(('publisherRid', params['publisher_rid']))  # noqa: E501

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
            '/api/source/engine/pop', 'PUT',
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

    def produce_ad(self, auth_token, namespace, ad_source_rid, body, **kwargs):  # noqa: E501
        """AdSourceAdapterResource - produceAd  # noqa: E501

        Produces a ad if available against the given vector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.produce_ad(auth_token, namespace, ad_source_rid, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str ad_source_rid: (required)
        :param AdRequestVector body: (required)
        :return: Ad
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.produce_ad_with_http_info(auth_token, namespace, ad_source_rid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.produce_ad_with_http_info(auth_token, namespace, ad_source_rid, body, **kwargs)  # noqa: E501
            return data

    def produce_ad_with_http_info(self, auth_token, namespace, ad_source_rid, body, **kwargs):  # noqa: E501
        """AdSourceAdapterResource - produceAd  # noqa: E501

        Produces a ad if available against the given vector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.produce_ad_with_http_info(auth_token, namespace, ad_source_rid, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auth_token: (required)
        :param str namespace: (required)
        :param str ad_source_rid: (required)
        :param AdRequestVector body: (required)
        :return: Ad
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_token', 'namespace', 'ad_source_rid', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method produce_ad" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_token' is set
        if ('auth_token' not in params or
                params['auth_token'] is None):
            raise ValueError("Missing the required parameter `auth_token` when calling `produce_ad`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `produce_ad`")  # noqa: E501
        # verify the required parameter 'ad_source_rid' is set
        if ('ad_source_rid' not in params or
                params['ad_source_rid'] is None):
            raise ValueError("Missing the required parameter `ad_source_rid` when calling `produce_ad`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `produce_ad`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ad_source_rid' in params:
            query_params.append(('adSourceRid', params['ad_source_rid']))  # noqa: E501

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
            '/api/source/engine/ad', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Ad',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
