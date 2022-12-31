import codecs
import os
import sys

from opencc import OpenCC
from conversion_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog

import threading

class subtitle_conversion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.converter = OpenCC('s2twp')

        self.thread_setup_control = threading.Thread(target=self.setup_control)
        self.thread_setup_control.start()

    # 按鈕控制
    def setup_control(self):
        self.ui.start_button.clicked.connect(self.onStartButtonClick) # 當按下開始按鈕
        self.ui.choose_ass_file_button.clicked.connect(self.choose_ass_file_path) # 當按下選擇字幕檔的路徑按鈕
        self.ui.save_path_button.clicked.connect(self.save_ass_file_path) # 當按下儲存路徑的路徑按鈕

    # 將text顯示在textBrowser上
    def display_text(self, text):
        self.ui.textBrowser.append(f'{text}')

    # 選擇字幕檔
    def choose_ass_file_path(self):
        self.save_ass_file, _ = QFileDialog.getOpenFileName(None, '選擇.ass字幕檔', './')
        self.ass_save_file_name = os.path.basename(self.save_ass_file) # 檔名
        self.ass_save_file_path = os.path.split(self.save_ass_file)[0] # 路徑
        self.ui.choose_ass_file_input.setText(self.ass_save_file_name)

    # 選擇儲存路徑
    def save_ass_file_path(self):
        self.ass_save_directory = QFileDialog.getExistingDirectory(None, '選擇儲存資料夾', './')
        self.ui.save_path_input.setText(self.ass_save_directory)

    # 當按下開始按鈕
    def onStartButtonClick(self):
        self.read_ass_file()
        self.conversion()
        self.write_ass_file()

    # 讀字幕檔
    def read_ass_file(self):
        self.display_text('讀取字幕檔')

        with codecs.open(self.save_ass_file, 'r', 'utf_8') as file:
            self.lines = file.readlines() # 讀全部的字幕

        self.traditional_lines = [] # 用來儲存繁體字的陣列

    # 進行簡繁轉換
    def conversion(self):
        self.display_text('進行簡繁轉換')

        for line in self.lines:
            traditional_line = self.converter.convert(line) # 簡轉繁
            self.traditional_lines.append(traditional_line) # 轉換後的繁體字添加到陣列裡

    # 儲存字幕檔
    def write_ass_file(self):
        self.display_text('儲存字幕檔')

        self.new_ass_save_file_path = f'{self.ass_save_directory}/【繁體】{self.ass_save_file_name}' # 將原本的檔名增加【繁體】兩字
        with codecs.open(f'{self.new_ass_save_file_path}', 'w', 'utf-8') as file:
            file.writelines(self.traditional_lines)

        self.display_text(f'儲存完畢!')