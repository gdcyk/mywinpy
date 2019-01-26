# coding: utf-8

import sys
import os
import time

# shutdown computer after time_diff seconds
def shutdown(seconds):
    print(str(seconds) + u' 秒后将会关机...')
    time.sleep(seconds)
    print(u'关机啦。。。')
    os.system('shutdown -s -f -t 1')
