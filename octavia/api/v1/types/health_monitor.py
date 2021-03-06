#    Copyright 2014 Rackspace
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from wsme import types as wtypes

from octavia.api.common import types as base
from octavia.common import constants


class HealthMonitorResponse(base.BaseType):
    """Defines which attributes are to be shown on any response."""
    type = wtypes.wsattr(wtypes.text)
    delay = wtypes.wsattr(wtypes.IntegerType())
    timeout = wtypes.wsattr(wtypes.IntegerType())
    fall_threshold = wtypes.wsattr(wtypes.IntegerType())
    rise_threshold = wtypes.wsattr(wtypes.IntegerType())
    http_method = wtypes.wsattr(wtypes.text)
    url_path = wtypes.wsattr(wtypes.text)
    expected_codes = wtypes.wsattr(wtypes.text)
    enabled = wtypes.wsattr(bool)
    project_id = wtypes.wsattr(wtypes.StringType())


class HealthMonitorPOST(base.BaseType):
    """Defines mandatory and optional attributes of a POST request."""
    type = wtypes.wsattr(
        wtypes.Enum(str, *constants.SUPPORTED_HEALTH_MONITOR_TYPES),
        mandatory=True)
    delay = wtypes.wsattr(wtypes.IntegerType(), mandatory=True)
    timeout = wtypes.wsattr(wtypes.IntegerType(), mandatory=True)
    fall_threshold = wtypes.wsattr(wtypes.IntegerType(), mandatory=True)
    rise_threshold = wtypes.wsattr(wtypes.IntegerType(), mandatory=True)
    http_method = wtypes.wsattr(
        wtypes.text, default=constants.HEALTH_MONITOR_HTTP_DEFAULT_METHOD)
    url_path = wtypes.wsattr(
        wtypes.text, default=constants.HEALTH_MONITOR_DEFAULT_URL_PATH)
    expected_codes = wtypes.wsattr(
        wtypes.text, default=constants.HEALTH_MONITOR_DEFAULT_EXPECTED_CODES)
    enabled = wtypes.wsattr(bool, default=True)
    # TODO(johnsom) Remove after deprecation (R series)
    project_id = wtypes.wsattr(wtypes.StringType(max_length=36))


class HealthMonitorPUT(base.BaseType):
    """Defines attributes that are acceptable of a PUT request."""
    type = wtypes.wsattr(
        wtypes.Enum(str, *constants.SUPPORTED_HEALTH_MONITOR_TYPES))
    delay = wtypes.wsattr(wtypes.IntegerType())
    timeout = wtypes.wsattr(wtypes.IntegerType())
    fall_threshold = wtypes.wsattr(wtypes.IntegerType())
    rise_threshold = wtypes.wsattr(wtypes.IntegerType())
    http_method = wtypes.wsattr(wtypes.text)
    url_path = wtypes.wsattr(wtypes.text)
    expected_codes = wtypes.wsattr(wtypes.text)
    enabled = wtypes.wsattr(bool)
