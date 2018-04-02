# swagger_client.AdRankerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_probabilities**](AdRankerApi.md#attach_probabilities) | **POST** /ranker | AdConstraintResource - Apply Soft Constraints


# **attach_probabilities**
> list[AdWithProbability] attach_probabilities(auth_token, namespace, body)

AdConstraintResource - Apply Soft Constraints

Applies the soft constraints based on the vector and the Publisher settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdRankerApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
body = swagger_client.SoftConstraintRequest() # SoftConstraintRequest | 

try:
    # AdConstraintResource - Apply Soft Constraints
    api_response = api_instance.attach_probabilities(auth_token, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdRankerApi->attach_probabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **body** | [**SoftConstraintRequest**](SoftConstraintRequest.md)|  | 

### Return type

[**list[AdWithProbability]**](AdWithProbability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

