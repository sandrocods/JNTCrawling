import json
import unittest
from src.JntCrawling import JntCrawling
from src.Exception import no_data_found, error_no_billCode


class BaseTrackReceiptTest(unittest.TestCase):

    def test_track_valid_receipt(self):
        jnt = JntCrawling().trackReceipt(billCodes="JP4392231394")
        self.assertEqual(json.loads(jnt)['status'], "success")

    def test_track_invalid_receipt(self):
        self.assertRaises(no_data_found, JntCrawling().trackReceipt, billCodes="JP439223134")

    def test_track_no_bill_code(self):
        self.assertRaises(error_no_billCode, JntCrawling().trackReceipt, billCodes="")
