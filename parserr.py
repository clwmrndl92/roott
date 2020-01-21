# parser.py
import requests
from bs4 import BeautifulSoup


def parsing(num):
    # HTTP GET Request
    req = requests.get("https://www.acmicpc.net/problem/" + str(num))
    # HTML 소스 가져오기
    html = req.text
    # BeautifulSoup으로 html소스를 python객체로 변환하기
    # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    # 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html.parser')

    title_data = soup.find('h1').get_text()
    title_data_ = title_data[:title_data.find('\n')]
    data = soup.find(id = 'problem-body').get_text()
    end=data.find("힌트")
    data = data[:end]
    data_list = data.split("\n")
    data_ = ""

    for i in data_list:
        if i != "":
            data_ += i + "\n"

    return title_data + data_

