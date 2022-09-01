#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random

from fake_useragent import UserAgent


def random_num(min_num,max_num):
    '''
    生成随机数
    :return:
    '''
    # print(30+round(random.uniform(0,5),2),40+round(random.uniform(0,5),2))
    # print(32 + round(random.uniform(0, 5), 2), 41 + round(random.uniform(0, 5), 2))
    return random.randint(min_num,max_num)

# print(random_num(0,4))

def random_ua():
    '''
    随机获取一个ie、Chrome、Firefox、Safari浏览器UA
    :return:
    '''
    #实例化一个对象
    ua=UserAgent()
    ua=UserAgent(verify_ssl=False)
    # ua = UserAgent(use_cache_server=False)
    # ua = UserAgent(path="./fake_useragent_0.1.11.json")
    # 随机获取一个ie、Chrome、Firefox、Safari浏览器ua
    if random.choice(("ie","Chrome","firefox","Safari")) == "ie":
        return (ua.ie)
    elif random.choice(("ie","Chrome","firefox","Safari")) == "Chrome":
        return (ua.Chrome)
    elif random.choice(("ie","Chrome","firefox","Safari")) == "firefox":
        return (ua.firefox)
    else:
        return (ua.Safari)

