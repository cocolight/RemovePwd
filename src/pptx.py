#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :pptx.py
@时间        :2023/07/20 14:00:53
@作者        :aliha
@版本        :1.0
@依赖        :util.py
@说明        :移除PPTX限制密码
'''


from lxml import etree
import shutil
import os
from util import delDirs, filterFiles, unZip, zipDir, mkdir

keyNode = ['modifyVerifier']

def unlockFile(fpath:str):
    fname = os.path.basename(fpath)
    fnamef, ftype = fname.rsplit(".",1)

    parent_path = os.path.dirname(fpath)

    tmpdir_path = os.path.join(parent_path, 'tmp')
    copyed_tar_fpath = os.path.join(tmpdir_path, fname)
    old_zip_fpath = tmpdir_path + '\\' + fnamef + '.zip'
    extractalldir_path = os.path.join(tmpdir_path, fnamef)
    new_zip_path = os.path.join(tmpdir_path, fnamef + '_removedPwd.zip')
    new_zip_fnamef = os.path.basename(new_zip_path)
    removedPwd_fpath = os.path.join(tmpdir_path, new_zip_fnamef + ftype)
    new_fpath = os.path.join(parent_path, fnamef + '_removedPwd.' + ftype)


    try:
        if os.path.exists(tmpdir_path):
            os.remove(tmpdir_path)

        mkdir(tmpdir_path)
        shutil.copyfile(fpath, copyed_tar_fpath)
        os.rename(copyed_tar_fpath, old_zip_fpath)

    except FileExistsError as e:
        raise Exception("文件已存在，无法创建") from e
    except Exception as e:
        raise Exception("拷贝 pptx 文件错误") from e


    # 解压文件
    unZip(old_zip_fpath, extractalldir_path)

    xmls = filterFiles(extractalldir_path, 'xml')

    for xml in xmls:
        if('Styles' not in xml and 'Props' not in xml and 'theme' not in xml and 'tag' not in xml and 'slide' not in xml):
            for kwd in keyNode:
                removeNode(xml, xml, kwd)

    zipDir(extractalldir_path, new_zip_path) # 重新压缩

    try: # 重命名为 pptx,拷贝到原目录
        os.rename(new_zip_path, removedPwd_fpath)
        shutil.copyfile(removedPwd_fpath, new_fpath)
    except Exception as e:
        raise Exception("拷贝文件错误") from e


    # 删除tmp下所有文件
    delDirs(tmpdir_path,root=True)


def removeNode(fpath:str, sfPath, keyNode:str):
    """移除xml节点，并且存储

    Args:
        fpath (str): 源xml路径
        sfpath (str): 移除节点后的xml路径
        keyNode (str): 要移除节点
    """
    try:
        tree = etree.parse(fpath) 

        for child in tree.iter():
            if(keyNode in child.tag):
                child.getparent().remove(child)  
                tree.write(sfPath)
                break
    except Exception as e:
        raise Exception("移除节点失败") from e

    


    
