#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :thread.py
@时间        :2023/07/20 10:41:04
@作者        :aliha
@版本        :1.0
@依赖        :excel.py, pdf.py, pptx.py
@说明        :移除密码的多线程处理
'''

from PySide6.QtCore import  QObject, QThread, Signal
from pdf import unlockFile as pdfUnlock
from excel import unlockFile as xlsxUnlock
from pptx import unlockFile as pptxUnlock
import time
import os

class WorkThread(QObject):
    count = (0)
    # countSignal = Signal(int)
    progressSignal = Signal(str)
    tipsSignal = Signal(str)

    def __init__(self):
        super(WorkThread, self).__init__()
        self.file_path = None

    def setFilePath(self, file_path):
        self.file_path = file_path

    # def work(self):
    #     self.flag = True
    #     while self.flag:
    #         self.count += 1
    #         self.progressSignal.emit(self.count)
    #         time.sleep(0.1)
    #         if(self.count == 100):
    #             QThread.currentThread().quit()
    #             break

    def work(self):
        if os.path.isfile(self.file_path ):
            self.progressSignal.emit('#=>[1/1]: {}'.format(self.file_path))
            self.unlockFile(self.file_path)

        if os.path.isdir(self.file_path ):
            file_lists = os.listdir(self.file_path)

            for file in file_lists:
                self.count += 1
                child_path = os.path.join(self.file_path, file)

                try:
                    self.unlockFile(child_path)
                except Exception as e:
                    self.progressSignal.emit('捕获到异常信息: {}'.format(e))

                self.progressSignal.emit('#=>[{}/{}]: {}'.format(self.count, len(file_lists), file))

        self.progressSignal.emit('ヾ(≧▽≦*)o 恭喜你，移除成功 \r\n 解密的文件保存在原目录下哦，名称带“removedPwd')
        QThread.currentThread().quit()



    def unlockFile(self, file):
        try:
            if('xlsx' in os.path.basename(file)):
                xlsxUnlock(file)
            if('pdf' in os.path.basename(file)):
                pdfUnlock(file)
            if('pptx' in os.path.basename(file)):
                pptxUnlock(file)

        except Exception as e:
            raise Exception("程序错误，请联系作者") from e


# 上述代码的启动方式如下：

# class main():

#     def runIt(self):
#         self.worker = WorkThread()
#         self.thread = QThread()
#         self.worker.moveToThread(self.thread)
#         self.worker.countSignal.connect(self.flush)
#         self.thread.started.connect(self.worker.work)
#         self.finished.connect(self.worker.quit)
#         self.finished.connect(self.worker.deleteLater)
#         self.thread.start()

#     def flush(self):
#         print('flush ing')



