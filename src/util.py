#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :util.py
@时间        :2023/07/20 13:59:26
@作者        :aliha
@版本        :1.0
@依赖        :无
@说明        :常用的文件处理的工具函数抽取到了这里
'''


import shutil
import os
import zipfile


def delDirs(dirpath:str, root=False):
    """删除路径文件下所有的文件，root=true 时包括根文件夹

    Args:
        dirpath (str): 文件夹路径
        root (boolean): 是否删除根目录
    """
    try:
        filelists = os.listdir(dirpath)  # 获取目录下所有文件列表
        for mydir in filelists:  # 遍历文件列表
            filepath = os.path.join(dirpath, mydir)  # 将文件名进行拼接
            if os.path.isfile(filepath):  # 判断该文件是否为文件
                os.remove(filepath)  # 若为文件，则直接删除
            elif os.path.isdir(filepath):  # 判断该文件是否为文件夹
                shutil.rmtree(filepath, True)  # 若为文件夹，则删除该文件夹及文件夹内所有文件
        if(root):
            shutil.rmtree(dirpath, True)  # 最后删除根文件夹
    except Exception as e:
        print('删除缓存文件失败') 


def filterFiles(folder_path:str, file_extension:str):
    """获取指定路径下，符合扩展名条件的文件路径

    Args:
        folder_path (str): 根目录
        file_extension (str): 扩展名

    Returns:
        _type_: 查找结果组成的数组
    """

    files = []

    def filter(folder:str, extension:str):

        try:
            file_lists = os.listdir(folder) 
            for child in file_lists:
                child_path = os.path.join(folder, child)

                if(os.path.isfile(child_path)):
                    frname, ftype = os.path.basename(child_path).rsplit('.',1)
                    if(extension in ftype):
                        files.append(child_path)
                        continue
                elif(os.path.isdir(child_path)):
                    filter(child_path, extension)
        except Exception as e:
            print('遍历文件错误')
            raise e

    filter(folder_path, file_extension)

    return files


def unZip(zip_file:str, extractall_path:str):
    """解压缩zip文件

    Args:
        zip_file (str): zip文件路径
        extractall_path (str): 解压路径
    """
    try:
        if(zipfile.is_zipfile(zip_file)):
            zin = zipfile.ZipFile(zip_file, 'r')  # 以只读方式打开压缩包
            zin.extractall(path=extractall_path) 
            zin.close()
    except Exception as e:
        print('解压失败')
        raise e


def zipDir(dirpath:str, outFullName:str):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
 
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()

def mkdir(dirpath:str):
    try:
        if( not os.path.exists(dirpath)):
            os.makedirs(dirpath)
    except Exception as e:
        print('创建缓存文件错误')