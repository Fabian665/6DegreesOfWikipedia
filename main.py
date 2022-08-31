import networkx as nx
import matplotlib.pyplot as plt
import wikipedia
import json

def read_from_index_file():
    """generator for id  of pages from the index file"""
    def csv_reader(file_name):
        for row in open(file_name, "r", encoding="utf8"):
            yield row

    csv_gen = csv_reader("enwiki-20220101-pages-articles-multistream-index.txt")
    row_count = 0
    page_id = 0
    page_name = ""

    for row in csv_gen:
        page_id = row.split(":", 2)[1]
        page_name = row.split(":", 2)[2][:-1]
        yield page_name, page_id
        row_count += 1
    # print(f"Row count is {row_count}")


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
