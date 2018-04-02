# swagger_client.AdSourceAdapterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pop**](AdSourceAdapterApi.md#pop) | **PUT** /api/source/engine/pop | AdSourceAdapterResource - pop
[**produce_ad**](AdSourceAdapterApi.md#produce_ad) | **POST** /api/source/engine/ad | AdSourceAdapterResource - produceAd


# **pop**
> pop(auth_token, namespace, publisher_rid, body)

AdSourceAdapterResource - pop

POP to annotate the advertisement that is delivered.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdSourceAdapterApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
publisher_rid = 'publisher_rid_example' # str | 
body = swagger_client.PopRequest() # PopRequest | 

try:
    # AdSourceAdapterResource - pop
    api_instance.pop(auth_token, namespace, publisher_rid, body)
except ApiException as e:
    print("Exception when calling AdSourceAdapterApi->pop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **publisher_rid** | **str**|  | 
 **body** | [**PopRequest**](PopRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **produce_ad**
> Ad produce_ad(auth_token, namespace, ad_source_rid, body)

AdSourceAdapterResource - produceAd

Produces a ad if available against the given vector.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdSourceAdapterApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
ad_source_rid = 'ad_source_rid_example' # str | 
body = swagger_client.AdRequestVector() # AdRequestVector | 

try:
    # AdSourceAdapterResource - produceAd
    api_response = api_instance.produce_ad(auth_token, namespace, ad_source_rid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdSourceAdapterApi->produce_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **ad_source_rid** | **str**|  | 
 **body** | [**AdRequestVector**](AdRequestVector.md)|  | 

### Return type

[**Ad**](Ad.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

