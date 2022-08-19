import pydot
from missonaries_and_cannibals import State, Node
from utils import add_edge, add_node

def main():
    initial_state = State(3,3,0)
    initial_node = Node(parent_node=None, state=initial_state, action=None)
    graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='white', abel="Missionaries and Cannibals State Space",fontsize="30", color="red", fontcolor="blue", style="filled")
    add_node(graph, initial_node)

    # visited_nodes = [initial_node]
    live_node = [initial_node]
    
    while True:
        state = State.LIVE_STATES[0]
        if state.is_goal_state():
            break
        node = live_node.pop(0)
        child = state.children_states()
        for c in child:
            child_node = Node(node, c[0], c[1])
            add_node(graph, child_node)
            add_edge(graph, child_node)
            if not c[0].killed:
                live_node.append(child_node)
    legend(graph)
    graph.write_png('output.png')

def legend(graph):
    graphlegend = pydot.Cluster(graph_name="legend", label="Legend", fontsize="20", color="red",
                                fontcolor="blue", style="filled", fillcolor="white")

    initial = pydot.Node('Initial node', shape="plaintext")
    graphlegend.add_node(initial)
    legend1 = pydot.Node('Processed node', shape="plaintext")
    graphlegend.add_node(legend1)
    legend2 = pydot.Node("Killed Node", shape="plaintext")
    graphlegend.add_node(legend2)
    legend3 = pydot.Node('No new child possible', shape="plaintext")
    graphlegend.add_node(legend3)
    legend4 = pydot.Node('Goal Node', shape="plaintext")
    graphlegend.add_node(legend4)
    legend5=pydot.Node('Node [m, c, b]=> m,c = No. of missionaries and cannibals at left bank\n'
                       '               If b=0 -> boat at left bank\n'
                       '               If z=1-> boat at right bank\n'
                       'Edge [m,c,b]=> If b=-1-> Move m missionaries and c cannibals to right bank\n'
                       '               If b=1-> Move m missionaries and c cannibals to left bank', shape="plaintext",fontsize="15")
    graphlegend.add_node(legend5)

    node0 = pydot.Node("0", style="filled", fillcolor="#0D6EFD", label="")
    graphlegend.add_node(node0)
    node1 = pydot.Node("1", style="filled", fillcolor="#6C757D", label="")
    graphlegend.add_node(node1)
    node2 = pydot.Node("2", style="filled", fillcolor="#DC3545", label="")
    graphlegend.add_node(node2)
    node3 = pydot.Node("3", style="filled", fillcolor="#F687A4", label="")
    graphlegend.add_node(node3)
    node4 = pydot.Node("4", style="filled", fillcolor="#198754", label="")
    graphlegend.add_node(node4)

    graph.add_subgraph(graphlegend)
    graph.add_edge(pydot.Edge(initial, legend1, style="invis"))
    graph.add_edge(pydot.Edge(legend1, legend2, style="invis"))
    graph.add_edge(pydot.Edge(legend2, legend3, style="invis"))
    graph.add_edge(pydot.Edge(legend3, legend4, style="invis"))
    graph.add_edge(pydot.Edge(legend4, legend5, style="invis"))
    graph.add_edge(pydot.Edge(node0, node1, style="invis"))
    graph.add_edge(pydot.Edge(node1, node2, style="invis"))
    graph.add_edge(pydot.Edge(node2, node3, style="invis"))
    graph.add_edge(pydot.Edge(node3, node4, style="invis"))

    namelegend = pydot.Cluster(graph_name="name", label="Name", fontsize="24", color="Blue",
                                fontcolor="Red", style="filled", fillcolor="white")
    name = pydot.Node("Ramraj Chimouriya\n CE IV/I \n Roll No 14", shape="plaintext")
    namelegend.add_node(name)

    graph.add_subgraph(namelegend)

if __name__ == "__main__":
    main()