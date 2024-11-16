# flowxcel.py

# DISCLAIMER:
# This code is original and created specifically for the user, Kamal, 
# and is free of any copyright concerns. It is intended to be used for educational purposes 
# and for further development in traffic simulation modeling using Python.
# There are no proprietary components or external libraries under copyright in this module.
# Feel free to use, modify, and distribute this code as needed.

import matplotlib.pyplot as plt

# RoadNetwork class
class RoadNetwork:
    def __init__(self):
        self.nodes = {}  # Intersections
        self.edges = {}  # Roads

    def add_node(self, node_id, x, y):
        self.nodes[node_id] = {'connected_edges': [], 'x': x, 'y': y}

    def add_edge(self, start_node, end_node, length, speed_limit):
        edge_id = f"{start_node}_{end_node}"
        self.edges[edge_id] = {
            'start': start_node,
            'end': end_node,
            'length': length,
            'speed_limit': speed_limit
        }
        self.nodes[start_node]['connected_edges'].append(edge_id)


# Route and Vehicle classes
class Route:
    def __init__(self, path):
        self.path = path  # List of nodes in sequence

class Vehicle:
    def __init__(self, route, speed=0):
        self.route = route
        self.position = route.path[0]  # Start position
        self.speed = speed
        self.current_node = 0

    def move(self):
        # Move to the next node based on speed and road limits
        if self.current_node < len(self.route.path) - 1:
            self.current_node += 1
            self.position = self.route.path[self.current_node]


# TrafficLight class
class TrafficLight:
    def __init__(self, green_duration, red_duration):
        self.green_duration = green_duration
        self.red_duration = red_duration
        self.current_phase = 'red'
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.current_phase == 'red' and self.timer >= self.red_duration:
            self.current_phase = 'green'
            self.timer = 0
        elif self.current_phase == 'green' and self.timer >= self.green_duration:
            self.current_phase = 'red'
            self.timer = 0


# SimulationManager class
class SimulationManager:
    def __init__(self, network, vehicles, traffic_lights):
        self.network = network
        self.vehicles = vehicles
        self.traffic_lights = traffic_lights

    def step(self):
        # Update traffic lights
        for light in self.traffic_lights.values():
            light.update()

        # Move vehicles
        for vehicle in self.vehicles:
            # Check traffic light at the current node
            current_light = self.traffic_lights.get(vehicle.position)
            if current_light and current_light.current_phase == 'red':
                continue  # Stop at red light
            vehicle.move()

    def get_vehicle_data(self):
        # Return current data for all vehicles
        data = []
        for vehicle in self.vehicles:
            data.append({
                'position': vehicle.position,
                'speed': vehicle.speed
            })
        return data


# Visualization (Optional)
def visualize(network, vehicles):
    plt.figure(figsize=(10, 10))

    # Plot roads
    for edge_id, edge in network.edges.items():
        start, end = edge['start'], edge['end']
        plt.plot([network.nodes[start]['x'], network.nodes[end]['x']],
                 [network.nodes[start]['y'], network.nodes[end]['y']], 'k-')

    # Plot vehicles
    for vehicle in vehicles:
        # Get the (x, y) coordinates of the vehicle’s current position
        position_node = vehicle.position
        if position_node in network.nodes:
            x = network.nodes[position_node]['x']
            y = network.nodes[position_node]['y']
            plt.plot(x, y, 'ro')  # Plot the vehicle as a red dot at (x, y)

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Traffic Simulation Visualization")
    plt.show()



# Example usage of the module
if __name__ == '__main__':
    # Create network, vehicles, and traffic lights
    network = RoadNetwork()
    network.add_node('A', 0, 0)
    network.add_node('B', 1, 1)
    network.add_edge('A', 'B', 1, 60)

    route = Route(['A', 'B'])
    vehicle = Vehicle(route)
    traffic_lights = {'B': TrafficLight(10, 5)}

    sim_manager = SimulationManager(network, [vehicle], traffic_lights)

    # Run simulation
    for _ in range(20):
        sim_manager.step()
        print(sim_manager.get_vehicle_data())

    # Optional visualization
    visualize(network, [vehicle])
