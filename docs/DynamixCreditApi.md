# swagger_client.DynamixCreditApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credits**](DynamixCreditApi.md#add_credits) | **POST** /api/credit/add | Add credits to a vault.
[**check_balance**](DynamixCreditApi.md#check_balance) | **GET** /api/credit/balance | Checks the balance of a given vault.


# **add_credits**
> add_credits(auth_token, namespace, server, body)

Add credits to a vault.

Any rid can be used as the vault key. Each Rid has its own vault.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamixCreditApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
server = 'server_example' # str | 
body = swagger_client.AotCreditGrant() # AotCreditGrant | 

try:
    # Add credits to a vault.
    api_instance.add_credits(auth_token, namespace, server, body)
except ApiException as e:
    print("Exception when calling DynamixCreditApi->add_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **server** | **str**|  | 
 **body** | [**AotCreditGrant**](AotCreditGrant.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_balance**
> AotCreditVault check_balance(auth_token, namespace, server)

Checks the balance of a given vault.

Any rid can be used as the vault key. Each Rid has its own vault.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamixCreditApi()
auth_token = 'auth_token_example' # str | 
namespace = 'namespace_example' # str | 
server = 'server_example' # str | 

try:
    # Checks the balance of a given vault.
    api_response = api_instance.check_balance(auth_token, namespace, server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamixCreditApi->check_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | 
 **namespace** | **str**|  | 
 **server** | **str**|  | 

### Return type

[**AotCreditVault**](AotCreditVault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

