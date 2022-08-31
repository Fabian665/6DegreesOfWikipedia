import networkx as nx
import matplotlib.pyplot as plt
import wikipedia

def read_from_index_file():
    """generator for id  of pages from the index file"""
    pass


def get_neighbours(page_id):
    """get neighbours of given page_id"""
    dic_neighbours = wikipedia.WikipediaPage(pageid=page_id).links
    return dic_neighbours


def get_id_from_name(page_id):
    pass


def create_json_file():
    pass


def main():
    graph = nx.complete_graph(5)
    nx.draw(graph)
    plt.show()


if __name__ == "__main__":
    main()
