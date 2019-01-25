# _*_ coding:utf-8 _*_

import os,shutil

def myjoin(*args):
    desdir = ''
    for item in args:
        desdir = desdir + item
        if item[-1] is not '/' and item.find('.') == -1:
            desdir += '/'
    return desdir

def movefile(srcfile:str, dstfile:str):
    """
    移动文件
    :param srcfile:源文件详 细位置
    :param dstfile: 目标文件 详细位置
    :return:
    """
    if not os.path.isfile(srcfile):
        print("{} not exist!".format(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print("move %s -> %s"%(srcfile, dstfile))


def copyfile(srcfile,dstfile):
    """
    复制文件
    :param srcfile: 源文件位置
    :param dstfile: 目标文件位置
    :return:
    """
    if not os.path.isfile(srcfile):
        print("{} not exist!".format(srcfile))
    else:
        fpath, fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy %s -> %s"%( srcfile, dstfile))


def findfile(file_dir, old_post, new_post, lis):
    """
    将目录及其子目录下的后缀为 old的后缀-> new的后缀
    :param file_dir:文件目录
    :param old_post:旧后缀
    :param new_post:新后缀
    :param lis:空列表，用来存储被修改文件名
    :return:
    """
    ls = os.listdir(file_dir)
    for i in ls:
        child_path = os.path.join(file_dir, i)
        # 判断是不是有子目录，有就递归进入搜寻
        if os.path.isdir(child_path):
            findfile(child_path, old_post, new_post, lis)
        else:
            file_post = str(i.split('.')[-1])
            if file_post == old_post:
                lis.append(i)
                os.rename(child_path, str(child_path.split('.')[0])+'.'+new_post)
                print('找到文件{srcnam},已修改成:{dicname}'
                      .format(srcnam=child_path, dicname=str(i.split('.')[0]) + '.' + new_post))
    return lis