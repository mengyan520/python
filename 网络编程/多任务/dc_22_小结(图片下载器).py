import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_url, file_name):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(file_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "http://rpic.douyucdn.cn/live-cover/"
                                 "appCovers/2018/11/17/1241123_20181117100024_small.jpg", "1.jpg"),
        gevent.spawn(downloader, "http://rpic.douyucdn.cn/live-cover/appCovers/"
                                 "2018/11/16/5104546_20181116011659_small.jpg", "2.jpg")
    ])


if __name__ == '__main__':
    main()
