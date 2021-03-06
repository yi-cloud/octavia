# Copyright 2015 Hewlett-Packard Development Company, L.P.
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
#

from taskflow import task


class DeleteModelObject(task.Task):
    """Task to delete an object in a model."""

    def execute(self, object):

        object.delete()


class UpdateAttributes(task.Task):
    """Task to update an object for changes."""

    def execute(self, object, update_dict):
        """Update an object and its associated resources.

        Note: This relies on the data_model update() methods to handle complex
              objects with nested objects (LoadBalancer.vip,
              Pool.session_persistence, etc.)

        :param object: The object will be updated.
        :param update_dict: The updates dictionary.
        :returns: None
        """
        object.update(update_dict)
