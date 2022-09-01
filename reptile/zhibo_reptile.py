#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import os
import random
import re
import ssl
import time
from urllib import request
from urllib import parse

import requests
# from bs4 import BeautifulSoup

from Tool.tool import random_ua
context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context
"""
# 定义变量：URL 与 headers
url = 'http://zhibohui-yizhangtu-web.gago.top:30724/get'
#重构请求头，伪装成 Mac Chrome浏览器访问，可以使用上表中任意浏览器的UA信息
headers = {
    'Content-Type': 'application/json;charset=utf-8',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 1、创建请求对象，包装ua信息
req = urllib.request.Request(url=url,headers=headers)
# 2、发送请求，获取响应对象
res = urllib.request.urlopen(req)
# response = urllib.request.urlopen('http://zhibohui-yizhangtu-web.gago.top:30724/get')
# 3、提取响应内容
html = res.read().decode('utf-8')
# print(html)

'''response=urllib.request.urlopen('http://httpbin.org/get')
html = response.read().decode()
print(html)'''
"""

def url_coding():
    '''
    字符串编码
    :return:
    '''
    #构建查询字符串字典
    query_string = {
    'wd' : '爬虫'
    }
    #调用parse模块的urlencode()进行编码
    result = parse.urlencode(query_string)
    #使用format函数格式化字符串，拼接url地址
    url = 'http://www.baidu.com/s?{}'.format(result)

    #注意url的书写格式，和 urlencode存在不同
    url = 'http://www.baidu.com/s?wd={}'
    word = '爬虫'
    #quote()只能对字符串进行编码
    result1 = parse.quote(word)
    return url.format(result1)

def url_decode():
    '''
    字符串解码
    :return:
    '''
    new_url_coding = re.compile(r'wd=(.*)').findall(url_coding())[0]
    return parse.unquote(new_url_coding)

def test_baidu():
    '''
    爬取百度页面保存到本地
    :return:
    '''
    url = 'https://www.so.com/s?q={}'
    word = input('请输出要查询的内容：')
    #使用quote()对查询内容进行加密
    params = parse.quote(word)
    #查询内容拼接到url
    new_url = url.format(params)
    headers = {'User-Agent':'%s'%(random_ua())}
    ssl._create_default_https_context = ssl._create_unverified_context
    #重构请求头
    req = request.Request(url=new_url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # print(html)
    filename = word+'.html'
    # 保存文件到本地
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

def test_xh():
    i = 0
    while i<=450:
        print(i)
        i+=50

# if __name__ == '__main__':
#     start_time=time.time()
#     test_baidu()
#     end_time=time.time()
#     print('耗时：{}'.format(end_time-start_time))

def regular_test():
    html="""
    <div><p>www.biancheng.net</p></div>
    <div><p>编程帮</p></div>
    """
    #贪婪匹配，re.S可以匹配换行符
    #创建正则表达式对象
    pattern=re.compile('<div><p>.*</p></div>',re.S)
    #匹配HTMLX元素，提取信息
    re_list=pattern.findall(html)
    print(re_list)
    #非贪婪模式匹配，re.S可以匹配换行符
    pattern=re.compile('<div><p>.*?</p></div>',re.S)
    re_list=pattern.findall(html)
    print(re_list)


def regular_test1():
    html = """
    <div class="movie-item-info">
    <p class="name">
    <a title="你好，李焕英">你好，李焕英</a>
    </p>
    <p class="star">
    主演：贾玲,张小斐,沈腾
    </p>    
    </div>
    <div class="movie-item-info">
    <p class="name">
    <a title="刺杀，小说家">刺杀，小说家</a>
    </p>
    <p class="star">
    主演：雷佳音,杨幂,董子健,于和伟
    </p>    
    </div> 
    """
    # 寻找HTML规律，书写正则表达式，使用正则表达式分组提取信息
    pattern = re.compile(r'<div.*?<a title="(.*?)".*?star">(.*?)</p.*?div>', re.S)
    r_list = pattern.findall(html)
    # print(r_list)
    # 整理数据格式并输出
    if r_list:
        for r_info in r_list:
            print("影片名称：", r_info[0])
            print("影片主演：", r_info[1].strip())
            print(20 * "*")
    # path = os.path.dirname(os.path.dirname(__file__))
    # file = open(path+'/data/test_data.html','rb')
    # new_html = file.read()
    # bs = BeautifulSoup(new_html,"html.parser")
    # print(bs.meta)

def test_csdn():
    '''
    爬取百度页面保存到本地
    :return:
    '''

    # filename = 'csdn'+'.html'
    # # 保存文件到本地
    # with open(filename,'w',encoding='utf-8') as f:
    #     f.write(html)
    filename = os.path.dirname((os.path.dirname(__file__)))+'/data/data_File.json'
    with open(filename,"r") as f:
        data = f.read()
    url1 = re.compile(r'"articleId": "(.*?)",',re.S)
    csdn_url = url1.findall(data)
    return csdn_url


