# vehicle.py

class Vehicle:
    """Class representing an autonomous vehicle."""

    def __init__(self, vehicle_id, location, destination, distance_to_destination, battery_level):
        self.vehicle_id = vehicle_id
        self.location = location
        self.destination = destination
        self.distance_to_destination = distance_to_destination
        self.battery_level = battery_level

    def set_location(self, location):
        self.location = location

    def set_destination(self, destination):
        self.destination = destination

    def set_distance_to_destination(self, distance):
        self.distance_to_destination = distance

    def set_battery_level(self, level):
        self.battery_level = level

    def get_location(self):
        return self.location

    def get_destination(self):
        return self.destination

    def get_distance_to_destination(self):
        return self.distance_to_destination

    def get_battery_level(self):
        return self.battery_level

    def __str__(self):
        return (f"Vehicle {self.vehicle_id}: Location={self.location}, "
                f"Destination={self.destination}, Distance={self.distance_to_destination}, "
                f"Battery={self.battery_level}%")
