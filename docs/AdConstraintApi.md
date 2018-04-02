# swagger_client.AdConstraintApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_constraints**](AdConstraintApi.md#get_constraints) | **GET** /constraints | AdConstraintResource - GetVector


# **get_constraints**
> AdRequestVector get_constraints(auth_token, namespace, publisher_rid, publisher)

AdConstraintResource - GetVector

Produces the ad request vector with all the constraints provided by the engine and publisher.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdConstraintApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
publisher_rid = 'publisher_rid_example' # str | 
publisher = 'publisher_example' # str | 

try:
    # AdConstraintResource - GetVector
    api_response = api_instance.get_constraints(auth_token, namespace, publisher_rid, publisher)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdConstraintApi->get_constraints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **publisher_rid** | **str**|  | 
 **publisher** | **str**|  | 

### Return type

[**AdRequestVector**](AdRequestVector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

