import unittest
from vario import igc_parser
import datetime

class TestIGCParser(unittest.TestCase):
    def test_pfx_fix_record(self):
        d = igc_parser.IGCParser.pfx_fix_record("B1101355206343N00006198WA0058700558")
        self.assertEqual(d,
            {
                'time':     datetime.datetime.strptime("110135", "%H%M%S"),
                'lat':      "5206343N",
                'long':     "00006198W",
                'valid':    True,
                'baro_alt': 587,
                'gps_alt':  558
            }
        )

        d = igc_parser.IGCParser.pfx_fix_record("B1101455206259N00006295WV0059300556")
        self.assertEqual(d,
             {
                 'time': datetime.datetime.strptime("110145", "%H%M%S"),
                 'lat': "5206259N",
                 'long': "00006295W",
                 'valid': False,
                 'baro_alt': 593,
                 'gps_alt': 556
             }
        )

        # Make sure that the correct error is thrown on garbage input
        self.assertRaises(AssertionError, igc_parser.IGCParser.pfx_fix_record, "Bsomething shorter")
