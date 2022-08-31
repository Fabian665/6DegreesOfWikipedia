import networkx as nx
import matplotlib.pyplot as plt
import wikipedia
import json

def csv_reader(file_name):
    for row in open(file_name, "r", encoding="utf8"):
        yield row


def read_from_index_file(filename):
    """generator for id  of pages from the index file"""
    csv_gen = csv_reader(filename)
    row_count = 0
    page_id = 0
    page_name = ""

    for row in csv_gen:
        page_id = row.split(":", 2)[1]
        page_name = row.split(":", 2)[2][:-1]
        if row_count > 150:
            break
        yield page_name, page_id
        row_count += 1


def get_neighbours(page_id):
    """get neighbours of given page_id"""
    dic_neighbours = wikipedia.WikipediaPage(pageid=page_id).links
    return dic_neighbours


def get_id_from_name(page_name):
    pass


def create_json_file():
    keys = read_from_index_file(filename="C:\\Users\\fabia\\Downloads\\enwiki-20220101-pages-articles-multistream\\enwiki-20220101-pages-articles-multistream-index.txt")
    dic = {}
    for name, page_id in keys:
        try:
            neighbours = get_neighbours(page_id)
            dic[name] = neighbours
        except AttributeError:
            print(f'name {name} is a wierdo')
        except wikipedia.exceptions.DisambiguationError:
            print(f'name {name} is even weirder')
    with open('wikipedia.json', 'w') as f:
        json.dump(dic, f, indent=4)


def main():
    # graph = nx.complete_graph(5)
    # nx.draw(graph)
    # plt.show()
    create_json_file()
    # gen = read_from_index_file(filename="C:\\Users\\fabia\\Downloads\\enwiki-20220101-pages-articles-multistream\\enwiki-20220101-pages-articles-multistream-index.txt")
    # [print(i) for i in gen]

if __name__ == "__main__":
    main()
