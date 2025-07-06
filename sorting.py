# sorting.py

import heapq

def heapsort(arr, key=lambda x: x):
    """Sorts vehicles using Heapsort based on a given key."""
    heap = [(key(v), v) for v in arr]  # Convert to (key, value) tuples
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(len(heap))]  # Extract sorted values

def quicksort(arr, key=lambda x: x, reverse=False):
    """Sorts vehicles using Quicksort based on a given key."""
    if len(arr) <= 1:
        return arr

    pivot = key(arr[len(arr) // 2])  # Use the key function for comparison
    if reverse:
        left = [x for x in arr if key(x) > pivot]  # Sort in descending order
        right = [x for x in arr if key(x) < pivot]
    else:
        left = [x for x in arr if key(x) < pivot]  # Sort in ascending order
        right = [x for x in arr if key(x) > pivot]
    
    middle = [x for x in arr if key(x) == pivot]

    return quicksort(left, key, reverse) + middle + quicksort(right, key, reverse)

def find_nearest_vehicle(vehicles):
    """Finds the vehicle closest to its destination."""
    vehicles = [v for v in vehicles if v is not None]
    return min(vehicles, key=lambda v: v.get_distance_to_destination(), default=None)

def find_vehicle_with_highest_battery(vehicles):
    """Finds the vehicle with the highest battery level."""
    vehicles = [v for v in vehicles if v is not None]
    return max(vehicles, key=lambda v: v.get_battery_level(), default=None)
