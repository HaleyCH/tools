import sys

import requests
import threading
from safe_open import open_s, get_all_files_name
from my_fake_useragent import UserAgent as UA
from time import sleep
import random


def download_img(url, fp, name, headers=None):
    if not headers:
        headers = {}
        ua = UA()
        user = ua.random()
        headers["User-Agent"] = user
    print("[#]Getting ", name, " from ", url)
    resp = requests.get(url, headers=headers)
    f_path = "/".join(("/".join(fp.split("\\"))).split("/")[:-1]) + "/" + name
    try:
        with open_s(f_path, "wb") as f_obj:
            f_obj.write(resp.content)
        print("[#]Image ", name, " was successfully downloaded.")
        return 0
    except:
        print("[!]Writing image ", name, " failed.")
        # print("[+]Resp status:", resp.status_code)
        return -1


def download_img_t(urls, fp, headers=None, t=1):
    finished_imgs = get_all_files_name(fp)
    while len(urls) >= t:
        k = None
        for i in range(t):
            url = urls.pop()
            name = url.split("/")[-1].replace("\\", "").replace("/", "")
            while urls and name in finished_imgs:
                print("[!]Image ", name, " has been already downloaded,pass.")
                url = urls.pop()
                name = url.split("/")[-1].replace("\\", "").replace("/", "")
            k = threading.Thread(target=download_img, args=(url, fp, name,), kwargs={"headers": headers})
            k.start()
            sleep(random.random())
        k.join(10)
    for url in urls:
        name = url.split("/")[-1]
        k = threading.Thread(target=download_img, args=(url, fp, name,), kwargs={"headers": headers})
        k.start()
        sleep(random.random())
        k.join(10)


if __name__ == "__main__":
    fp, out = sys.argv[0], sys.argv[1]
    if len(sys.argv) < 3:
        t = 5
    else:
        t = sys.argv[2]
    with open_s(fp) as r_obj:
        urls = r_obj.read().split("\n")[20:]
        # urls.reverse()

    download_img_t(urls, out, t)
