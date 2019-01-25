# _*_ coding:utf-8 _*_

from pytube import YouTube
import os

def youtube(url:str, path, filename=None):
    """
    使用pytube下载youtube 视频，需要翻墙
    :param url: YouTube 视频链接
    :param path: 要下载到的位置
    :param filename: 文件名（可选）
    :return:
    """
    if not os.path.exists(path):
        os.mkdir(path)
    yt = YouTube(url)
    if filename:
        yt.streams.first().download(path, filename=filename)  # 默认下载清晰度最高的视频
    else:
        yt.streams.first().download(path)  # 默认下载清晰度最高的视频