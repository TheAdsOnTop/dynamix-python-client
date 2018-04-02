# swagger_client.DeliveryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_next_ad**](DeliveryApi.md#get_next_ad) | **GET** /api/delivery | Get next Ad
[**pop_ad**](DeliveryApi.md#pop_ad) | **POST** /api/delivery | Trigger Proof of Play on Ad


# **get_next_ad**
> ReleasedAd get_next_ad(auth_token, namespace, publisher_rid)

Get next Ad



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeliveryApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
publisher_rid = 'publisher_rid_example' # str | 

try:
    # Get next Ad
    api_response = api_instance.get_next_ad(auth_token, namespace, publisher_rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->get_next_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **publisher_rid** | **str**|  | 

### Return type

[**ReleasedAd**](ReleasedAd.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pop_ad**
> pop_ad(auth_token, namespace, publisher_rid, ad_rid, body)

Trigger Proof of Play on Ad



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeliveryApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
publisher_rid = 'publisher_rid_example' # str | 
ad_rid = 'ad_rid_example' # str | 
body = swagger_client.ImpressionsValidationData() # ImpressionsValidationData | 

try:
    # Trigger Proof of Play on Ad
    api_instance.pop_ad(auth_token, namespace, publisher_rid, ad_rid, body)
except ApiException as e:
    print("Exception when calling DeliveryApi->pop_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **publisher_rid** | **str**|  | 
 **ad_rid** | **str**|  | 
 **body** | [**ImpressionsValidationData**](ImpressionsValidationData.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

