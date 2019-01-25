# _*_ coding:utf-8 _*_

# !/usr/bin/env python
# Version = 3.5.2
# __auth__ = '无名小妖'

# psutil = process and system utilities
# 它不仅可以通过一两行代码实现系统监控，
# 还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，
# 是系统管理员和运维小伙伴不可或缺的必备模块。
import psutil
import collections
import os

GB = 1024 ** 3
MB = 1024 ** 2
KB = 1024 ** 1

def get_disk_info():
    """
    查看磁盘属性信息
    :return: 磁盘使用率和剩余空间 字符串 字典
    """
    disk_used = collections.OrderedDict()  # 有顺序的字典
    for id in psutil.disk_partitions():  # 获取分区信息
        # id: ('device':设备名, 'mountpoint':计算起始点, 'fstype':磁盘类型, 'opts':选项)
        # cdrom：CD-ROM
        if 'cdrom' in id.opts or id.fstype == '':
            continue
        disk_name = id.device.split(':')
        s = disk_name[0]
        disk_info = psutil.disk_usage(id.device)  # disk_usage 磁盘使用率
        disk_used[s + '盘使用率：'] = '{}%'.format(disk_info.percent)  # percent 使用百分百
        disk_used[s + '剩余空间：'] = '{}GB'.format(disk_info.free // 1024 // 1024 // 1024)  # free 可用空间,单位byte
    return disk_used


def get_disk_free(device:str):
    """
    获取对应盘符的剩余空间
    :param device: 硬盘盘符 'C', 'D', 'E', 'F', 'G'...
    :return: 空间大小 单位GB
    """
    key = device + '剩余空间：'
    disk_used = get_disk_info()
    free = float(disk_used[key].split('GB')[0])
    return free


def display_byte_type(size:int):
    """
    将字节转化为 KB MB GB
    :param size: 输入字节(byte 8个位bit)大小
    :return:
    """
    if size > 1024 * 1024 * 1024:
        return '{} GB'.format(str(size / GB))
    elif size > 1024 * 1024:
        return '{} MB'.format(str(size / MB))
    elif size > 1024:
        return '{} KB'.format(str(size / KB))


def getFileSize(filePath):
    """
    获取文件夹大小
    :param filePath: 输入文件夹路径
    :return: 文件夹大小 单位Byte字节
    """
    # 作者：Always0nTheWay
    # 来源：CSDN
    # 原文：https://blog.csdn.net/wukai_std/article/details/54946636
    # 版权声明：本文为博主原创文章，转载请附上博文链接！
    size = 0
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            print(f)
    return size

if __name__ == '__main__':
    print(display_byte_type(getFileSize("D:/PythonProject/mywinpy/dist")))