import json
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from pagerank import pagerank_scores
import numpy as np


pagerank_threshold = 0.5
tfidf_matrix_threshold = 0.5 #both can be adjusted acc. to which one is more accurate.


with open("index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

documents = [page["text"] for page in data]
urls = [page["url"] for page in data]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(documents)
terms = vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=terms
)

tfidf_df.to_csv("tfidf_index.csv", index=False)
query = input("Search: ")

query_vec = vectorizer.transform([query])

scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
pagerank_list = [pagerank_scores[url] for url in urls]

pagerank_list = np.array(pagerank_list)

total_score = pagerank_list*pagerank_threshold + scores*tfidf_matrix_threshold

top_indices = total_score.argsort()[-5:][::-1]

for i in top_indices:
    print(urls[i], total_score[i])



        