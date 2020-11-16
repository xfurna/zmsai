def test_run():
    import zmsai.LDA as lda
    import zmsai.base as base

    distributions = lda.heuristics(path=base.path, numberTopics=6)
    distributions.get_doc_topic_distrib(base.defdocs)
    distributions.get_topic_word_distrib(5)
    distributions.get_doc_word_distrib(base.defdocs, 5)
    distributions.get_vocabulary(base.defdocs, 5)
    assert 1
