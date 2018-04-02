# swagger_client.APITokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](APITokenApi.md#create_account) | **POST** /api/token | Creates an Ads on Top Dynamix account


# **create_account**
> str create_account(namespace, body)

Creates an Ads on Top Dynamix account

Each namespace is its own data sandbox.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APITokenApi()
namespace = 'namespace_example' # str | 
body = swagger_client.AccountRegistrationRequest() # AccountRegistrationRequest | 

try:
    # Creates an Ads on Top Dynamix account
    api_response = api_instance.create_account(namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APITokenApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | [**AccountRegistrationRequest**](AccountRegistrationRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

