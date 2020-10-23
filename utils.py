def series_to_list(obj):
    return list(obj)


def countFiles(DIR):
    from os import listdir

    count = len([name for name in listdir(DIR)])
    return count
