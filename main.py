# 签到、抽奖
import sys
import requests
# 签到
URL = "https://api.juejin.cn/growth_api/v1/check_in?aid=2606"
# 首次抽奖
LOTTERY = 'https://api.juejin.cn/growth_api/v1/lottery/draw?aid=2600'
api_list = [URL, LOTTERY]
herder = {
    'referer': 'https://juejin.cn/',
    'origin': 'https://juejin.cn',
    'content-type': 'application/json; charset=utf-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'cookie': sys.argv[1]
}


def access_check_in():
    """
    签到
    :return:
    """
    for api in api_list:
        resp = requests.post(url=api, headers=herder)
        if resp.status_code == 200:
            print('请求成功')
            print(resp.text)


if __name__ == '__main__':
    access_check_in()
