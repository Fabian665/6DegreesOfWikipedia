def main():
    graph = nx.complete_graph(5)
    nx.draw(graph)
    plt.show()


if __name__ == "__main__":
    import networkx as nx
    import matplotlib.pyplot as plt
    main()
