from sklearn.feature_extraction.text import TfidVectrizer

class EmbeddingModel:
    def embed(self, texts):
        vec = TfidVectorizer()
        return vec.fit_transform(texts).toarray