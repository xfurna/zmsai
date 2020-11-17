def series_to_list(obj):
    return list(obj)


def countFiles(DIR):
    from os import listdir

    try:
        lsdir = listdir(DIR)
        count = len(lsdir)
    except:
        count, lsdir = 0, 0

    return count, lsdir


def print_topics(model, vectorizer, nWords):
    print("=======================")
    print("TOPIC-WORD DISTRIBUTION")
    print("=======================")
    words = vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print(
            "Topic %d:\t" % (topic_idx + 1),
            " | ".join([words[i] for i in topic.argsort()[: -nWords - 1 : -1]]),
        )
    print("\n")


def print_list(dct, message):
    print(message)
    print("---------------------")
    for i in dct:
        jstr = ""
        nPad = 15
        ls = [" "] * (nPad - len(i[0]))
        pad = jstr.join(ls)
        print(i[0], pad, i[1])


def padding(size, symb="="):
    jstr = ""
    ls = [symb] * size
    print(jstr.join(ls))
