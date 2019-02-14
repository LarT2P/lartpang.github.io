# todo:
#   有时间一定要尝试写一个markdown解析器
#   需要把更新的部分合并进来

import markdown
import os
import argparse

# 处理命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("target", help="处理文件(夹)", type=str)

# https://blog.csdn.net/p_lart/article/details/55819896
html = '''
<html lang="zh-cn">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<link href="tools/asserts/css/default.css" rel="stylesheet">
<link href="tools/asserts/css/html.css" rel="stylesheet"></link>
</head>
<body>
%s
</body>
</html>
'''

exts = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.admonition',
    'markdown.extensions.toc', ]

def main(args):
    input_path = os.path.join('..', args.target)
    print(input_path)
    output_path = '..'
    if os.path.isdir(input_path):
        # 输入为目录
        input_files = os.listdir(input_path)
        for input_file in input_files:
            ifile_path = os.path.join(
                input_path,
                input_file)
            ofile_path = os.path.join(
                output_path,
                input_file.replace('.md', '.html'))

            with open(ifile_path, mode='r', encoding='utf-8') as ifile:
                itext = ifile.read()
                body = markdown.markdown(itext, extensions=exts)
            with open(ofile_path, mode='w', encoding='utf-8') as ofile:
                ofile.write(html % body)
    elif os.path.isfile(input_path):
        # 输入为文件
        ifile_path = input_path
        ofile_path = os.path.join(
            output_path,
            input_path.replace('.md', '.html').split(os.sep)[-1])

        with open(ifile_path, mode='r', encoding='utf-8') as ifile:
            itext = ifile.read()
            body = markdown.markdown(itext, extensions=exts)
        with open(ofile_path, mode='w', encoding='utf-8') as ofile:
            ofile.write(html % body)
    else:
        print("参数异常")


if __name__ == "__main__":
    main(parser.parse_args())