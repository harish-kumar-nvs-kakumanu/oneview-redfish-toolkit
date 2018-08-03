# -*- coding: utf-8 -*-

# Copyright (2017) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

STATUS_MAP = {
    "OK": {
        "State": "Enabled",
        "Health": "OK"
    },
    "Disabled": {
        "State": "Disabled",
        "Health": "Warning"
    },
    "Warning": {
        "State": "Enabled",
        "Health": "Warning"
    },
    "Critical": {
        "State": "Enabled",
        "Health": "Critical"
    },
    "Unknown": {
        "State": "Absent",
        "Health": None
    }
}

HEALTH_STATUS_MAPPING = {
    "Critical": "Critical",
    "OK": "OK",
    "Unknown": "Warning",
    "Disabled": "Warning",
    "Warning": "Warning",
}

COMPOSITION_STATE_MAPPING = {
    "NoProfileApplied": "Unused",
    "ApplyingProfile": "Composing",
    "ProfileApplied": "Composed",
    "ProfileError": "Failed"
}

COMPUTER_SYSTEM_STATE_MAPPING = {
    "NoProfileApplied": "Enabled",
    "Monitored": "Enabled",
    "ProfileApplied": "Enabled",
    "Unsupported": "UnavailableOffline",
    "Unknown": "Absent",
    "RemoveFailed": "StandbyOffline",
    "ProfileError": "StandbyOffline",
    "Unmanaged": "StandbyOffline",
    "Removing": "Updating",
    "ApplyingProfile": "Updating",
    "RemovingProfile": "Updating",
    "UpdatingFirmware": "Updating",
    "Adding": "Updating",
    "Removed": "Disabled"
}

SERVER_PROFILE_STATE_MAPPING = {
    "Normal": "Enabled",
    "Creating": "Updating",
    "Updating": "Updating",
    "Deleting": "Updating",
    "CreateFailed": "StandbyOffline",
    "UpdateFailed": "StandbyOffline",
    "DeleteFailed": "StandbyOffline"
}


def get_redfish_status_struct(oneview_status):
    """Gets corresponding Redfish Status struct containing

        State and Health properties
    """
    state = STATUS_MAP[oneview_status]["State"]
    health = STATUS_MAP[oneview_status]["Health"]
    return state, health


def get_redfish_state(oneview_state, ov_to_rf_map):
    """Gets corresponding Redfish State"""
    return ov_to_rf_map.get(oneview_state, None)


def get_redfish_health_status(oneview_health_status):
    """Gets corresponding Redfish Health"""

    return HEALTH_STATUS_MAPPING[oneview_health_status]
