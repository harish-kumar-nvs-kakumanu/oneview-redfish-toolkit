# -*- coding: utf-8 -*-

# Copyright (2018) Hewlett Packard Enterprise Development LP
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

import json
from unittest import mock

from oneview_redfish_toolkit.api import session_service
from oneview_redfish_toolkit.api.session_service import SessionService
from oneview_redfish_toolkit.tests.base_test import BaseTest


@mock.patch.object(session_service, 'config')
class TestSessionService(BaseTest):
    """Tests for SessionService class"""

    def test_when_enabled(self, config_mock):
        config_mock.auth_mode_is_session.return_value = True
        with open(
            'oneview_redfish_toolkit/mockups/redfish/'
            'SessionService.json'
        ) as f:
            event_service_mockup = json.load(f)

        result = json.loads(SessionService().serialize())

        self.assertEqualMockup(event_service_mockup, result)

    def test_when_disabled(self, config_mock):
        config_mock.auth_mode_is_session.return_value = False
        with open(
            'oneview_redfish_toolkit/mockups/redfish/'
            'SessionServiceDisabled.json'
        ) as f:
            event_service_mockup = json.load(f)

        result = json.loads(SessionService().serialize())

        self.assertEqualMockup(event_service_mockup, result)
