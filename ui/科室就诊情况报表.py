# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
import sys

from db.login_op import check_permission
from db.statistic_op import get_diagnosisInUnit_statistic
from ui.print_dialog import PrintDialog  # 导入打印窗口类（假设文件名为 print_dialog.py）


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 331, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.horizontalLayout.addWidget(self.dateTimeEdit_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(420, 20, 320, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)

        # 数据显示表格
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 760, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)  # 根据实际表结构调整列数
        self.tableWidget.setHorizontalHeaderLabels(["列1", "列2", "列3", "列4", "列5"])  # 替换为实际列名

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.close)  # 退出按钮
        self.pushButton_2.clicked.connect(self.openPrintDialog)  # 打印按钮绑定事件
        self.pushButton.clicked.connect(self.on_search_button_clicked)  # 查询按钮绑定事件
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "科室就诊情况报表"))
        self.label.setText(_translate("MainWindow", "时间："))
        self.label_2.setText(_translate("MainWindow", "至"))
        self.pushButton.setText(_translate("MainWindow", "查询(&S)"))
        self.pushButton_2.setText(_translate("MainWindow", "打印(&P)"))
        self.pushButton_3.setText(_translate("MainWindow", "导出(&D)"))
        self.pushButton_4.setText(_translate("MainWindow", "退出(&E)"))

    def openPrintDialog(self):
        """打开打印窗口"""
        self.printDialog = PrintDialog()  # 创建打印窗口实例
        self.printDialog.show()  # 显示打印窗口

    def on_search_button_clicked(self):

        """查询按钮点击事件"""
        try:
            # 获取查询结果
            results = get_diagnosisInUnit_statistic()

            # 清空表格
            self.tableWidget.setRowCount(0)

            # 填充表格
            if results:
                for row_index, row_data in enumerate(results):
                    self.tableWidget.insertRow(row_index)
                    for col_index, data in enumerate(row_data):
                        self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(data)))
            else:
                QMessageBox.information(None, "提示", "未查询到符合条件的数据！")
        except Exception as e:
            QMessageBox.critical(None, "错误", f"查询失败: {str(e)}")



if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
