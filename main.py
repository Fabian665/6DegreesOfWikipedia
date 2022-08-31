import networkx as nx
import matplotlib.pyplot as plt
import wikipedia
import json

def read_from_index_file():
    """generator for id  of pages from the index file"""
    pass


def get_neighbours(page_id):
    """get neighbours of given page_id"""
    dic_neighbours = wikipedia.WikipediaPage(pageid=page_id).links
    return dic_neighbours


def get_id_from_name(page_name):
    pass


def create_json_file():
    keys = read_from_index_file()
    dic = {}
    for name in keys:
        neighbours = get_neighbours(name)
        dic[name] = neighbours
    with open('wikipedia.json', 'w') as f:
        json.dump(dic, f)





def main():
    graph = nx.complete_graph(5)
    nx.draw(graph)
    plt.show()


if __name__ == "__main__":
    main()
