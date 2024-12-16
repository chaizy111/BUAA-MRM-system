# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file '借阅审批.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox

from db.normal_op import get_pending_requests, change_request_status_to_approved


class Ui_MainWindow(object):

    borrow_request_ids=[]

    def __init__(self, account=None):
        self.account = account  # 存储传递的 account 值


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 30, 300, 30))  # 设置位置和大小
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 711, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 6, item)

        self.tableWidget.itemChanged.connect(self.handle_checkbox_change)

        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setText("确定")
        self.confirm_button.setGeometry(QtCore.QRect(650, 440, 100, 40))  # 设置按钮位置
        self.confirm_button.clicked.connect(self.confirm_approval)  # 绑定点击事件

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.get_pending_request()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "借阅审批"))
        self.label.setText(_translate("MainWindow", "借阅审批"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "byperson"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "id_card_number"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "phone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "statue"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def get_pending_request(self):
        requests = get_pending_requests()
        for i, request in enumerate(requests):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(request[0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(request[1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(request[2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(request[3])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(request[5])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(request[7])))

    def handle_checkbox_change(self, item):
        """处理复选框的状态改变"""
        if item.column() == 6 and item.checkState() == QtCore.Qt.Checked:
            row = item.row()
            # 获取该行的所有信息
            request_id = self.tableWidget.item(row, 0).text()
            number = self.tableWidget.item(row, 1).text()
            date = self.tableWidget.item(row, 2).text()
            byperson = self.tableWidget.item(row, 3).text()
            id_card_number = self.tableWidget.item(row, 4).text()
            phone = self.tableWidget.item(row, 5).text()

            # 新建一个表格来展示选择的借阅请求信息
            self.create_new_table([request_id, number, date, byperson, id_card_number, phone])

            # 记录已选择的借阅请求id
            self.borrow_request_ids.append(request_id)

            QMessageBox.information(self.centralwidget, "借阅请求已选中", f"选中的借阅请求Id: {request_id}")

    def create_new_table(self, data):
        """新建一个表格展示选择的借阅请求"""
        table_window = QtWidgets.QWidget(self.centralwidget)
        table_window.setGeometry(50, 300, 711, 200)  # 设置表格位置

        table_widget = QtWidgets.QTableWidget(table_window)
        table_widget.setColumnCount(6)
        table_widget.setRowCount(1)

        headers = ["Id", "number", "date", "byperson", "id_card_number", "phone"]
        table_widget.setHorizontalHeaderLabels(headers)

        for col, value in enumerate(data):
            table_widget.setItem(0, col, QTableWidgetItem(value))

        #table_window.show()

    def confirm_approval(self):
        change_request_status_to_approved(self.borrow_request_ids, self.account)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())