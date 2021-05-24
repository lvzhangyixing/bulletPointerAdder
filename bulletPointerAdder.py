#! python3
# bullectPointerAdder.py 给粘贴板每一行内容增加*

import pyperclip

text = pyperclip.paste()

# 分割行，添加*
lines = text.split('\n')
for i in range(len(lines)):  # 遍历所有行的索引
    lines[i] = '*' + lines[i]
text = '\n'.join(lines) # 连接列表中的字符串
pyperclip.copy(text)
