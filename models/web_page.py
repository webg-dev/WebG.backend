from typing import Dict, Any, List
from uuid import UUID, uuid4

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
    from_: int = Field(..., alias='from')
    to_: int = Field(..., alias='to')


class Graph(BaseModel):
    nodes: List[Node]
    edges: List[Edge]


class NodeLabel(BaseModel):
    node_id: int = Field(..., alias='nodeId')
    class_name: str = Field(..., alias='className')


class WebPage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    url: str
    viewport_width: int = Field(..., alias='viewportWidth')
    viewport_height: int = Field(..., alias='viewportHeight')
    html: str
    screenshot: str
    graph: Graph
    labels: List[NodeLabel] = []
