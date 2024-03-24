#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :removePwd.py
@时间        :2023/07/20 10:42:17
@作者        :aliha
@版本        :1.0
@依赖        :thread.py, styleSheet.py, readme.py, pic.py
@说明        :文档密码移除工具主界面
'''


from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QTabWidget, QPushButton, QHBoxLayout, QTextEdit, QTextBrowser, QSizePolicy, QSpacerItem
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent, QPixmap, QPainter, QCursor, QCloseEvent, QFont
from PySide6.QtCore import Qt, QByteArray, QThread, Signal
import sys
import base64
import os
from styleSheet import styleSheet
from readme import info
from pic import imgstr
from thread import WorkThread

class FileDropLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("label")  # 添加该行
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setText("拖拽文件或文件夹到这里")
        self.setStyleSheet("QLabel { border: 2px dashed #aaa; padding: 5px; color: #555; }")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            event.setDropAction(Qt.CopyAction)
            pixmap = QPixmap(100, 100)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.setOpacity(0.7)
            painter.drawPixmap(0, 0, self.grab())
            painter.end()
            cursor = QCursor(pixmap)
            event.accept()
            self.setCursor(cursor)
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            file_path = urls[0].toLocalFile()
            self.setText("已选择: " + file_path)
            self.setCursor(Qt.CursorShape.ArrowCursor)
            # 调用MainWindow的方法，将选定的文件路径传递过去
            main_window = self.window()  # 使用 window() 方法获取父级窗口（MainWindow）
            if isinstance(main_window, MainWindow):
                main_window.setSelectedFilePath(file_path)
        else:
            event.ignore()

class ClickableLabel(QLabel):
    def __init__(self, text, url=None):
        super().__init__()
        self.url = url
        self.text = text

        if self.url is not None:
            self.setText(f'<a href="{url}">{text}</a>')
            self.setOpenExternalLinks(True)  # 打开链接时在外部浏览器中打开
            self.setStyleSheet("color: blue; text-decoration: underline;")  # 设置颜色和下划线效果
        else:
            self.setText(f'<p >{text}</>')

        font = QFont("Arial", 12, QFont.Bold)
        self.setFont(font)
          


class AboutUsTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        left_layout = QVBoxLayout()

        # Create labels for displaying software information
        author_label = ClickableLabel("作者信息：\t{}".format(info['author']),info['userWeb'])
        version_label = ClickableLabel("软件版本信息：\t{}".format(info['version']))
        update_label = ClickableLabel("更新日期：\t{}".format(info['updateDate']))

        # Create a layout for the QR code
        qr_code_layout = QHBoxLayout()
        qr_code_label = QLabel(self)
        png = self.base64ToByte()
        qr_code_image = QPixmap() 
        qr_code_image.loadFromData(png)
        # qr_code_image = QPixmap("QR.png") 
        qr_code_image = qr_code_image.scaled(250, 250, Qt.KeepAspectRatio) 
        qr_code_label.setPixmap(qr_code_image)
        qr_code_layout.addWidget(qr_code_label)

        left_layout.addWidget(author_label)
        left_layout.addWidget(version_label)
        left_layout.addWidget(update_label)
        left_layout.addLayout(qr_code_layout)
        left_layout.addStretch()

        funcInfo_label = QTextBrowser(self)
        funcInfo_label.setOpenExternalLinks(True) 
        funcInfo_label.setLineWrapMode(QTextBrowser.WidgetWidth) 

        func_info_html = """
        <h3>功能简介：</h3>
        {}
        <h3>更新日志</h3>
        {}
        """.format(info['info'],info['updateLog'])

        funcInfo_label.setHtml(func_info_html)

        layout.addLayout(left_layout)
        layout.addWidget(funcInfo_label)

        self.setLayout(layout)

    def base64ToByte(self):
        # Step 1: Decode the base64 data to obtain the raw image data
        decoded_data = base64.b64decode(imgstr)

        # Step 2: Create a QByteArray from the decoded image data
        byte_array = QByteArray(decoded_data)

        # Step 3: Load the image data into a QPixmap
        # pixmap = QPixmap()
        # pixmap.loadFromData(byte_array)
        return byte_array

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文档密码移除工具")
        self.resize(600, 280)
        self.thread = None
        self.selected_file_path = None

    # def rendererWindow(self):
        layout = QVBoxLayout(self)

        tab_widget = QTabWidget(self)

        # Tab 1: Password Removal
        tab1 = QWidget(self)
        tab1_layout = QVBoxLayout(tab1)
        label = FileDropLabel(tab1)
        tab1_layout.addWidget(label)

        self.progress_output = QTextEdit(tab1)
        self.progress_output.setReadOnly(True)
        tab1_layout.addWidget(self.progress_output)

        self.button = QPushButton("开始处理", tab1)
        self.button.clicked.connect(self.startWorkerThread)
        tab1_layout.addWidget(self.button)

        tab1.setLayout(tab1_layout)
        tab_widget.addTab(tab1, "限制密码移除")

        # Tab 2: Software Settings
        tab2 = QWidget(self)
        tab_widget.addTab(tab2, "批量加密解密")

        tab2_layout = QVBoxLayout(tab2)
        development_label = QLabel("正在开发中，请耐心等待", tab2)
        development_label.setAlignment(Qt.AlignCenter)
        tab2_layout.addWidget(development_label)

        tab2.setLayout(tab2_layout)

        # Create the third tab (About Us)
        tab3 = AboutUsTab()
        tab_widget.addTab(tab3, "关于我们")

        layout.addWidget(tab_widget)

        self.setStyleSheet(styleSheet)
        layout.setContentsMargins(0, 1, 0, 0)
        self.setLayout(layout)

    def closeEvent(self, event: QCloseEvent) -> None:
        return super().closeEvent(event)

    def startWorkerThread(self):
        if self.selected_file_path is not None:
            if os.path.isdir(self.selected_file_path) or os.path.isfile(self.selected_file_path):
                self.worker = WorkThread()
                self.thread = QThread()
                self.worker.moveToThread(self.thread)
                self.worker.setFilePath(self.selected_file_path)
                self.worker.progressSignal.connect(self.updateProgressBar)
                self.thread.started.connect(self.progress_output.clear)
                self.thread.started.connect(self.worker.work)
                self.thread.finished.connect(self.thread.quit)
                self.thread.finished.connect(self.unlockStartButtom)
                self.thread.finished.connect(self.thread.deleteLater)
                self.thread.start()
                self.button.setEnabled(False)
                self.button.setStyleSheet('background-color: #e0e0e0;')
                label = self.findChild(FileDropLabel, "label")
                if label:
                    label.setEnabled(False)
        else:
            self.progress_output.clear()
            self.progress_output.append('请输入正确的路径')
    
    def unlockStartButtom(self):
        self.button.setEnabled(True)
        self.button.setStyleSheet('background-color: #4caf50;')
        label = self.findChild(FileDropLabel, "label")
        if label:
            label.setEnabled(True)

    def setSelectedFilePath(self, file_path):
        self.selected_file_path = file_path

    def updateProgressBar(self, value):
        self.progress_output.append(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.rendererWindow()
    window.show()
    sys.exit(app.exec())
