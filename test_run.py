def test_run():
    import zmsai

    distributions = zmsai.LDA.heuristics(path=zmsai.base.path, numberTopics=6)
    distributions.get_doc_topic_distrib(zmsai.base.docs)
    distributions.get_topic_word_distrib(5)
    distributions.get_doc_word_distrib(zmsai.base.docs, 5)
    distributions.get_vocabulary(zmsai.base.docs, 5)
    assert 1