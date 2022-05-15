import json
import unittest
from src.JntCrawling import JntCrawling
from src.Exception import no_data_found


class BaseCheckDropPointByGPSTest(unittest.TestCase):
    
#     Not work in action test github, in locally work
#     def test_check_drop_point_by_GPS(self):
#         jnt = JntCrawling().checkDropPointByGPS()
#         self.assertEqual(json.loads(jnt)['status'], "success")

    def test_check_drop_point_by_GPS_no_data_found(self):
        self.assertRaises(no_data_found, JntCrawling().checkDropPointByGPS, latitude="0", longitude="0")
