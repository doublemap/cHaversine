from __future__ import print_function
import math
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

    def test_small_distance(self):
        # floats will store these two coordinates as the same value, resulting
        # in dist = 0.
        # doubles are able to distinguish these two points.
        dist = haversine((39, -88.97223382), (39, -88.972237))
        self.assertTrue(dist > 0)

    def test_same_coords(self):
        # distance between a coord and itself should not be NaN
        dist = haversine((39.11, -86.7), (39.11, -86.7))
        self.assertFalse(math.isnan(dist))

if __name__ == '__main__':
    unittest.main()
