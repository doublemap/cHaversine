from __future__ import print_function
from cHaversine import haversine
import unittest

paris = (48.8567, 2.3508)
london = (51.5072, 0.1275)
tokyo = (35.6833, 139.6833)
cape_town = (-33.9253, 18.4239)
denver = (39.7392, -104.9903)
santiago = (-70.6667, -33.45)


class TestCHaversine(unittest.TestCase):

    def test_paris_to_cape_town(self):
        dist = haversine(paris, cape_town)
        known_dist = 9336 * 1000
        self.assertTrue(abs(dist - known_dist) < 5000)

    def test_tokyo_to_santiago(self):
        dist = haversine(tokyo, santiago)
        known_dist = 16090 * 1000
        self.assertTrue(abs(dist - known_dist) < 5000)

    def test_0_to_1(self):
        dist = haversine((0, 0), (1, 1))
        known_dist = 156900
        self.assertTrue(abs(dist - known_dist) < 1000)

if __name__ == '__main__':
    unittest.main()
