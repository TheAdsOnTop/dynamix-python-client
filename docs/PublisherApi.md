# swagger_client.PublisherApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_resolve_publishers**](PublisherApi.md#bulk_resolve_publishers) | **POST** /api/publisher/bulk/resolve | PublisherResource - bulkResolvePublishers
[**delete_publisher**](PublisherApi.md#delete_publisher) | **DELETE** /api/publisher | PublisherResource - deletePublisher
[**get_all_authorized_publishers**](PublisherApi.md#get_all_authorized_publishers) | **POST** /api/publisher/authorized | PublisherResource - getAllAuthorizedPublishers
[**register_publisher**](PublisherApi.md#register_publisher) | **POST** /api/publisher | PublisherResource - registerPublisher
[**update_publisher**](PublisherApi.md#update_publisher) | **PUT** /api/publisher | PublisherResource - updatePublisher


# **bulk_resolve_publishers**
> list[Publisher] bulk_resolve_publishers(auth_token, namespace, body=body)

PublisherResource - bulkResolvePublishers

Grab a set of publishers by RID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublisherApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = [swagger_client.list[str]()] # list[str] |  (optional)

try:
    # PublisherResource - bulkResolvePublishers
    api_response = api_instance.bulk_resolve_publishers(auth_token, namespace, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublisherApi->bulk_resolve_publishers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | **list[str]**|  | [optional] 

### Return type

[**list[Publisher]**](Publisher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_publisher**
> delete_publisher(auth_token, namespace, server)

PublisherResource - deletePublisher

Deletes a publisher from the database.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublisherApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
server = 'server_example' # str | 

try:
    # PublisherResource - deletePublisher
    api_instance.delete_publisher(auth_token, namespace, server)
except ApiException as e:
    print("Exception when calling PublisherApi->delete_publisher: %s\n" % e)
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

# **get_all_authorized_publishers**
> PagedResponsePublisher get_all_authorized_publishers(auth_token, namespace, body)

PublisherResource - getAllAuthorizedPublishers

Grab all the publishers that the token is authorized for. Requires paging.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublisherApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = swagger_client.PagedRequest() # PagedRequest | 

try:
    # PublisherResource - getAllAuthorizedPublishers
    api_response = api_instance.get_all_authorized_publishers(auth_token, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublisherApi->get_all_authorized_publishers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | [**PagedRequest**](PagedRequest.md)|  | 

### Return type

[**PagedResponsePublisher**](PagedResponsePublisher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_publisher**
> str register_publisher(auth_token, namespace, body)

PublisherResource - registerPublisher

Registers a content consumer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublisherApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = swagger_client.Publisher() # Publisher | 

try:
    # PublisherResource - registerPublisher
    api_response = api_instance.register_publisher(auth_token, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublisherApi->register_publisher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | [**Publisher**](Publisher.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_publisher**
> update_publisher(auth_token, namespace, server, body)

PublisherResource - updatePublisher

Updates the publisher with the provided value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublisherApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
server = 'server_example' # str | 
body = swagger_client.Publisher() # Publisher | 

try:
    # PublisherResource - updatePublisher
    api_instance.update_publisher(auth_token, namespace, server, body)
except ApiException as e:
    print("Exception when calling PublisherApi->update_publisher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **server** | **str**|  | 
 **body** | [**Publisher**](Publisher.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

