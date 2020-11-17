from zmsai.readData import read_txt
from zmsai.utils import print_topics
from zmsai.utils import print_list
from zmsai.utils import padding
from zmsai.utils import countFiles

import warnings

warnings.simplefilter("ignore", DeprecationWarning)


class heuristics:
    def __init__(self, path, numberTopics):
        data = read_txt(path)
        self.ndocs, self.docs = countFiles(path)
        self.vector, self.vectorizer = self.get_feature_space(data)
        self.transform, self.lda = self.LDA_transform(numberTopics)

    def get_topic_word_distrib(self, nWords):
        topic_word = self.lda.components_
        print_topics(self.lda, self.vectorizer, nWords)
        return topic_word

    def get_doc_word_distrib(self, nWords):
        print("=====================")
        print("DOC-WORD DISTRIBUTION")
        print("=====================")
        message = "Words\t\tCount"
        import numpy as np

        words = self.vectorizer.get_feature_names()
        total_counts = np.zeros(len(words))
        for i, t in enumerate(self.vector):
            padding(len("* " + self.docs[i]), "-")
            print("*", self.docs[i])
            padding(len("* " + self.docs[i]), "-")
            total_counts = t.toarray()[0]
            count_dict = zip(words, total_counts)
            count_dict = sorted(count_dict, key=lambda x: x[1], reverse=True)[0:nWords]
            print_list(count_dict, message)
            print("\n")
        return count_dict

    def get_doc_topic_distrib(self):
        print("======================")
        print("DOC-TOPIC DISTRIBUTION")
        print("======================")
        jstr = ""
        nPad = 15
        ls = [" "] * (nPad - len("DOCS"))
        pad = jstr.join(ls)

        print("\nDocs", pad, "Topics")
        for n in range(self.transform.shape[0]):
            topic_most_pr = self.transform[n].argmax()

            ls = [" "] * (nPad - len(self.docs[n]))
            pad = jstr.join(ls)

            print(self.docs[n], pad, topic_most_pr + 1)
        print("\n")

    def get_vocabulary(self, nWords):
        from numpy import zeros as npz

        print("===========================")
        print("CORPUS VOCABULARY DISTRIBUTION")
        print("===========================")
        message = "Words\t\tCount"

        words = self.vectorizer.get_feature_names()
        total_counts = npz(len(words))
        for t in self.vector:
            total_counts += t.toarray()[0]

        count_dict = zip(words, total_counts)
        count_dict = sorted(count_dict, key=lambda x: x[1], reverse=True)[0:nWords]
        print_list(count_dict, message)
        print("\n")
        return self.vectorizer.vocabulary_

    def get_feature_space(self, data):
        from sklearn.feature_extraction.text import CountVectorizer

        vectorizer = CountVectorizer(stop_words="english")
        vector = vectorizer.fit_transform(data)
        return vector, vectorizer

    def LDA_transform(self, numberTopics):
        from sklearn.decomposition import LatentDirichletAllocation as LDA

        lda = LDA(n_components=numberTopics)
        transform = lda.fit_transform(self.vector)
        return transform, lda

    def save(self):
        import pickle as pkl
        from sys import getsizeof as size

        pickling_on = open("meta.zms", "wb")
        pkl.dump(self, pickling_on)
        pickling_on.close()
        print("[Data stored]", size(self) / 1024, "kb")
        pass
