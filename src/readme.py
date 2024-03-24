#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :readme.py
@时间        :2023/07/20 14:00:28
@作者        :aliha
@版本        :1.0
@依赖        :无
@说明        :软件的介绍说明
'''


__updateLog = '''

<h4><span style="color:red">V 0.3.1 </span></h4>
<p>更新日期：2023-7-21</p>
<p>修复：错误路径导致程序卡死</p>
<hr />

<h4><span style="color:red">V 0.3.0 </span></h4>
<p>更新日期：2023-7-20</p>
<p>新增：拖拽文件或者文件夹打开的功能</p>
<p>新增：批量移除限制密码的功能</p>
<p>变更：更改 GUI 框架为 Pyside6 ，更漂亮的 UI</p>
<p>修复：无法重复点击【开始处理】按钮，需要重新打开的 BUG</p>
<hr />

<h4><span style="color:red">V 0.2.1 </span></h4>
<p>更新日期：2023-7-17</p>
<p>1. 增加移除限制 pptx 文档编辑的密码</p>
<p>2. 修复 bug ：启动软件直接点击【开始】按钮会退出软件</p>
<hr />

<h4><span style="color:red">V 0.2.0 </span></h4>
<p>更新日期：2023-7-13</p>
<p>1. 增加移除限制 xlsx 文档编辑的密码,包括工作簿和工作表保护密码</p>
<hr />

<h4><span style="color:red">V 0.1.0 </span></h4>
<p>更新日期：2022-10-24</p>
<p>1. 移除限制pdf文档编辑的密码</p>
<hr />

'''

__info = """
<p>批量移除限制编辑密码</p>
<p>移除PDF、xlsx、pptx限制密码输出文件在源路径，结果名称带_removepwd</p>
<p>只能移除文档限制编辑的密码解密不了加密文件</p>
"""

info = {
    'author': 'aliha',
    'version': '0.3.1',
    'updateDate': '2023-07-21',
    'userWeb': 'https://www.52pojie.cn/home.php?mod=space&uid=1873109',
    'info': __info,
    'updateLog': __updateLog
}

#  <p style="font-size:30px;color:orange">p标签设置字体颜色</p>
# nuitka --enable-plugin=pyside6 --standalone --onefile --remove-output --windows-disable-console --windows-icon-from-ico=icon.ico RemovePwd.py