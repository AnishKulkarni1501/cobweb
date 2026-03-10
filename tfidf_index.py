import json
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

with open("index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

documents = [page["text"] for page in data]
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(documents)
terms = vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=terms
)
tfidf_df.to_csv("tfidf_index.csv", index=False)
