import requests
import json
import sys


class BaiDuFanyi:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.lang_detect_str = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 ("
                                      "KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.loads(response.content.decode())

    def get_str(self, dict_response):
        ret = dict_response["trans"][0]["dst"]
        print("翻译结果：", ret)

    def run(self):
        lang_detect_data = {"query": self.trans_str}
        lang = self.parse_url(self.lang_detect_str, lang_detect_data)["lan"]
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == "zh" else {"query": self.trans_str,
                                                                                               "from": "en", "to": 'zh'}
        dict_response = self.parse_url(self.trans_url, trans_data)
        self.get_str(dict_response)


if __name__ == '__main__':
    trans_str = "你好"
    if len(sys.argv) > 1:
        trans_str = sys.argv[1]

    fanyi = BaiDuFanyi(trans_str)
    fanyi.run()
