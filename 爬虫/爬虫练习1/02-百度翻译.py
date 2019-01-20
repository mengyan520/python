import requests
import json

if __name__ == '__main__':
    headers = {
        "Host": "fanyi.baidu.com",
        "Connection": "keep-alive",
                      "Content-Length": "122",
                                        "Accept": "*/*",
    "Origin": "https://fanyi.baidu.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "BAIDUID=F885488890077AB97E794420E143F231:FG=1; BIDUPSID=F885488890077AB97E794420E143F231; PSTM=1524569202; " \
              "FP_UID=fac72dc110ddac5aa1f7fd567f7d9b15; pgv_pvi=523676672; delPer=0; H_PS_PSSID=1451_21105_28132_28267_27244;" \
              " FEED_SIDS=489364_0111_22; SE_LAUNCH=5%3A25786993_0%3A25786993; " \
              "H_WISE_SIDS=125703_125819_100806_126755_128070_127492_120136_123018_128638_122155_126009_118886_118877_118856_118832_118786_127181_128038_128364_107311_126995_127771_127405_" \
              "127768_117331_128449_117430_128451_128819_128402_127835_128589_127808_127026_128791_128497_128246_128805_127797" \
              "_126720_128528_127873_127764_128240_124030_128341_110085_124869_123289_128763_127315_127380_128600_128195; " \
              "PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1547257629;" \
              " Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1547257629; " \
              "to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value" \
              "%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; " \
              "HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; " \
              "from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E" \
              "2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D"
    }
    formdata = {"from": "en",
                "to": "zh",
                "query": "I Love you",
                "transtype": "translang",

                "simple_means_flag": "3",
                "sign": "944017.689312",
                "token": "c74e2104b466f2192291a411dd610445"
                }
    url = "https://fanyi.baidu.com/v2transapi"
    response = requests.post(url, data=formdata, headers=headers)
    trans_result = json.loads(response.content.decode())
    content = trans_result["trans_result"]["data"][0]["dst"]

    print("翻译结果：", content)
