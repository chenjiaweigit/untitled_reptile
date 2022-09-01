#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
import ssl
import time
from urllib import request, parse

from Tool.tool import random_ua
from reptile.zhibo_reptile import test_csdn

ssl._create_default_https_context = ssl._create_unverified_context
"""
class TiebaSpider():
    #初始化url属性
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'

    def get_url(self,url):
        #请求方法重构
        req = request.Request(url,headers={'User-Agent':'%s'%(random_ua())})
        #请求体
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def save_file(self,filename,html):
        #保存文件函数
        with open(filename,'w') as f:
            f.write(html)

    def run_url(self):
        #运行主函数
        name = input('请输入贴吧名字：')
        start_page = int(input('请输入起始页：'))
        end_page= int(input('请输入终止页：'))
        for page in range(start_page,end_page+1):
            pn = (page-1)*50
            params = {
                'kw':name,
                'pn': pn
            }
            #请求参数编码
            params = parse.urlencode(params)
            #url地址拼接
            new_url = self.url.format(params)
            #发起请求
            html = self.get_url(new_url)
            filename = '{}-{}页.html'.format(name,page)
            self.save_file(filename,html)
            print('第%d页抓取成功'%page)

if __name__ == '__main__':
    start_time = time.time()
    test1 = TiebaSpider()
    test1.run_url()
    end_time = time.time()
    print('执行时间为：%.2fs'%(end_time-start_time))
"""


class brush_Traffic():
    #初始化url属性
    def __init__(self,):
        self.url = 'https://blog.csdn.net/qq_41648820/article/details/{}'

    def get_url(self,url):
        #请求方法重构
        req = request.Request(url,headers={'User-Agent':'%s'%(random_ua())})
        #请求体
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def save_file(self,filename,html):
        #保存文件函数
        with open(filename,'w') as f:
            f.write(html)

    def run_url(self):
        #运行主函数
        # name = input('请输入贴吧名字：')
        # start_page = int(input('请输入起始页：'))
        # end_page= int(input('请输入终止页：'))
        # for page in range(start_page,end_page+1):
        #     pn = (page-1)*50
        #     params = {
        #         'kw':name,
        #         'pn': pn
        #     }
        #     #请求参数编码
        #     params = parse.urlencode(params)
        #     #url地址拼接
        #     new_url = self.url.format(params)
            #发起请求
        try:
            for i in range(1,301):

                for num in range(len(test_csdn())):
                    pn = num+1
                    # 请求参数编码
                    params = parse.quote(test_csdn()[num])
                    #url地址拼接
                    new_url = self.url.format(params)
                    print(new_url)
                    self.get_url(new_url)
                    # filename = '{}-{}页.html'.format(name,page)
                    # self.save_file(filename,html)
                    # print('第%d页抓取成功'%page)
                    print("第%d轮执行完成" %i)
                    print("已发送请求%d条"%pn)
                print("等待时间60s")
                time.sleep(90)
                print("等待结束....")
        except "Not Found":
            print("Not Found")

if __name__ == '__main__':
    start_time = time.time()
    test1 = brush_Traffic()
    test1.run_url()
    end_time = time.time()
    print('执行时间为：%.2fs'%(end_time-start_time))