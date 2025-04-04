# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '病案借阅.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from db.login_op import check_permission
from db.normal_op import create_borrow_request
from intermediate_data_structure.br_info import BrInfo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 40, 187, 21))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(430, 10, 341, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 400, 631, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_4.addWidget(self.lineEdit_7)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_4.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_5.addWidget(self.lineEdit_8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton.clicked.connect(self.handle_borrow) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "病案借阅"))
        self.label.setText(_translate("MainWindow", "病案号："))
        self.pushButton.setText(_translate("MainWindow", "提交(&S)"))
        self.pushButton_4.setText(_translate("MainWindow", "放弃(&C)"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭(&E)"))
        self.label_3.setText(_translate("MainWindow", "借阅人："))
        self.label_7.setText(_translate("MainWindow", "所属科室："))
        self.label_9.setText(_translate("MainWindow", "证件号："))
        self.label_4.setText(_translate("MainWindow", "借阅原因："))
        self.label_8.setText(_translate("MainWindow", "联系电话："))

    def handle_borrow(self):
        br_info = BrInfo (
            medical_record_id = self.lineEdit.text(),
            borrowed_by = self.lineEdit_3.text(),
            unit_name = self.lineEdit_7.text(),
            IDcard_num = self.lineEdit_9.text(),
            borrow_reason = self.lineEdit_4.text(),
            contact_phone = self.lineEdit_8.text()
        )

        if create_borrow_request(br_info):
            QMessageBox.information(None, "成功", "借阅请求已提交！")
            QApplication.quit()
        else:
            QMessageBox.critical(None, "失败", "借阅请求提交失败！")

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
import sys

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
