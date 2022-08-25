import networkx as nx
import matplotlib.pyplot as plt


def create_shortest_path_graph(graph, source, target):
    sub_graph = nx.DiGraph()

    val_map = {
        source: 0.0,
        target: 1.0
    }
    jump = 1 / (nx.shortest_path_length(graph, source=source, target=target) - 1)

    for path in nx.all_shortest_paths(graph, source, target):
        nx.add_path(sub_graph, path)
        val = 0
        for node in path[1: -2]:
            val += jump
            val_map[node] = val

    colors = [val_map.get(node, 0.25) for node in sub_graph.nodes()]

    nx.draw(sub_graph, cmap=plt.get_cmap("viridis"), node_color=colors, with_labels=True, font_color="white")
    plt.show()


if __name__ == '__main__':
    dod = {
        "A": ["E", "C", "F"],
        "B": ["F"],
        "C": ["A", "B"],
        "D": [],
        "E": ["A", "D"],
        "F": ["D"]
    }

    G = nx.from_dict_of_lists(dod, create_using=nx.DiGraph)
    nx.draw(G, with_labels=True)
    plt.show()
    create_shortest_path_graph(G, "C", "D")
