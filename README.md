# swagger-client
Sign up for Dynamix & grab your token.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v0.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://theadsontop.com](http://theadsontop.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APITokenApi* | [**create_account**](docs/APITokenApi.md#create_account) | **POST** /api/token | Creates an Ads on Top Dynamix account
*AdConstraintApi* | [**get_constraints**](docs/AdConstraintApi.md#get_constraints) | **GET** /constraints | AdConstraintResource - GetVector
*AdRankerApi* | [**attach_probabilities**](docs/AdRankerApi.md#attach_probabilities) | **POST** /ranker | AdConstraintResource - Apply Soft Constraints
*AdSourceApi* | [**bulk_resolve_source**](docs/AdSourceApi.md#bulk_resolve_source) | **POST** /api/source/bulk/resolve | AdSourceResource - bulkResolveSources
*AdSourceApi* | [**delete_source**](docs/AdSourceApi.md#delete_source) | **DELETE** /api/source | AdSourceResource - deleteSource
*AdSourceApi* | [**get_all_authorized_sources**](docs/AdSourceApi.md#get_all_authorized_sources) | **POST** /api/source/all/auth | AdSourceResource - getAllAuthorizedSources
*AdSourceApi* | [**register_source**](docs/AdSourceApi.md#register_source) | **POST** /api/source | AdSourceResource - registerSource
*AdSourceApi* | [**update_source**](docs/AdSourceApi.md#update_source) | **PUT** /api/source | AdSourceResource - updateSource
*AdSourceAdapterApi* | [**pop**](docs/AdSourceAdapterApi.md#pop) | **PUT** /api/source/engine/pop | AdSourceAdapterResource - pop
*AdSourceAdapterApi* | [**produce_ad**](docs/AdSourceAdapterApi.md#produce_ad) | **POST** /api/source/engine/ad | AdSourceAdapterResource - produceAd
*CatalogApi* | [**create_catalog_item**](docs/CatalogApi.md#create_catalog_item) | **POST** /api/catalog/item | Create a catalog item
*CatalogApi* | [**delete_catalog_item**](docs/CatalogApi.md#delete_catalog_item) | **DELETE** /api/catalog/item | Delete a Catalog entry
*CatalogApi* | [**get_catalog_item**](docs/CatalogApi.md#get_catalog_item) | **GET** /api/catalog/item | Get a single Catalog Item
*CatalogApi* | [**get_catalog_items**](docs/CatalogApi.md#get_catalog_items) | **PUT** /api/catalog/item/bulk/get | Get Catalog Items Paged
*CatalogApi* | [**list_catalog**](docs/CatalogApi.md#list_catalog) | **PUT** /api/catalog/list/search | List the Catalog entries
*CatalogApi* | [**list_catalog_0**](docs/CatalogApi.md#list_catalog_0) | **PUT** /api/catalog/list/type | List the Catalog entries
*CatalogApi* | [**update_catalog_item**](docs/CatalogApi.md#update_catalog_item) | **PUT** /api/catalog/item | Update a Catalog entry
*DefaultSourceContentApi* | [**delete_content**](docs/DefaultSourceContentApi.md#delete_content) | **DELETE** /api/source-engine/default/register | DefaultSourceContentResource - deleteContent
*DefaultSourceContentApi* | [**get_all_authorized_content_paged**](docs/DefaultSourceContentApi.md#get_all_authorized_content_paged) | **POST** /api/source-engine/default/register/paged | 
*DefaultSourceContentApi* | [**get_content_request**](docs/DefaultSourceContentApi.md#get_content_request) | **GET** /api/source-engine/default/register | 
*DefaultSourceContentApi* | [**register_new_content**](docs/DefaultSourceContentApi.md#register_new_content) | **POST** /api/source-engine/default/register | DefaultSourceContentResource - registerNewContent
*DefaultSourceContentApi* | [**update_content**](docs/DefaultSourceContentApi.md#update_content) | **PUT** /api/source-engine/default/register | DefaultSourceContentResource - updateContent
*DefaultSourceContentApi* | [**upload_file**](docs/DefaultSourceContentApi.md#upload_file) | **POST** /api/source-engine/default/register/upload | DefaultSourceContentResource - uploadFile
*DeliveryApi* | [**get_next_ad**](docs/DeliveryApi.md#get_next_ad) | **GET** /api/delivery | Get next Ad
*DeliveryApi* | [**pop_ad**](docs/DeliveryApi.md#pop_ad) | **POST** /api/delivery | Trigger Proof of Play on Ad
*DynamixCreditApi* | [**add_credits**](docs/DynamixCreditApi.md#add_credits) | **POST** /api/credit/add | Add credits to a vault.
*DynamixCreditApi* | [**check_balance**](docs/DynamixCreditApi.md#check_balance) | **GET** /api/credit/balance | Checks the balance of a given vault.
*PublisherApi* | [**bulk_resolve_publishers**](docs/PublisherApi.md#bulk_resolve_publishers) | **POST** /api/publisher/bulk/resolve | PublisherResource - bulkResolvePublishers
*PublisherApi* | [**delete_publisher**](docs/PublisherApi.md#delete_publisher) | **DELETE** /api/publisher | PublisherResource - deletePublisher
*PublisherApi* | [**get_all_authorized_publishers**](docs/PublisherApi.md#get_all_authorized_publishers) | **POST** /api/publisher/authorized | PublisherResource - getAllAuthorizedPublishers
*PublisherApi* | [**register_publisher**](docs/PublisherApi.md#register_publisher) | **POST** /api/publisher | PublisherResource - registerPublisher
*PublisherApi* | [**update_publisher**](docs/PublisherApi.md#update_publisher) | **PUT** /api/publisher | PublisherResource - updatePublisher


## Documentation For Models

 - [AccountRegistrationRequest](docs/AccountRegistrationRequest.md)
 - [Ad](docs/Ad.md)
 - [AdMetadata](docs/AdMetadata.md)
 - [AdRequestVector](docs/AdRequestVector.md)
 - [AdRequestWeights](docs/AdRequestWeights.md)
 - [AdResolutionInfo](docs/AdResolutionInfo.md)
 - [AdRestrictions](docs/AdRestrictions.md)
 - [AdSourceRestriction](docs/AdSourceRestriction.md)
 - [AdWithProbability](docs/AdWithProbability.md)
 - [Address](docs/Address.md)
 - [AotCreditCharge](docs/AotCreditCharge.md)
 - [AotCreditGrant](docs/AotCreditGrant.md)
 - [AotCreditVault](docs/AotCreditVault.md)
 - [AotFile](docs/AotFile.md)
 - [AspectRatio](docs/AspectRatio.md)
 - [BearerToken](docs/BearerToken.md)
 - [CatalogItem](docs/CatalogItem.md)
 - [CatalogItemPagedRequest](docs/CatalogItemPagedRequest.md)
 - [ContentRequest](docs/ContentRequest.md)
 - [Currency](docs/Currency.md)
 - [DateBoundedTimeRange](docs/DateBoundedTimeRange.md)
 - [DayBoundedTimeRange](docs/DayBoundedTimeRange.md)
 - [DemographicVector](docs/DemographicVector.md)
 - [EnabledAdSource](docs/EnabledAdSource.md)
 - [FileMetadata](docs/FileMetadata.md)
 - [ImpressionInfo](docs/ImpressionInfo.md)
 - [ImpressionsValidationData](docs/ImpressionsValidationData.md)
 - [InputStream](docs/InputStream.md)
 - [KeyedAd](docs/KeyedAd.md)
 - [KeyedItem](docs/KeyedItem.md)
 - [KeyedItemObject](docs/KeyedItemObject.md)
 - [MonetaryRequirementInfo](docs/MonetaryRequirementInfo.md)
 - [ObjectNode](docs/ObjectNode.md)
 - [PagedRequest](docs/PagedRequest.md)
 - [PagedResponse](docs/PagedResponse.md)
 - [PagedResponseContentRequest](docs/PagedResponseContentRequest.md)
 - [PagedResponsePublisher](docs/PagedResponsePublisher.md)
 - [PagedSearchQuery](docs/PagedSearchQuery.md)
 - [PopRequest](docs/PopRequest.md)
 - [Publisher](docs/Publisher.md)
 - [PublisherHistoryInfo](docs/PublisherHistoryInfo.md)
 - [PublisherLocationInfo](docs/PublisherLocationInfo.md)
 - [ReleasedAd](docs/ReleasedAd.md)
 - [Resolution](docs/Resolution.md)
 - [ResourceIdentifier](docs/ResourceIdentifier.md)
 - [ScreenDimensions](docs/ScreenDimensions.md)
 - [SoftConstraintRequest](docs/SoftConstraintRequest.md)
 - [TimeInfo](docs/TimeInfo.md)
 - [TimeRange](docs/TimeRange.md)
 - [User](docs/User.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

david@theadsontop.com

