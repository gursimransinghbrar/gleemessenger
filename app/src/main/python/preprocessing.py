from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
def preprocess(X):
    count_vect=CountVectorizer()
    X_train_counts=count_vect.fit_transform(X)
    X_train_counts.shape
    tfidf_transform=TfidfTransformer()
    X_train_tfidf=tfidf_transform.fit_transform(X_train_counts)
    X_train_counts.shape
    return X_train_tfidf
