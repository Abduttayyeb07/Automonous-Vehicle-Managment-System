# test_hashtable.py

import unittest
from hashtable import VehicleHashTable
from vehicle import Vehicle

class TestVehicleHashTable(unittest.TestCase):
    def setUp(self):
        """Set up a fresh hash table before each test."""
        self.hash_table = VehicleHashTable(size=5)
        self.vehicle1 = Vehicle(101, "A", "B", 15, 80)
        self.vehicle2 = Vehicle(102, "C", "D", 10, 90)

    def test_insert(self):
        """Test inserting vehicles into the hash table."""
        self.hash_table.insert(self.vehicle1)
        self.assertIsNotNone(self.hash_table.search(101))

    def test_search(self):
        """Test searching for a vehicle."""
        self.hash_table.insert(self.vehicle1)
        found_vehicle = self.hash_table.search(101)
        self.assertEqual(found_vehicle.vehicle_id, 101)

    def test_delete(self):
        """Test deleting a vehicle from the hash table."""
        self.hash_table.insert(self.vehicle1)
        self.hash_table.delete(101)
        self.assertIsNone(self.hash_table.search(101))

    def test_collision_resolution(self):
        """Test that collisions are resolved using linear probing."""
        vehicle3 = Vehicle(106, "E", "F", 20, 50)  # Hash collision with 101
        self.hash_table.insert(self.vehicle1)
        self.hash_table.insert(vehicle3)
        self.assertIsNotNone(self.hash_table.search(106))

    def test_display_all(self):
        """Ensure the hash table displays stored vehicles."""
        self.hash_table.insert(self.vehicle1)
        self.hash_table.display_all()

if __name__ == "__main__":
    unittest.main()
