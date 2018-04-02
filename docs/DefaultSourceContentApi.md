# swagger_client.DefaultSourceContentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_content**](DefaultSourceContentApi.md#delete_content) | **DELETE** /api/source-engine/default/register | DefaultSourceContentResource - deleteContent
[**get_all_authorized_content_paged**](DefaultSourceContentApi.md#get_all_authorized_content_paged) | **POST** /api/source-engine/default/register/paged | 
[**get_content_request**](DefaultSourceContentApi.md#get_content_request) | **GET** /api/source-engine/default/register | 
[**register_new_content**](DefaultSourceContentApi.md#register_new_content) | **POST** /api/source-engine/default/register | DefaultSourceContentResource - registerNewContent
[**update_content**](DefaultSourceContentApi.md#update_content) | **PUT** /api/source-engine/default/register | DefaultSourceContentResource - updateContent
[**upload_file**](DefaultSourceContentApi.md#upload_file) | **POST** /api/source-engine/default/register/upload | DefaultSourceContentResource - uploadFile


# **delete_content**
> delete_content(auth_token, namespace, server)

DefaultSourceContentResource - deleteContent

Delete a content delivery entry.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultSourceContentApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
server = 'server_example' # str | 

try:
    # DefaultSourceContentResource - deleteContent
    api_instance.delete_content(auth_token, namespace, server)
except ApiException as e:
    print("Exception when calling DefaultSourceContentApi->delete_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **server** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_authorized_content_paged**
> PagedResponseContentRequest get_all_authorized_content_paged(auth_token, namespace, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultSourceContentApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = swagger_client.PagedRequest() # PagedRequest | 

try:
    api_response = api_instance.get_all_authorized_content_paged(auth_token, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultSourceContentApi->get_all_authorized_content_paged: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | [**PagedRequest**](PagedRequest.md)|  | 

### Return type

[**PagedResponseContentRequest**](PagedResponseContentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_request**
> ContentRequest get_content_request(auth_token, namespace, server)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultSourceContentApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
server = 'server_example' # str | 

try:
    api_response = api_instance.get_content_request(auth_token, namespace, server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultSourceContentApi->get_content_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **server** | **str**|  | 

### Return type

[**ContentRequest**](ContentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_new_content**
> str register_new_content(auth_token, namespace, body)

DefaultSourceContentResource - registerNewContent

Set a content delivery entry for a set of content receivers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultSourceContentApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = swagger_client.ContentRequest() # ContentRequest | 

try:
    # DefaultSourceContentResource - registerNewContent
    api_response = api_instance.register_new_content(auth_token, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultSourceContentApi->register_new_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | [**ContentRequest**](ContentRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content**
> update_content(auth_token, namespace, server, body)

DefaultSourceContentResource - updateContent

Update a content delivery entry for a set of content receivers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultSourceContentApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
server = 'server_example' # str | 
body = swagger_client.ContentRequest() # ContentRequest | 

try:
    # DefaultSourceContentResource - updateContent
    api_instance.update_content(auth_token, namespace, server, body)
except ApiException as e:
    print("Exception when calling DefaultSourceContentApi->update_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **server** | **str**|  | 
 **body** | [**ContentRequest**](ContentRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> str upload_file(auth_token, namespace, metadata, body)

DefaultSourceContentResource - uploadFile

Uploads a file to the Ads on Top Content Network.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultSourceContentApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
metadata = 'metadata_example' # str | 
body = swagger_client.InputStream() # InputStream | 

try:
    # DefaultSourceContentResource - uploadFile
    api_response = api_instance.upload_file(auth_token, namespace, metadata, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultSourceContentApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **metadata** | **str**|  | 
 **body** | [**InputStream**](InputStream.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

