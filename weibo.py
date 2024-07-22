import requests
import signal
from lxml import etree
from flask import Flask
from jinja2 import Template
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

Header = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Cookie": "SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5mn0qIGILEoWGL_I_WJDvX; SINAGLOBAL=7316900708533.683.1694859572493; SUB=_2AkMSW6cIf8NxqwJRmP8cy23naYRyyAHEieKkB1bTJRMxHRl-yj9kqk5TtRB6OduJ5w3Idvr6fe9jkFzmgNdlXUuTonpp; UOR=localhost:5000,s.weibo.com,localhost:5000; _s_tentry=-; Apache=5882601969292.636.1704349065829; ULV=1704349065837:3:3:3:5882601969292.636.1704349065829:1704252936013",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def get_html(url) -> str:
    response = requests.get(url, headers=Header)
    response.encoding = 'utf-8'
    return response.text


def parse_html(html) -> list:
    # 创建etree对象
    html = etree.HTML(html)
    # 获取所有a标签
    tr_list = html.xpath("//div[@id='pl_top_realtimehot']/table/tbody//tr")
    import time
    data = []

    for tr in tr_list:
        index = tr.xpath("./td[contains(@class,'td-01')]/text()")[0] if tr.xpath(
            "./td[contains(@class,'td-01')]/text()") else ""
        href = tr.xpath("./td[@class='td-02']/a/@href")[0]
        text = tr.xpath("./td[@class='td-02']/a/text()")[0]
        span = tr.xpath("./td[@class='td-02']/span/text()")[0] if tr.xpath(
            "./td[@class='td-02']/span/text()") else ""
        hot = tr.xpath("./td[@class='td-03']/i/text()")[0] if tr.xpath(
            "./td[@class='td-03']/i/text()") else ""
        text = f"<a class='link-success link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover' href='https://s.weibo.com{href}' target='_blank'>{text}</a>"

        strings = "{} {} {} {}".format(index, text, span, hot)
        data.append(strings)
    return data


def exit_gracefully(signum, frame):
    import sys
    sys.exit()


@app.get('/')
def index() -> str:
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    template = Template(
        '<link href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/5.3.3/css/bootstrap.min.css" rel="stylesheet">'
        '<script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/5.3.3/js/bootstrap.bundle.min.js"></script>'
        "<div class='container table-responsive' style='text-align:center;display:flex;align-items: center;'><table class='table mx-auto table-borderless'><tbody>{% for line in lines %}<tr class='row text-center'><td class='col-12' style='color:#0180a5'>{{line}}</td></tr><tr>{% endfor %}</tbody></table></div>")
    content = parse_html(get_html(url))
    return template.render(lines=content)


if __name__ == "__main__":
    http_server = WSGIServer(("0.0.0.0", 5000), app)
    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGTERM, exit_gracefully)
    http_server.serve_forever()
