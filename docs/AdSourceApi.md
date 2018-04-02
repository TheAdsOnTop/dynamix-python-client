# swagger_client.AdSourceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_resolve_source**](AdSourceApi.md#bulk_resolve_source) | **POST** /api/source/bulk/resolve | AdSourceResource - bulkResolveSources
[**delete_source**](AdSourceApi.md#delete_source) | **DELETE** /api/source | AdSourceResource - deleteSource
[**get_all_authorized_sources**](AdSourceApi.md#get_all_authorized_sources) | **POST** /api/source/all/auth | AdSourceResource - getAllAuthorizedSources
[**register_source**](AdSourceApi.md#register_source) | **POST** /api/source | AdSourceResource - registerSource
[**update_source**](AdSourceApi.md#update_source) | **PUT** /api/source | AdSourceResource - updateSource


# **bulk_resolve_source**
> list[EnabledAdSource] bulk_resolve_source(auth_token, namespace, body)

AdSourceResource - bulkResolveSources

Resolves a bunch of rids into EnabledAdSource objects.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdSourceApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = [swagger_client.list[str]()] # list[str] | 

try:
    # AdSourceResource - bulkResolveSources
    api_response = api_instance.bulk_resolve_source(auth_token, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdSourceApi->bulk_resolve_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | **list[str]**|  | 

### Return type

[**list[EnabledAdSource]**](EnabledAdSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source**
> delete_source(auth_token, namespace, ad_source_rid)

AdSourceResource - deleteSource

Delete a source stored at the rid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdSourceApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
ad_source_rid = 'ad_source_rid_example' # str | 

try:
    # AdSourceResource - deleteSource
    api_instance.delete_source(auth_token, namespace, ad_source_rid)
except ApiException as e:
    print("Exception when calling AdSourceApi->delete_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **ad_source_rid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_authorized_sources**
> PagedResponse get_all_authorized_sources(auth_token, namespace, body)

AdSourceResource - getAllAuthorizedSources

Grab all ad sources that this token is authorized for.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdSourceApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = swagger_client.PagedRequest() # PagedRequest | 

try:
    # AdSourceResource - getAllAuthorizedSources
    api_response = api_instance.get_all_authorized_sources(auth_token, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdSourceApi->get_all_authorized_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | [**PagedRequest**](PagedRequest.md)|  | 

### Return type

[**PagedResponse**](PagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_source**
> str register_source(auth_token, namespace, body)

AdSourceResource - registerSource

Registers a source for content creation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdSourceApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = swagger_client.EnabledAdSource() # EnabledAdSource | 

try:
    # AdSourceResource - registerSource
    api_response = api_instance.register_source(auth_token, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdSourceApi->register_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | [**EnabledAdSource**](EnabledAdSource.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source**
> update_source(auth_token, namespace, ad_source_rid, body)

AdSourceResource - updateSource

Update the source registered at the rid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdSourceApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
ad_source_rid = 'ad_source_rid_example' # str | 
body = swagger_client.EnabledAdSource() # EnabledAdSource | 

try:
    # AdSourceResource - updateSource
    api_instance.update_source(auth_token, namespace, ad_source_rid, body)
except ApiException as e:
    print("Exception when calling AdSourceApi->update_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **ad_source_rid** | **str**|  | 
 **body** | [**EnabledAdSource**](EnabledAdSource.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

