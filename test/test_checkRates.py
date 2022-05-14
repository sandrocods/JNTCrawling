import json
import unittest
from src.JntCrawling import JntCrawling
from src.Exception import parameter_error, no_data_found


class BaseCheckRatesTest(unittest.TestCase):

    def test_check_rates_invalid_parameters(self):
        self.assertRaises(no_data_found, JntCrawling().checkRates, receiverAddress="soldo", senderAddress="solod",
                          weight=1.6)

    def test_check_rates_valid_parameters(self):
        self.assertEqual(json.loads(
            JntCrawling().checkRates(weight=16.68, receiverAddress="PURWOKERTO SELATAN", senderAddress="KARANG ANYAR"))[
                             'status'], "success")
