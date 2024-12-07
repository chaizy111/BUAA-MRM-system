# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from designer.db.search_op import get_patients_by_info
from print_dialog import PrintDialog  # 假设打印窗口的类在 `print_dialog.py` 中


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '查询条件1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        '''
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        '''


        # 表格布局
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 700, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels([
            "病历号", "患者姓名", "性别", "出生年月", "省市","区县",
            "民族", "职业", "患者地址"
        ])


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.pushButton_2.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "查询条件1"))
        #self.pushButton.setText(_translate("MainWindow", "查询[&S]"))
        #self.pushButton_2.setText(_translate("MainWindow", "关闭[&E]"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 30, 320, 80))
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 90, 701, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 40, 694, 210))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_2.addWidget(self.lineEdit_9)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_2.addWidget(self.lineEdit_10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_3.addWidget(self.lineEdit_11)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_3.addWidget(self.lineEdit_12)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_3.addWidget(self.lineEdit_13)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_4.addWidget(self.lineEdit_14)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_4.addWidget(self.lineEdit_15)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_4.addWidget(self.lineEdit_16)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.label_18)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_5.addWidget(self.dateTimeEdit)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.horizontalLayout_5.addWidget(self.dateTimeEdit_2)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_5.addWidget(self.label_24)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_5.addWidget(self.lineEdit_17)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_5.addWidget(self.label_25)
        spacerItem = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_6.addWidget(self.label_21)
        self.dateTimeEdit_6 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_6.setObjectName("dateTimeEdit_6")
        self.horizontalLayout_6.addWidget(self.dateTimeEdit_6)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_6.addWidget(self.label_22)
        self.dateTimeEdit_4 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_4.setObjectName("dateTimeEdit_4")
        self.horizontalLayout_6.addWidget(self.dateTimeEdit_4)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_6.addWidget(self.label_23)
        self.dateTimeEdit_5 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_5.setObjectName("dateTimeEdit_5")
        self.horizontalLayout_6.addWidget(self.dateTimeEdit_5)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_6.addWidget(self.label_20)
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.horizontalLayout_6.addWidget(self.dateTimeEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_7.addWidget(self.label_27)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_7.addWidget(self.lineEdit_19)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_7.addWidget(self.label_26)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.horizontalLayout_7.addWidget(self.lineEdit_18)
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # 绑定按钮事件
        self.pushButton_2.clicked.connect(self.openPrintDialog)  # 打印按钮绑定事件
        self.pushButton_4.clicked.connect(MainWindow.close)      # 退出按钮关闭窗口
        self.pushButton.clicked.connect(self.openQueryDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "患者信息查询"))
        self.pushButton.setText(_translate("MainWindow", "查询(&S)"))
        self.pushButton_2.setText(_translate("MainWindow", "打印(&P)"))
        self.pushButton_3.setText(_translate("MainWindow", "导出(&D)"))
        self.pushButton_4.setText(_translate("MainWindow", "退出(&E)"))
        self.label.setText(_translate("MainWindow", "病历号;"))
        self.label_4.setText(_translate("MainWindow", "患者姓名："))
        self.label_5.setText(_translate("MainWindow", "性别："))
        self.label_6.setText(_translate("MainWindow", "医疗付款方式："))
        self.comboBox.setItemText(0, _translate("MainWindow", "微信"))
        self.comboBox.setItemText(1, _translate("MainWindow", "支付宝"))
        self.comboBox.setItemText(2, _translate("MainWindow", "现金"))
        self.comboBox.setItemText(3, _translate("MainWindow", "其他"))
        self.label_7.setText(_translate("MainWindow", "国籍："))
        self.label_10.setText(_translate("MainWindow", "民族："))
        self.label_11.setText(_translate("MainWindow", "职业："))
        self.label_12.setText(_translate("MainWindow", "地址："))
        self.label_13.setText(_translate("MainWindow", "联系电话："))
        self.label_14.setText(_translate("MainWindow", "患者邮编："))
        self.label_15.setText(_translate("MainWindow", "联系人："))
        self.label_16.setText(_translate("MainWindow", "联系人地址："))
        self.label_17.setText(_translate("MainWindow", "联系人电话："))
        self.label_18.setText(_translate("MainWindow", "出生年月："))
        self.label_19.setText(_translate("MainWindow", "——"))
        self.label_24.setText(_translate("MainWindow", "患者年龄"))
        self.label_25.setText(_translate("MainWindow", "岁"))
        self.label_21.setText(_translate("MainWindow", "入院时间："))
        self.label_22.setText(_translate("MainWindow", "——"))
        self.label_23.setText(_translate("MainWindow", "出院时间："))
        self.label_20.setText(_translate("MainWindow", "——"))
        self.label_27.setText(_translate("MainWindow", "疾病名称："))
        self.label_26.setText(_translate("MainWindow", "住院天数："))

    def openPrintDialog(self):
        """打开打印窗口"""
        self.printDialog = PrintDialog()  # 创建打印窗口实例
        self.printDialog.show()  # 显示打印窗口

    def openQueryDialog(self):
        """打开查询条件窗口"""
        self.queryDialog = QtWidgets.QMainWindow()  # 创建一个新的窗口实例
        self.ui_query = Ui_MainWindow1()  # 创建查询条件窗口的UI实例
        self.ui_query.setupUi(self.queryDialog)  # 初始化查询条件窗口的UI
        self.queryDialog.show()  # 显示查询条件窗口

        search_info = {
            "medical_record_number": self.ui.lineEdit.text(),  # 病历号
            "name": self.ui.lineEdit_2.text(),  # 患者姓名
            "gender": self.ui.comboBox.currentText(),  # 性别
            "payment_method": self.ui.comboBox_2.currentText(),  # 医疗付款方式
            "nationality": self.ui.lineEdit_6.text(),  # 国籍
            "ethnicity": self.ui.lineEdit_7.text(),  # 民族
            "occupation": self.ui.lineEdit_8.text(),  # 职业
            "address": self.ui.lineEdit_9.text(),  # 地址
            "phone_number": self.ui.lineEdit_10.text(),  # 联系电话
            "postal_code": self.ui.lineEdit_11.text(),  # 患者邮编
            "contact_person": self.ui.lineEdit_12.text(),  # 联系人
            "contact_address": self.ui.lineEdit_13.text(),  # 联系人地址
            "contact_phone": self.ui.lineEdit_14.text(),  # 联系人电话
            "birth_date": self.ui.dateEdit.date().toString("yyyy-MM-dd"),  # 出生年月
            "age": self.ui.spinBox.value(),  # 患者年龄
            "admission_date": self.ui.dateEdit_2.date().toString("yyyy-MM-dd"),  # 入院时间
            "discharge_date": self.ui.dateEdit_3.date().toString("yyyy-MM-dd"),  # 出院时间
            "disease_name": self.ui.lineEdit_15.text(),  # 疾病名称
            "hospital_stay_days": self.ui.spinBox_2.value()  # 住院天数
        }

        # 调用数据库查询函数
        try:
            results = get_patients_by_info(search_info)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "查询失败", f"数据库查询失败：{str(e)}")
            return

        # 更新表格显示
        self.update_table(results)


    def update_table(self, results):
        # 清空表格
        self.ui.tableWidget.setRowCount(0)

        # 填充查询结果
        for row_num, row_data in enumerate(results):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
