import networkx as nx
from pydantic import BaseModel
import json

"""
#TODO load your graph here
"""


class Route(BaseModel):
    origin: str
    destination: str
    distance: float
    profit: float


def get_distance(origin: str, destination: str) -> float:
    """#TODO"""
    raise NotImplementedError


def get_minimum_distance(origin: str, destinations: list[str]) -> float:
    """#TODO"""
    raise NotImplemented


def get_route_info(origin, destination) -> Route:
    """#TODO"""
    raise NotImplementedError
