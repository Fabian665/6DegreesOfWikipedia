import networkx as nx
import matplotlib.pyplot as plt

dod = {
    "A": ["E", "D", "C"],
    "B": ["D"],
    "C": ["A", "B"],
    "D": [],
    "E": ["A", "D"]
}

G = nx.from_dict_of_lists(dod, create_using=nx.DiGraph)
print([p for p in nx.all_shortest_paths(G, "C", "D")])
nx.draw(G, with_labels=True)
plt.show()
