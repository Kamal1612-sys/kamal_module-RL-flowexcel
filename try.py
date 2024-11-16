import sys
import os
from flowxcel import RoadNetwork, Vehicle, Route, TrafficLight, SimulationManager, visualize

# Create a road network
network = RoadNetwork()
network.add_node('A', 0, 0)
network.add_node('B', 2, 2)
network.add_node('C', 4, 0)

network.add_edge('A', 'B', 2, 60)
network.add_edge('B', 'C', 2, 60)

# Create a route for the vehicle
route = Route(['A', 'B', 'C'])

# Create vehicles and assign them to the route
vehicle1 = Vehicle(route)
vehicle2 = Vehicle(route)

# Define traffic lights at each intersection
traffic_lights = {
    'A': TrafficLight(10, 5),
    'B': TrafficLight(8, 4),
    'C': TrafficLight(6, 3),
}

# Create a simulation manager to handle the traffic simulation
sim_manager = SimulationManager(network, [vehicle1, vehicle2], traffic_lights)

# Run the simulation for 20 steps
for step in range(20):
    print(f"Step {step + 1} of the simulation:")

    # Update traffic lights
    for light in traffic_lights.values():
        light.update()

    sim_manager.step()
    print(sim_manager.get_vehicle_data())
    visualize(network, [vehicle1, vehicle2])  # Visualize the network and vehicles

print("\nFinal state of vehicles:")
print(sim_manager.get_vehicle_data())