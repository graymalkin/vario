import unittest
from vario import gps_helper
from math import pi

class TestGPSHelper(unittest.TestCase):
    def test_minutes_to_decimal(self):
        self.assertAlmostEqual( 000.1008194, gps_helper.minutes_to_decimal("00006295E"))
        self.assertAlmostEqual(-000.1008194, gps_helper.minutes_to_decimal("00006295W"))
        self.assertAlmostEqual( 096.5345028, gps_helper.minutes_to_decimal("096032421E"))
        self.assertAlmostEqual(-096.5345028, gps_helper.minutes_to_decimal("096032421W"))

        self.assertRaises(ValueError, gps_helper.minutes_to_decimal, "short")

        self.assertAlmostEqual(0.0, gps_helper.minutes_to_decimal("00000000W"))
        self.assertAlmostEqual(0.0, gps_helper.minutes_to_decimal("00000000E"))
        self.assertAlmostEqual(0.0, gps_helper.minutes_to_decimal("00000000N"))
        self.assertAlmostEqual(0.0, gps_helper.minutes_to_decimal("00000000S"))

    def test_haversine(self):
        # Circumference of earth = 2*radius*pi = 6371*2.0*pi
        # Distance between poles = half the circumference
        self.assertAlmostEqual((6371*2.0*pi) / 2.0, gps_helper.haversine(-90.0, 0, 90.0, 0))

        self.assertAlmostEqual(0.0, gps_helper.haversine(-72, 14, -72, 14))

        # Big distances are inaccurate
        self.assertAlmostEqual(934.52, gps_helper.haversine(51.5074, -0.1278, 52.5200, 13.4050), places=-1)
        self.assertAlmostEqual(10.16, gps_helper.haversine(51.709899, -2.133092, 51.715537, -2.280741), places=1)

        # Small distances, to +- 10m
        self.assertAlmostEqual(0.03558, gps_helper.haversine(51.178761, -1.825948, 51.178953, -1.826394), places=2)