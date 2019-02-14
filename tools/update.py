# 将生成的html移动到外层文件夹.
# 但是不会移动index.html, 因为流程不同, 需要重新生成index.html, 再移动到父文件夹.

import os
import re
import shutil

print('更新文本内容')
dir_name = 'md'
os.system(f"python converter.py {dir_name}")

# 获得index.md中的已有文件列表
md_path = os.path.join('..', 'md')
html_path = '..'
with open(os.path.join(md_path, 'index.md'), 'r', encoding='UTF-8') as index_md:
    content_md = index_md.readlines()

list_articles = []
for i, raw_md in enumerate(content_md):
    if '* [' in raw_md:
        start_i = i
        list_articles.append(re.findall('\[(.*?)\]', raw_md)[0])

# 获得md文件夹中的文件列表, 这个使用的是.html文件生成到md文件夹里的情况
# todo: 这里需要更改为符合现在的文件生成方式
html_names = [x for x in os.listdir('..')  \
    if os.path.isfile(os.path.join('..', x)) and x.endswith('.html')]
html_set = set([x.split('.')[0] for x in html_names])

other_set = set(['index'])
md_set = html_set - other_set
list_set = set(list_articles)

if md_set == list_set:
    print("文档已为最新")
else:
    print("文档已有更新")
    update_file = list(md_set - list_set)
    print(update_file)

    for file_md in update_file:
        with open(os.path.join(md_path, 'index.md'), 'a', encoding='UTF-8') as index_md:
            # 添加新文章列表
            # * [生活-论文&代码&生活](./生活-论文&代码&生活.html)
            new_line = f"* [{file_md}](./{file_md}.html)\n"
            print(new_line)
            index_md.write(new_line)

        # shutil.move(
        #     os.path.join(md_path, file_md + '.html'),
        #     os.path.join(html_path, file_md + '.html'))

print('更新index')
file_name = os.path.join('md', 'index.md')
os.system(f"python converter.py {file_name}")
