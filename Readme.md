# 一、功能介绍

批量移除限制编辑密码，移除PDF、xlsx、pptx限制密码输出文件在源路径，结果名称带`_removepwd`。

⚠️**只能移除文档限制编辑的密码解密不了加密文件**

## 1.1、使用方法

将文件/文件夹拖入窗口虚线框位置，点击开始处理

![](E:\BaiduSyncdisk\vsc\removepwd\1.png)

## 1.2、更新计划

### TODO：

- [ ] 注册右键菜单——可以方便的处理文件；
- [ ] 增加支持docx文件——支持docx文件的限制解除；

- [ ] 增加【浏览】按钮——便于选择文件夹；

- [ ] 增加批量加密（限制密码）；

- [ ] 增加log功能——便于排查问题；

### BUG：

- [ ] win11 处理 ppt 和 excel 陷入死循环；

# 二、二次开发

## 2.1、项目结构

+ `src`下为代码文件，其中`removePwd.py`为主入口；

+ `setup`下为**Inno Setup Compiler**脚本，用于制作安装包；

## 2.2、环境安装

+ Python3 Version：≤3.11

1. 安装依赖

```shell
pip install -r requirements.txt
```

## 2.2、原理介绍

办公文档解压后将内部的`xml`文件中的密码字段移除从而达到解除限制的效果。

## 2.3、打包exe

使用[Nuitka](https://github.com/Nuitka/Nuitka)制作可执行文件。

```shell
nuitka --standalone --enable-plugin=pyside6 --enable-plugin=upx --windows-disable-console --remove-output --include-data-file=./icon.ico=./ --windows-icon-from-ico='icon.ico' RemovePwd.py
```

## 2.4、安装包打包

使用 Inno Setup Compiler 打开`setup.iss`文件，修改其中的`[Files]`下的路径为上一步生成的文件夹，执行打包即可。
