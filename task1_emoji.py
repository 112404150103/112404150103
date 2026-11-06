# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:35:31 2026

@author: 同载
"""
import requests

# =========函数1：获取图片二进制数据（可复用）=========
def get_image(url):
    # =========【红框标注1：定义请求信息】=========
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    timeout = 10
    try:
        # =========【红框标注2：发送请求并获得响应】=========
        r = requests.get(url, headers=headers, timeout=timeout)
        r.raise_for_status()   # 状态码非200抛出异常
        return r.content       # 返回图片二进制数据
    except Exception as err:
        print("图片请求出错：", err)
        return None

# =========函数2：保存图片到本地（可复用）=========
def save_image(save_path, img_bytes):
    if img_bytes is None:
        print("二进制数据为空，跳过保存")
        return
    # =========【红框标注3：将响应图片存储到本地】=========
    with open(save_path, "wb") as f:
        f.write(img_bytes)


if __name__ == "__main__":
    # 多张表情包url列表
    url_list = [
        "http://www.bspider.top/static/yh31/images/202008242134566465.gif",
        "http://www.bspider.top/static/yh31/images/202103302056530751.gif"
    ]
    # 循环下载每张图片
    for img_url in url_list:
        # 从url截取文件名
        file_name = img_url.split("/")[-1]
        save_file = file_name
        img_data = get_image(img_url)
        save_image(save_file, img_data)
        print(f"{save_file}下载完成")

