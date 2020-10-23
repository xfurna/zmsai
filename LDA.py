import warnings
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer


class heuristics:
    def __init__(self, numTopics=base.numberTopics, path=base.path):
        # Initialise the count vectorizer with the English stop words
        count_vectorizer = CountVectorizer(stop_words="english")

        # Fit and transform the processed titles
        count_data = count_vectorizer.fit_transform(papers)

        # Visualise the 10 most common words
        warnings.simplefilter("ignore", DeprecationWarning)

        # Load the LDA model from sk-learn

        # Create and fit the LDA model
        lda = LDA(n_components=number_topics)
        lda.fit(count_data)
        trfm = lda.transform(count_data)
