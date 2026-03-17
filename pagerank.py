import json
import networkx as nx

with open("index.json", "r", encoding="utf-8") as f:
    data = json.load(f)
G = nx.DiGraph()


for page in data:
    url = page["url"]
    for link in page["links"]:
        G.add_edge(url, link)

pagerank_scores = nx.pagerank(G)