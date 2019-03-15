# -*- coding: utf-8 -*-

import os
import shutil
import hashlib

# 执行hugo生成页面
os.system('hugo')

# 复制public到docs文件夹中
source = './public'
target = './docs'

# 通过校验MD5 判断B内的文件与A 不同
def get_MD5(file_path):
    with open(file_path, "rb") as fd:
        fcont = fd.read()
    fmd5 = hashlib.md5(fcont)
    return fmd5

def main(path, out):
    for files in os.listdir(path):
        name = os.path.join(path, files)
        back_name = os.path.join(out, files)
        if os.path.isfile(name):
            if os.path.isfile(back_name):
                if get_MD5(name) != get_MD5(back_name):
                    shutil.copy(name, back_name)
            else:
                shutil.copy(name, back_name)
        else:
            if not os.path.isdir(back_name):
                os.makedirs(back_name)
            main(name, back_name)

if __name__ == '__main__':
    main(source, target)
    print("处理完成")
