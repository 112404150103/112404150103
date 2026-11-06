# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:14:11 2026

@author: 同载
"""

import requests
from urllib import parse

# 可复用函数：查询手机号归属地，并且保存网页源码到本地html
def query_phone(phone_number, save_html_name):
    # =========【红框标注1：定义请求信息】=========
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    timeout = 10
    # GET请求参数字典
    param_dict = {
        "mobile": phone_number,
        "action": "mobile"
    }
    # 将字典转为url查询字符串
    param_str = parse.urlencode(param_dict)
    base_url = "https://www.ip138.com/mobile.asp?"
    full_url = base_url + param_str

    try:
        # =========【红框标注2：发送请求并获得响应】=========
        r = requests.get(full_url, headers=headers, timeout=timeout)
        r.raise_for_status()
        # 处理中文乱码，教材3.5案例
        r.encoding = r.apparent_encoding
        html_text = r.text

        # =========【红框标注3：将响应存储到本地html】=========
        with open(save_html_name, "w", encoding="utf-8") as f:
            f.write(html_text)
        print(f"网页源码已经保存到 {save_html_name}")

    except Exception as err:
        print("手机号查询请求出错：", err)


if __name__ == "__main__":
    # 填入你自己真实手机号！！！
    my_phone = "19741881785"
    query_phone(my_phone, "phone_result.html")
