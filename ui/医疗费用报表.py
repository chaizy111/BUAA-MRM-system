# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
import sys

from PyQt5 import QtGui

import db
from db.login_op import check_permission
from ui.print_dialog import PrintDialog  # 导入打印窗口类（假设文件名为 print_dialog.py）
from db.statistic_op import get_fee_statistic_by_day
from db.statistic_op import get_fee_statistic_by_month
from db.statistic_op import get_fee_statistic_by_year

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 341, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.dateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateTimeEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.dateTimeEdit_2.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateTimeEdit_2)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 0, 341, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_year = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_year.setObjectName("pushButton_year")
        self.horizontalLayout_2.addWidget(self.pushButton_year)

        self.pushButton_month = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_month.setObjectName("pushButton_month")
        self.horizontalLayout_2.addWidget(self.pushButton_month)

        self.pushButton_day = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_day.setObjectName("pushButton_day")
        self.horizontalLayout_2.addWidget(self.pushButton_day)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(730, 150, 16, 401))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(60, 170, 671, 371))
        self.columnView.setObjectName("columnView")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_year.clicked.connect(lambda: self.perform_search("year"))
        self.pushButton_month.clicked.connect(lambda: self.perform_search("month"))
        self.pushButton_day.clicked.connect(lambda: self.perform_search("day"))
        self.pushButton_2.clicked.connect(MainWindow.close)  # 关闭按钮
        self.pushButton_4.clicked.connect(self.openPrintDialog)  # 打印按钮绑定事件
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "医疗费用报表"))
        self.label.setText(_translate("MainWindow", "时间："))
        self.label_2.setText(_translate("MainWindow", "至"))
        self.pushButton_year.setText(_translate("MainWindow", "年报表(&Y)"))
        self.pushButton_month.setText(_translate("MainWindow", "月报表(&M)"))
        self.pushButton_day.setText(_translate("MainWindow", "日报表(&D)"))
        self.pushButton_4.setText(_translate("MainWindow", "打印(&P)"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭(&E)"))


    def perform_search(self, report_type):
        """
        根据报表类型执行查询并展示结果
        :param report_type: str, "year", "month", "day"
        """
        try:
            if report_type == "year":
                results = db.statistic_op.get_fee_statistic_by_year()
            elif report_type == "month":
                results = db.statistic_op.get_fee_statistic_by_month()
            elif report_type == "day":
                results = db.statistic_op.get_fee_statistic_by_day()
            else:
                raise ValueError("无效的报表类型")

            # 将结果显示在界面表格中
            self.display_results(results)

        except Exception as e:
            print(f"查询失败: {e}")

    def display_results(self, results):
        """
        将查询结果显示在前端表格中
        :param results: list of tuples, 查询结果
        """

        # 设置列标题
        column_headers = ["Year", "Month", "Day", "TotalIncome"]
        if len(results) > 0:
            if len(results[0]) == 2:  # 年报表
                column_headers = ["Year", "TotalIncome"]
            elif len(results[0]) == 3:  # 月报表
                column_headers = ["Year", "Month", "TotalIncome"]

        # 使用表格模型显示数据
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(column_headers)

        for row in results:
            s = 't'.join([str(cell) for cell in row])
            items = QtGui.QStandardItem(s)
            model.appendRow(items)

        self.columnView.setModel(model)

    def openPrintDialog(self):
        """打开打印窗口"""
        self.printDialog = PrintDialog()  # 创建打印窗口实例
        self.printDialog.show()  # 显示打印窗口


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
