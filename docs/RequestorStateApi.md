# ya_activity.RequestorStateApi

All URIs are relative to *http://localhost/activity-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity_state**](RequestorStateApi.md#get_activity_state) | **GET** /activity/{activityId}/state | Get state of specified Activity.
[**get_activity_usage**](RequestorStateApi.md#get_activity_usage) | **GET** /activity/{activityId}/usage | Get usage of specified Activity.
[**get_running_command**](RequestorStateApi.md#get_running_command) | **GET** /activity/{activityId}/command | Get running command for a specified Activity.


# **get_activity_state**
> ActivityState get_activity_state(activity_id)

Get state of specified Activity.

### Example

* Bearer Authentication (app_key):
```python
from __future__ import print_function
import time
import ya_activity
from ya_activity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/activity-api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ya_activity.Configuration(
    host = "http://localhost/activity-api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: app_key
configuration = ya_activity.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ya_activity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ya_activity.RequestorStateApi(api_client)
    activity_id = 'activity_id_example' # str | 

    try:
        # Get state of specified Activity.
        api_response = api_instance.get_activity_state(activity_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RequestorStateApi->get_activity_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  | 

### Return type

[**ActivityState**](ActivityState.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_usage**
> list[float] get_activity_usage(activity_id)

Get usage of specified Activity.

### Example

* Bearer Authentication (app_key):
```python
from __future__ import print_function
import time
import ya_activity
from ya_activity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/activity-api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ya_activity.Configuration(
    host = "http://localhost/activity-api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: app_key
configuration = ya_activity.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ya_activity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ya_activity.RequestorStateApi(api_client)
    activity_id = 'activity_id_example' # str | 

    try:
        # Get usage of specified Activity.
        api_response = api_instance.get_activity_usage(activity_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RequestorStateApi->get_activity_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  | 

### Return type

**list[float]**

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_command**
> ExeScriptCommandState get_running_command(activity_id)

Get running command for a specified Activity.

**Note:** This call shall get routed directly to ExeUnit.

### Example

* Bearer Authentication (app_key):
```python
from __future__ import print_function
import time
import ya_activity
from ya_activity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/activity-api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ya_activity.Configuration(
    host = "http://localhost/activity-api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: app_key
configuration = ya_activity.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ya_activity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ya_activity.RequestorStateApi(api_client)
    activity_id = 'activity_id_example' # str | 

    try:
        # Get running command for a specified Activity.
        api_response = api_instance.get_running_command(activity_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RequestorStateApi->get_running_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**|  | 

### Return type

[**ExeScriptCommandState**](ExeScriptCommandState.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

