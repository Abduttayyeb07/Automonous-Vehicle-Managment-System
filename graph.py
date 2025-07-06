from collections import deque

class Graph:
    """Graph class to represent the road network using an adjacency list."""

    def __init__(self):
        self.graph = {}

    def add_vertex(self, location):
        """Adds a new location (vertex) to the graph."""
        if location not in self.graph:
            self.graph[location] = []

    def add_edge(self, location1, location2, distance):
        """Adds a road (edge) between two locations with a given distance."""
        if location1 in self.graph and location2 in self.graph:
            self.graph[location1].append((location2, distance))
            self.graph[location2].append((location1, distance))

    def get_neighbors(self, location):
        """Retrieves the neighbors of a given location."""
        return self.graph.get(location, [])

    def display_graph(self):
        """Displays the adjacency list representation of the graph."""
        print("\nGraph Representation (Adjacency List):")
        for location, neighbors in self.graph.items():
            edges = ", ".join([f"{neighbor} ({distance} km)" for neighbor, distance in neighbors])
            print(f"{location} -> {edges}")

    def is_path(self, source, destination):
        """Checks if a path exists between source and destination using BFS or DFS."""
        visited = set()
        return self.bfs(source, destination) or self.dfs(source, destination, visited)

    def dfs(self, current, destination, visited):
        """Performs Depth-First Search (DFS) to check for a path."""
        if current == destination:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor, _ in self.graph.get(current, []):
                if self.dfs(neighbor, destination, visited):
                    return True
        return False

    def bfs(self, source, destination):
        """Performs Breadth-First Search (BFS) to check for a path."""
        queue = deque([source])
        visited = set()
        while queue:
            current = queue.popleft()
            if current == destination:
                return True
            if current not in visited:
                visited.add(current)
                for neighbor, _ in self.graph.get(current, []):
                    queue.append(neighbor)
        return False
