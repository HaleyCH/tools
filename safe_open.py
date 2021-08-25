from os.path import exists
from os import makedirs


def open_s(fp, mode='r', encoding=None):
    f_dir = "/".join(("/".join(fp.split("\\"))).split("/")[:-1])
    if exists(f_dir):
        print("[#]Open file ", fp)
        return open(fp, mode=mode, encoding=encoding)

    print("[#]Making path ", f_dir)
    makedirs(f_dir)
    print("[#]Open file ", fp)
    return open(fp, mode=mode, encoding=encoding)


if __name__ == "__main__":
    a = open_s("D:/notMNIST_large/qq/aaa/s/a2FkZW4udHRm.png", mode="wb")
    print(a)
    a.close()
