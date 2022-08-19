import pydot
from missonaries_and_cannibals import Node, State

def add_node(graph:pydot.Dot,node:Node) -> None:
    color = node_color(node.state)
    graph.add_node(pydot.Node(str(node), label=node.label, color=color, style="filled"))

def add_edge(graph:pydot.Dot,node:Node) -> None:
    graph.add_edge(pydot.Edge(str(node.parent_node), str(node), label=node.edge_label, color="black"))

def node_color(state:State):
    if state.missonaries == 3 and state.cannibals == 2 and state.bank == 1:
        return "#F687A4"
    elif state.is_initial_state():
        return "#0D6EFD"
    elif state.goal:
        return "#198754"
    elif state.killed:
        return "#DC3545"
    else:
        return "#6C757D"