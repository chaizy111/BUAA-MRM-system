# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '入院信息查询.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from db.login_op import check_permission
from db.search_op import search_admission_info
from ui.print_dialog import PrintDialog  # 假设打印窗口的类在 `print_dialog.py` 中

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout for date range selection
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

        # Layout for department input
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(380, 30, 115, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)

        # Layout for buttons
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(510, 20, 241, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        # Adding the table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 760, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(10)  # For example, setting 10 rows for demonstration

        # Setting up table headers
        headers = ["入院时间", "病历号", "患者姓名", "性别", "入院科室"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Adding row numbers (1, 2, 3, ...)
        #self.tableWidget.setVerticalHeaderLabels([str(i+1) for i in range(self.tableWidget.rowCount())])

        # Enable vertical header (for row numbers)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_4.clicked.connect(self.openPrintDialog)  # 打印按钮绑定事件
        self.pushButton_2.clicked.connect(MainWindow.close)  # 退出按钮关闭窗口
        self.pushButton.clicked.connect(self.on_search_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "入院信息查询"))
        self.label.setText(_translate("MainWindow", "时间："))
        self.label_2.setText(_translate("MainWindow", "至"))
        self.label_3.setText(_translate("MainWindow", "科室："))
        self.pushButton.setText(_translate("MainWindow", "查询(&S)"))
        self.pushButton_4.setText(_translate("MainWindow", "打印(&P)"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭(&E)"))

    def openPrintDialog(self):
        """打开打印窗口"""
        self.printDialog = PrintDialog()  # 创建打印窗口实例
        self.printDialog.show()  # 显示打印窗口


    def on_search_clicked(self):

        username, ok = QInputDialog.getText(
            None, "输入账号", "请输入您的账号："
        )

        if not ok or not username.strip():
            QtWidgets.QMessageBox.warning(
                None, "输入错误", "账号不能为空！", QtWidgets.QMessageBox.Ok
            )
            return

        # 检查权限
        if not check_permission(username.strip(), "admission_info_search"):
            QtWidgets.QMessageBox.critical(
                None, "权限不足", "您没有权限查询！", QtWidgets.QMessageBox.Ok
            )
            return

        # 获取输入的日期范围和科室
        admission_start_date = self.dateTimeEdit.date().toString("yyyy-MM-dd")
        admission_end_date = self.dateTimeEdit_2.date().toString("yyyy-MM-dd")
        unit_name = self.lineEdit.text()

        try:
            # 调用数据库查询函数
            admission_info = search_admission_info(admission_start_date, admission_end_date, unit_name)

            # 更新表格显示
            self.update_table(admission_info)
        except Exception as e:
            QMessageBox.critical(self, "查询失败", f"数据库查询失败：{str(e)}")

    def update_table(self, results):
        # 清空表格
        self.tableWidget.setRowCount(0)

        # 填充查询结果
        for row_num, row_data in enumerate(results):
            self.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
import sys

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
