import wikipedia


ny = wikipedia.search("New York City", results=1, suggestion=False)
print(dir(ny[0]))
print(wikipedia.WikipediaPage(pageid=1874).links)
