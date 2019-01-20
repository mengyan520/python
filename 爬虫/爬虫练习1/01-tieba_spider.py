import requests


class Tieba_Spider(object):
    def __init__(self, name):
        self.name = name
        self.temp_url = "https://tieba.baidu.com/f?kw=" + name + "&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                      "like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    def get_url_list(self):
        return [self.temp_url.format(i * 50) for i in range(5)]

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def sava_content(self, content, index):
        file_name = "{}--第{}页".format(self.name, index)
        with open(file_name, 'w') as f:
            f.write(content)

    def run(self):
        print(self.get_url_list())
        for url in self.get_url_list():
            content = self.parse_url(url)
            self.sava_content(content, self.get_url_list().index(url))


if __name__ == '__main__':
    tieba = Tieba_Spider("lol")
    tieba.run()
