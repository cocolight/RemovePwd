#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :styleSheet.py
@时间        :2023/07/20 14:00:10
@作者        :aliha
@版本        :1.0
@依赖        :无
@说明        :窗口的样式文件
'''


styleSheet = """
QPushButton {
    background-color: #4caf50;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #45a049;
}
QPushButton:pressed {
    background-color: #2980b9;
}
QTextEdit {
    background-color: #fff;
    border: 2px solid #aaa;
    padding: 5px;
    font-family: Arial, sans-serif;
    font-size: 14px;
    color: #333;
}
QTabWidget::pane {
    border: 1px solid #aaa;
    background-color: #f0f0f0;
    padding: 0px;
}
QTabBar::tab {
    background-color: #4caf50;
    color: white;
    padding: 8px;
    border: none;
    font-family: Arial, sans-serif;
    font-size: 14px;
    font-weight: bold;
}
QTabBar::tab:hover {
    background-color: #45a049;
}
QTabBar::tab:selected {
    background-color: #fff;
    color: #4caf50;
}
"""
