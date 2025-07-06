from graph import Graph
from vehicle import Vehicle
from hashtable import VehicleHashTable
from sorting import find_nearest_vehicle, find_vehicle_with_highest_battery

def get_valid_int(prompt):
    """Ensures input is a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")

def get_valid_float(prompt):
    """Ensures input is a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    graph = Graph()
    vehicle_table = VehicleHashTable()

    while True:
        print("\nAutonomous Vehicle Management System")
        print("1. Add Vertex (Location)")
        print("2. Add Edge (Road)")
        print("3. Add Vehicle")
        print("4. Search Vehicle")
        print("5. Display Vehicles")
        print("6. Display Graph")
        print("7. Find Nearest Vehicle")
        print("8. Find Vehicle with Highest Battery")
        print("9. Get Neighbors of a Location")
        print("10. Check if Path Exists Between Two Locations")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            location = input("Enter location: ").strip()
            if location:
                graph.add_vertex(location)
                print("Location added successfully.")
            else:
                print("Location name cannot be empty!")

        elif choice == "2":
            loc1 = input("Enter start location: ").strip()
            loc2 = input("Enter end location: ").strip()
            if loc1 and loc2 and loc1 != loc2:
                distance = get_valid_float("Enter distance: ")
                graph.add_edge(loc1, loc2, distance)
                print("Road added successfully.")
            else:
                print("Invalid locations. Ensure they are not empty and different.")

        elif choice == "3":
            vid = get_valid_int("Enter Vehicle ID: ")
            location = input("Enter current location: ").strip()
            destination = input("Enter destination: ").strip()
            if location and destination:
                distance = get_valid_float("Enter distance to destination: ")
                battery = get_valid_int("Enter battery level (0-100): ")
                if 0 <= battery <= 100:
                    vehicle = Vehicle(vid, location, destination, distance, battery)
                    vehicle_table.insert(vehicle)
                    print("Vehicle added successfully.")
                else:
                    print("Battery level must be between 0 and 100.")
            else:
                print("Location and destination cannot be empty!")

        elif choice == "4":
            vid = get_valid_int("Enter Vehicle ID: ")
            vehicle = vehicle_table.search(vid)
            print(vehicle if vehicle else "Vehicle not found.")

        elif choice == "5":
            vehicle_table.display_all()

        elif choice == "6":
            graph.display_graph()

        elif choice == "7":
            nearest = find_nearest_vehicle(vehicle_table.table)
            print(nearest if nearest else "No vehicles available.")

        elif choice == "8":
            highest_battery = find_vehicle_with_highest_battery(vehicle_table.table)
            print(highest_battery if highest_battery else "No vehicles available.")

        elif choice == "9":
            location = input("Enter the location: ").strip()
            neighbors = graph.get_neighbors(location)
            if neighbors:
                print(f"Neighbors of {location}:")
                for neighbor, distance in neighbors:
                    print(f" - {neighbor} ({distance} km)")
            else:
                print(f"No neighbors found for {location} or location does not exist.")

        elif choice == "10":
            src = input("Enter source location: ").strip()
            dest = input("Enter destination location: ").strip()
            if graph.is_path(src, dest):
                print(f"A path exists between {src} and {dest}.")
            else:
                print(f"No path exists between {src} and {dest}.")

        elif choice == "11":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 11.")


if __name__ == "__main__":
    main()
