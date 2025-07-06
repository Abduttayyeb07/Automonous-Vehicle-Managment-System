# test_sorting.py

import unittest
from sorting import heapsort, quicksort
from vehicle import Vehicle

class TestSorting(unittest.TestCase):
    def setUp(self):
        """Set up a list of vehicles for sorting tests."""
        self.vehicles = [
            Vehicle(201, "X", "Y", 30, 50),
            Vehicle(202, "A", "B", 10, 80),
            Vehicle(203, "C", "D", 20, 60),
        ]

    def test_heapsort_distance(self):
        """Test Heapsort by sorting vehicles based on distance_to_destination."""
        sorted_vehicles = heapsort(self.vehicles, key=lambda v: v.get_distance_to_destination())
        self.assertEqual([v.distance_to_destination for v in sorted_vehicles], [10, 20, 30])

    def test_quicksort_battery(self):
        """Test Quicksort by sorting vehicles based on battery_level."""
        sorted_vehicles = quicksort(self.vehicles, key=lambda v: v.battery_level, reverse=True)
        self.assertEqual([v.battery_level for v in sorted_vehicles], [80, 60, 50])

if __name__ == "__main__":
    unittest.main()
