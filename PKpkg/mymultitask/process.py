# _*_ coding:utf-8 _*_

from multiprocessing import Process, Queue
import json
import sys
import glob
import os
from PKpkg.myfileprocessing.file import myjoin

class MyBaseProcess():
    def __init__(self, filename:str, num_worker:int, maxsize:int=100):
        self.num_worker = num_worker
        self.content_list_file = filename
        self.end = False
        self.queue = Queue(maxsize=maxsize)  # 队列大小

    def get_content_list(self):
        with open(self.content_list_file, 'r') as js:
            self.json_dict = json.load(js)

    # 将导航目录加入队列，防止多进程重复处理同一个文件
    def put_data_to_queue(self):
        name = sys._getframe().f_code.co_name
        raise NotImplementedError('{} is not Implemented.'.format(name))
        self.end = True

    # 处理文件的函数，也是进程
    def cope_data(self):
        name = sys._getframe().f_code.co_name
        raise NotImplementedError('{} is not Implemented.'.format(name))
        pass

    # 运行
    def run(self):
        load_data_list = Process(target=self.put_data_to_queue())
        load_data_list.start()

        ps = []
        # 创建子进程实例
        for i in range(self.num_worker):
            p = Process(target=self.cope_data, name="cope_data" + str(i), args=())
            ps.append(p)

        # 开启进程
        for i in range(self.num_worker):
            ps[i].start()

        # 阻塞进程
        for i in range(self.num_worker):
            ps[i].join()

        print("主进程终止")


