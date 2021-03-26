from typing import Dict, Any, List

from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    width: float
    height: float
    left: float
    right: float
    top: float
    bottom: float


class Node(BaseModel):
    id: int
    label: str
    attributes: Dict[str, Any]
    coordinates: Coordinates
    is_visible: bool = Field(..., alias='isVisible')


class Edge(BaseModel):
    # leading underscore added because 'from' would clash with internal python directive
    _from: int = Field(..., alias='from')
    _to: int = Field(..., alias='to')


class Graph(BaseModel):
    nodes: List[Node]
    edges: List[Edge]


class WebPage(BaseModel):
    url: str
    viewport_width: int = Field(..., alias='viewportWidth')
    viewport_height: int = Field(..., alias='viewportHeight')
    html: str
    screenshot: str
    graph: Graph
