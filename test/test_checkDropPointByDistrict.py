import json
import unittest
from src.JntCrawling import JntCrawling
from src.Exception import parameter_error, no_data_found


class BaseCheckDropPointByDistrictTest(unittest.TestCase):
    def test_check_drop_point_by_district_parameter_error(self):
        self.assertRaises(parameter_error, JntCrawling().checkDropPointByDistrict, None)

    def test_check_drop_point_by_district_success(self):
        jnt = JntCrawling().checkDropPointByDistrict(district="SRAGEN", city="SRAGEN", province="JAWA TENGAH")
        self.assertEqual(json.loads(jnt)['status'], "success")

    def test_check_drop_point_by_district_fail(self):
        self.assertRaises(no_data_found, JntCrawling().checkDropPointByDistrict, district="so", city="sa",
                          province="jt")
