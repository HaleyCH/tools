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
        print("[!]Image ", name, " failed.")
        print("[+]Resp status:", resp.status_code)
        return -1


def download_img_t(urls, fp, headers=None, t=1):
    while (len(urls) >= t):
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
    url = r"https://img-blog.csdn.net/20140613201350500?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveWl0b3VoYW4=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast"

    download_img(url, "D:/test/", "1.jpg")
