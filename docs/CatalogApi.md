# swagger_client.CatalogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_catalog_item**](CatalogApi.md#create_catalog_item) | **POST** /api/catalog/item | Create a catalog item
[**delete_catalog_item**](CatalogApi.md#delete_catalog_item) | **DELETE** /api/catalog/item | Delete a Catalog entry
[**get_catalog_item**](CatalogApi.md#get_catalog_item) | **GET** /api/catalog/item | Get a single Catalog Item
[**get_catalog_items**](CatalogApi.md#get_catalog_items) | **PUT** /api/catalog/item/bulk/get | Get Catalog Items Paged
[**list_catalog**](CatalogApi.md#list_catalog) | **PUT** /api/catalog/list/search | List the Catalog entries
[**list_catalog_0**](CatalogApi.md#list_catalog_0) | **PUT** /api/catalog/list/type | List the Catalog entries
[**update_catalog_item**](CatalogApi.md#update_catalog_item) | **PUT** /api/catalog/item | Update a Catalog entry


# **create_catalog_item**
> CatalogItem create_catalog_item(auth_token, body)

Create a catalog item



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
auth_token = 'auth_token_example' # str | 
body = swagger_client.CatalogItem() # CatalogItem | 

try:
    # Create a catalog item
    api_response = api_instance.create_catalog_item(auth_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->create_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **body** | [**CatalogItem**](CatalogItem.md)|  | 

### Return type

[**CatalogItem**](CatalogItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_catalog_item**
> delete_catalog_item(auth_token, item_rid)

Delete a Catalog entry



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
auth_token = 'auth_token_example' # str | 
item_rid = 'item_rid_example' # str | 

try:
    # Delete a Catalog entry
    api_instance.delete_catalog_item(auth_token, item_rid)
except ApiException as e:
    print("Exception when calling CatalogApi->delete_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **item_rid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_item**
> CatalogItem get_catalog_item(auth_token, item_rid)

Get a single Catalog Item



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
auth_token = 'auth_token_example' # str | 
item_rid = 'item_rid_example' # str | 

try:
    # Get a single Catalog Item
    api_response = api_instance.get_catalog_item(auth_token, item_rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **item_rid** | **str**|  | 

### Return type

[**CatalogItem**](CatalogItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_items**
> list[CatalogItem] get_catalog_items(auth_token, body)

Get Catalog Items Paged



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
auth_token = 'auth_token_example' # str | 
body = swagger_client.CatalogItemPagedRequest() # CatalogItemPagedRequest | 

try:
    # Get Catalog Items Paged
    api_response = api_instance.get_catalog_items(auth_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **body** | [**CatalogItemPagedRequest**](CatalogItemPagedRequest.md)|  | 

### Return type

[**list[CatalogItem]**](CatalogItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_catalog**
> PagedResponse list_catalog(auth_token, body)

List the Catalog entries



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
auth_token = 'auth_token_example' # str | 
body = swagger_client.PagedSearchQuery() # PagedSearchQuery | 

try:
    # List the Catalog entries
    api_response = api_instance.list_catalog(auth_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->list_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **body** | [**PagedSearchQuery**](PagedSearchQuery.md)|  | 

### Return type

[**PagedResponse**](PagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_catalog_0**
> PagedResponse list_catalog_0(auth_token, type, body)

List the Catalog entries



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
auth_token = 'auth_token_example' # str | 
type = 'type_example' # str | 
body = swagger_client.PagedRequest() # PagedRequest | 

try:
    # List the Catalog entries
    api_response = api_instance.list_catalog_0(auth_token, type, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->list_catalog_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **type** | **str**|  | 
 **body** | [**PagedRequest**](PagedRequest.md)|  | 

### Return type

[**PagedResponse**](PagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_item**
> update_catalog_item(auth_token, item_rid, body)

Update a Catalog entry



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogApi()
auth_token = 'auth_token_example' # str | 
item_rid = 'item_rid_example' # str | 
body = swagger_client.CatalogItem() # CatalogItem | 

try:
    # Update a Catalog entry
    api_instance.update_catalog_item(auth_token, item_rid, body)
except ApiException as e:
    print("Exception when calling CatalogApi->update_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **item_rid** | **str**|  | 
 **body** | [**CatalogItem**](CatalogItem.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

