#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :pdf.py
@时间        :2023/07/20 14:01:58
@作者        :aliha
@版本        :1.0
@依赖        :无
@说明        :移除PDF限制密码
'''


import pikepdf


def unlockFile(fpath:str):
    """移除pdf限制编辑，并且存储

    Args:
        fpath (str): 带限制的pdf路径
        sfpath (str): 移除限制的pdf路径

    Returns:
        str: 移除成功的提示话语
    """
    try:
        pdf = pikepdf.open(fpath, allow_overwriting_input=True)
    except Exception as e:
        print('打开pdf出错') 
    
    try:
        sfpath = fpath.rsplit('.',1)[0] +"_removepwd."+ fpath.rsplit('.',1)[1]
        pdf.save(sfpath)
    except Exception as e:
        print('写入pdf失败') 

    return 'ヾ(≧▽≦*)o 恭喜你，移除成功'
