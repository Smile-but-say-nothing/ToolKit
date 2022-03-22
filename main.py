import sys
import ToolKit
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QRadioButton
import urllib.request
from PyQt5.QtWidgets import QApplication, QWidget
import os
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = ToolKit.Ui_MainWindow()
        self.ui.setupUi(self)

    def get_file_directory(self):
        fileDescription = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "All Files(*);;Text Files(*.txt);;Excel Files(*.xlsx)")
        filePath = str(fileDescription[0])
        # 显示文件路径
        self.ui.lineEdit.setText(filePath)
        # 读取表格
        df = pd.read_excel(filePath)
        # 显示列名
        self.ui.lineEdit_2.setText(' '.join(df.columns.values))

    def get_folder_directory(self):
        folderPath = QFileDialog.getExistingDirectory(self, "选取文件", os.getcwd())
        # 显示文件夹路径
        self.ui.lineEdit_5.setText(folderPath)

    def download(self):
        def download_img(img_url, imgname, path):
            request = urllib.request.Request(img_url)
            response = urllib.request.urlopen(request)
            img_name = imgname + '.jpg'
            filename = path + img_name
            if response.getcode() == 200:
                with open(filename, "wb") as f:
                    f.write(response.read())  # 将内容写入图片
                return filename

        filePath = self.ui.lineEdit.text()
        dstPath = self.ui.lineEdit_5.text() + '/'
        urlCol = self.ui.lineEdit_4.text()
        df = pd.read_excel(filePath, )
        dfUrl = df[urlCol]
        pattern = self.ui.lineEdit_3.text().split(' ')
        patternList = []
        for item in pattern:
            patternList.append(df[item])
        for i in range(df.shape[0]-1):
            try:
                imgurl = dfUrl[i]
                imgname = [str(patternList[order][i]) for order in range(len(pattern))]
                imgname = str('-'.join(imgname))
                download_img(imgurl, imgname, dstPath)
                print('第' + str(i) + '张图下载完成！')
            except BaseException as e:
                print(e)
                continue



if __name__ =='__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())