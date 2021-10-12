from os.path import exists
from os import makedirs
import os.path
from shutil import copyfile


def open_s(fp, mode='r', encoding=None):
    f_dir = os.path.dirname(fp)
    if exists(f_dir):
        print("[#]Open file ", fp)
        return open(fp, mode=mode, encoding=encoding)

    print("[#]Making path ", f_dir)
    makedirs(f_dir)
    print("[#]Open file ", fp)
    return open(fp, mode=mode, encoding=encoding)


def get_all_files(fp):
    return [fp + fn for fn in get_all_files_name(fp)]


def get_all_files_name(fp):
    ff = []
    for root, dirs, files in os.walk(fp):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            ff.append(f)
    return ff


def copy_file(fp, fdir):
    fn = os.path.basename(fp)
    print("[#]Copy file ", fp, " to ", fdir + fn)
    copyfile(fp, fdir + fn)
    return 0


def copy_files(fps, fdir):
    for f in fps:
        copy_file(f, fdir)
    return 0


if __name__ == "__main__":
    print(get_all_files("D:\\nsfw\\sexy"))
