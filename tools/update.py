# 将生成的html移动到外层文件夹.
# 但是不会移动index.html, 因为流程不同, 需要重新生成index.html, 再移动到父文件夹.

import os
import re
import shutil

md_path = os.path.join('..', 'md')
html_path = '..'
with open(os.path.join(md_path, 'index.md'), 'r', encoding='UTF-8') as index_md:
    content_md = index_md.readlines()

list_articles = []
for i, raw_md in enumerate(content_md):
    if '* [' in raw_md:
        start_i = i
        list_articles.append(re.findall('\[(.*?)\]', raw_md)[0])

md_set = set([x.split('.')[0] for x in os.listdir(md_path)])
other_set = set(['index'])
md_set = md_set - other_set
list_set = set(list_articles)

if md_set == list_set:
    print("文档已为最新")
else:
    print("文档已有更新")
    update_file = list(md_set - list_set)
    print(update_file)

    for file_md in update_file:
        with open(os.path.join(md_path, 'index.md'), 'a', encoding='UTF-8') as index_md:
            # * [生活-论文&代码&生活](./生活-论文&代码&生活.html)
            new_line = f"* [{file_md}](./{file_md}.html)\n"
            print(new_line)
            index_md.write(new_line)

        shutil.move(
            os.path.join(md_path, file_md + '.html'),
            os.path.join(html_path, file_md + '.html'))

if 'index.html' in os.listdir(md_path):
    print('更新index.html')
    shutil.move(
        os.path.join(md_path, 'index.html'),
        os.path.join(html_path, 'index.html'))
