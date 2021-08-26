import requests
import threading
from safe_open import open_s
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
    while len(urls) >= t:
        k = None
        for i in range(t):
            url = urls.pop()
            name = url.split("/")[-1]
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
    with open_s("D:\\nsfw_url_data\\sexy\\urls_sexy.txt") as r_obj:
        urls = r_obj.read().split("\n")[20:]
        # urls.reverse()

    download_img_t(urls, "D:/nsfw/sexy/", t=5)
