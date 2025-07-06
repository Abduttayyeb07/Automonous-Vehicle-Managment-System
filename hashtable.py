# vehicle_hash_table.py

class VehicleHashTable:
    """Hash Table for managing vehicles using Linear Probing for collision resolution."""

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # Using a list for Linear Probing

    def _hash(self, vehicle_id):
        """Hash function based on vehicle ID."""
        return vehicle_id % self.size

    def insert(self, vehicle):
        """Inserts a vehicle into the hash table using Linear Probing."""
        index = self._hash(vehicle.vehicle_id)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash Table is full")
        self.table[index] = vehicle

    def delete(self, vehicle_id):
        """Deletes a vehicle from the hash table."""
        index = self._hash(vehicle_id)
        original_index = index
        while self.table[index] is not None:
            if self.table[index].vehicle_id == vehicle_id:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                return

    def search(self, vehicle_id):
        """Searches for a vehicle in the hash table."""
        index = self._hash(vehicle_id)
        original_index = index
        while self.table[index] is not None:
            if self.table[index].vehicle_id == vehicle_id:
                return self.table[index]
            index = (index + 1) % self.size
            if index == original_index:
                return None
        return None

    def display_all(self):
        """Displays all vehicles stored in the hash table."""
        for i, vehicle in enumerate(self.table):
            if vehicle:
                print(f"Index {i}: {vehicle}")
