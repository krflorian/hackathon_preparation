import networkx as nx
from pydantic import BaseModel
import json

graph = nx.Graph()

# load graph
with open("graph.json", "r") as infile:
    data = json.load(infile)

# add edges to graph object
for origin in data:
    for destination in data[origin]:
        graph.add_edge(
            origin, destination, distance=data[origin][destination]["distance"]
        )


class Route(BaseModel):
    origin: str
    destination: str
    distance: float
    profit: float


def get_profit(distance: float, revenue: float) -> float:
    return revenue - distance * 1.2


def get_distance(origin: str, destination: str) -> float:
    return nx.shortest_path_length(graph, origin, destination, weight="distance")


def get_minimum_distance(origin: str, destinations: list[str]) -> tuple[str, float]:
    paths = nx.shortest_path_length(graph, source=origin, weight="distance")
    paths = {node: distance for node, distance in paths.items() if node in destinations}
    return sorted(paths.items(), key=lambda x: x[0])[0]


def get_route_info(origin, destination, revenue) -> Route:
    distance = get_distance(origin, destination)
    profit = get_profit(distance, revenue)
    return Route(
        origin=origin, destination=destination, distance=distance, profit=profit
    )
