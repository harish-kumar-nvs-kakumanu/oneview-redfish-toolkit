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


class OneViewRedfishError(Exception):

    def __init__(self, msg):
        self.msg = msg


class OneViewRedfishResourceNotFoundError(OneViewRedfishError):

    def __init__(self, res_name, res_type):
        self.msg = "{} {} not found".format(res_type, res_name)


class OneViewRedfishResourceNotAccessibleError(OneViewRedfishError):

    def __init__(self, res_name, res_type):
        self.msg = "Can't access {} {}".format(res_type, res_name)