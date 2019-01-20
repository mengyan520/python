import requests
import json
from pprint import pprint

if __name__ == '__main__':
    headers = {
        "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) " \
                      "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 " \
                      "Mobile/15A372 Safari/604.1"
    }
    count = 0
    # pprint(ret)
    # 保存json数据,先转python对象再保存，可以做一些其他操作，比如，指定编码格式
    while True:
        if count>40:
            break
        response = requests.get(
            'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start={'
            '}&count=18&loc_id=108288&_ '
            '=1547356905391'.format(count), headers=headers)
        json_str = response.content.decode()
        ret = json.loads(json_str)
        with open("douban{}.json".format(count), 'w') as f:
            # 关闭不用ascii编码保存，indent指定文本缩进
            f.write(json.dumps(ret, ensure_ascii=False, indent=2))
        count=count+18;

    pprint(json.load(open("douban0.json")))
