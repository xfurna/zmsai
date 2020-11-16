from os import walk, listdir
from zmsai.utils import series_to_list as stl


def read_txt(path="./custom"):
    files = []
    data = dict()
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend([str(dirpath) + "/" + i for i in filenames])
    fstream = list(map(open, files))
    txt = [i.read() for i in fstream]
    return txt


def read_csv(path="./custom/data.csv", sep=","):
    import pandas as pd

    files = pd.read_csv(path, delimiter=sep)
    txt = stl(files["text"])
    return txt
