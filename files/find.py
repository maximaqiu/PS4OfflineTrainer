#!/usr/bin/env python
# _*_ coding: utf-8 _*_

'''
Author: Maximayau
Date: 2022/1/5 下午 3:38
ver: 1.0
desc: 
'''

import os
import json

def file_dir(path):
    return os.listdir(path)

def json_file(files):
    furl = []
    with open(files, encoding='UTF8') as f:
        dir_file = json.load(f)
    for i in dir_file['games']:
        furl.append(i['url'])
    return furl

def main():
    re_file = []
    # 当前目录
    curr_dir = file_dir('./')
    # 读取list文件里的url字段
    jfile = json_file('list.json')
    for i in curr_dir:
        # 如果list文件里的路径不存在当前目录就显示出来
        if i not in jfile:
            re_file.append(i)
    for j in re_file:
        print(j)
    print(f'总计:{len(re_file)}')




if __name__ == '__main__':
    main()
