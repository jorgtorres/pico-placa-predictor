#!/usr/bin/env python
import unittest
from app.picoyplaca import PicoYPlaca as PP

class TestingLicensePlate(unittest.TestCase):
    def setUp(self):
        self.picoyplaca = PP('ASD-121', '2017-11-06', '16:00')
        #END setup

    def test_canitbeonroad(self):
        self.assertEqual(self.picoyplaca.CanItBeOnRoad(), False)
        #END test_canitbeonroad

if __name__ == "__main__":
    unittest.main()