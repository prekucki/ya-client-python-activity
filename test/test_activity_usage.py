# coding: utf-8

"""
    Yagna Activity API

    It conforms with capability level 1 of the [Activity API specification](https://docs.google.com/document/d/1BXaN32ediXdBHljEApmznSfbuudTU8TmvOmHKl0gmQM).  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ya_activity
from ya_activity.models.activity_usage import ActivityUsage  # noqa: E501
from ya_activity.rest import ApiException

class TestActivityUsage(unittest.TestCase):
    """ActivityUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ActivityUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ya_activity.models.activity_usage.ActivityUsage()  # noqa: E501
        if include_optional :
            return ActivityUsage(
                current_usage = [
                    1.337
                    ], 
                timestamp = 56
            )
        else :
            return ActivityUsage(
        )

    def testActivityUsage(self):
        """Test ActivityUsage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
