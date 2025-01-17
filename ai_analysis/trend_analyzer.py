from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

class TrendAnalyzer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.kmeans = KMeans(n_clusters=5)

    def analyze_trends(self, descriptions):
        tfidf_matrix = self.vectorizer.fit_transform(descriptions)
        self.kmeans.fit(tfidf_matrix)
        
        cluster_centers = self.kmeans.cluster_centers_
        order_centroids = cluster_centers.argsort()[:, ::-1]
        terms = self.vectorizer.get_feature_names_out()
        
        trends = []
        for i in range(5):
            trend_terms = [terms[ind] for ind in order_centroids[i, :10]]
            trends.append(trend_terms)
        
        return trends

    def predict_virality(self, description, likes, comments, shares):
        engagement = int(likes) + int(comments) * 2 + int(shares) * 3
        return engagement > 10000
