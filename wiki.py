import wikipedia


ny = wikipedia.search("New York City", results=1, suggestion=False)
print(ny[0])
print(wikipedia.WikipediaPage(ny[0]).url)
