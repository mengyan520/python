import requests

if __name__ == '__main__':
    proxies = {
        "http": "http://222.246.120.37"
    }
    response = requests.get("http://www.baidu.com", proxies=proxies,headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                      "like Gecko) Chrome/54.0.2840.99 Safari/537.36"})
    print(response.status_code)
