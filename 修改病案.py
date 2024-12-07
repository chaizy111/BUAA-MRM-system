# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '修改病案.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os  # 用于运行外部脚本
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from designer.db.normal_op import delete_record_by_recordID
from designer.db.search_op import search_by_info


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 50, 187, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 添加信号和槽
        self.pushButton.clicked.connect(self.open_new_case)  # 点击“查找”按钮
        self.pushButton_2.clicked.connect(MainWindow.close)  # 点击“关闭”按钮

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "修改病案"))
        self.pushButton.setText(_translate("MainWindow", "查找[&S]"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭[&E]"))
        self.label.setText(_translate("MainWindow", "病案号："))

    def open_new_case(self):
        search_info = self.lineEdit.text()  # 获取病案号
        if not search_info:
            QtWidgets.QMessageBox.warning(
                None, "输入错误", "请输入病案号！", QtWidgets.QMessageBox.Ok
            )
            return

        # 查找病案
        result = search_by_info(search_info)
        if result:
            # 找到病案，删除原有病案
            delete_record_by_recordID(search_info)
            QtWidgets.QMessageBox.information(
                None, "成功", "原有病案已删除！现在打开新建病案。", QtWidgets.QMessageBox.Ok
            )
            # 打开新建病案脚本
            script_path = os.path.join(os.getcwd(), "新建病案.py")
            if os.path.exists(script_path):
                os.system(f'python "{script_path}"')  # 运行脚本
            else:
                QtWidgets.QMessageBox.critical(
                    None, "错误", "新建病案.py 文件未找到！", QtWidgets.QMessageBox.Ok
                )
        else:
            QtWidgets.QMessageBox.warning(
                None, "未找到病案", "没有找到相关病案！", QtWidgets.QMessageBox.Ok
            )



if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
