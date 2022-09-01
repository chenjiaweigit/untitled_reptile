#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests,json
import random
from urllib import request

def read_interface_data(url,data):
    '''
    :param url:
    :param data:
    :return:
    '''
    url1 = url
    data = data
    header = {'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjgxNTk4NzliLTg3MzMtNDhlYy05OTljLTQ3Yjc3OWI5NGJmZSJ9.yJ84YL5sl12QFoeTvW312SvPhi-hgiGu6BSgHE-eMh81aS8DNwnpJn7_0Ssm22V1ycsoYnliOrSH75dL6fh3RA'}
    a = requests.post(url=url1, json=data, headers=header)
    # print(a.json()['rows'][0]['area'])
    b = 0
    for i in range(0, 999):
        b += a.json()['rows'][i]['area']
        # print(a.json()['rows'][i]['area'])
    print(b)
    #     # json_str = str.replace("'",'"')
    #     # print(a.json())
    #     # dict2 = a.text
    #     # json_dict = json.loads(dict2)
    #     # print(json_dict['rows'])

url2 = ' http://chongqing-agri-industry.gago.top:31882/system/b_lands_attribute/lands/list'
data2 = {"year":2021,"slope":[0,20],"crop":"冬水田","code":None,"altitude":[300,600],"pageNum":1,"pageSize":1000}
# read_interface_data(url=url2,data=data2)

def json_data():
    path = '/Users/chenjiawei/Desktop/公司文档/佳格项目/重庆农业产业数字化地图/优质基地信息_v2.json'
    with open(path,"r") as f:
        row_data = json.load(f)
    b = 0
    for i in range(0,55):
        if (row_data[i]['name'] == '新阳大米基地' or row_data[i]['name'] == '坪天一口香优质大米基地' or row_data[i]['name'] == '大阳米基地'):
            b+=row_data[i]['ability']
            print(row_data[i]['ability'])
    print(b)

def read_excel(path):
    path = path
    # with open(path,"r") as f:
        # read_excel1

#
# def pa_url_data():
#     '''
#     :param url:
#     :param data:
#     :return:
#     '''
#     url = 'http://zhibohui-yizhangtu-web.gago.top:30724/big-screen/quality-base'
#     url_data = request.Request(url)
#     # 获取响应对象
#     res = request.urlopen(url_data)
#     # 获取响应内容
#     html = res.read().decode("utf-8")
#     filename = 'test' + '.html'
#     with open('/Users/chenjiawei/Desktop/automation/爬虫', 'w', encoding='utf-8') as f:
#         f.write(html)

'''
from urllib import request,parse
# 1.拼url地址
# url = 'http://www.baidu.com/s?wd={}'
url = 'http://zhibohui-yizhangtu-web.gago.top:30724/big-screen/quality-base'
# word = input('请输入搜索内容:')
# params = parse.quote(word)
# full_url = url.format(params)
# 2.发请求保存到本地
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')
# 3.保存文件至当前目录
# filename = '/Users/chenjiawei/Desktop/automation/pa/'+ word + '.html'
filename = '/Users/chenjiawei/Desktop/automation/pa/'+ 'test'+'.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)
'''

def jiekou_test():
    '''

    :return:
    '''
    url1 = 'http://chongqing-agri-industry.gago.top:31882/system/b_lands_attribute/lands/list'
    data1 = {"year":2021,"slope":[0,19],"crop":"冬水田","code":None,"altitude":[0,600],"pageNum":1,"pageSize":1000}
    header = {'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImZiOTk4MDVjLTI2MGUtNGEzNC04OTE0LWZmMDA3M2RlMzM1NyJ9.VQCPd0hiAGBIpv6pPP51gn6PWC8lMPfcs8AJnofkfvFOW1wx2jJ_UF1LIZchxzsc0cje7LFK2n24ygIxgNmbiw'}
    response = requests.post(url=url1,json=data1,headers=header)
    print(response.json()['total'])

# jiekou_test()

from seleniumwire import webdriver

def url_get():
    driver = webdriver.Chrome()
    driver.get('http://zhibohui-yizhangtu-web.gago.top:30724/big-screen/winter-paddy-field')
    for request in driver.requests:
        if request.response:
            print("url:",request.url)
    driver.quit()


def random_num():
    '''
    生成随机数
    :return:
    '''
    print(30+round(random.uniform(0,5),2),40+round(random.uniform(0,5),2))
    print(32 + round(random.uniform(0, 5), 2), 41 + round(random.uniform(0, 5), 2))
# random_num()

from seleniumwire import webdriver

def jiekou():

    url = 'http://zhibohui-yizhangtu-web.gago.top:30724/big-screen/rice-remote-sensing-monitoring'
    test = webdriver.Chrome()
    test.get(url)
    for request in test.requests:
        if request.response:
            print(request.url)

