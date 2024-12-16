# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys

from db.search_op import search_disease_info, search_return_info
from intermediate_data_structure.search_info import SearchInfo


class Ui_MainWindow2(object):

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
            "病历号", "患者姓名", "性别", "入院时间", "出院科室",
            "住院天数", "诊断类型", "疾病编码", "疾病名称"
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
        MainWindow.setWindowTitle(_translate("MainWindow", "查询条件2"))
        #self.pushButton.setText(_translate("MainWindow", "查询[&S]"))
        #self.pushButton_2.setText(_translate("MainWindow", "关闭[&E]"))



class Ui_MainWindow(object):
    """疾病信息查询主界面"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(410, 40, 320, 80))
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
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_7.addWidget(self.label_29)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.horizontalLayout_7.addWidget(self.lineEdit_20)
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
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_7.addWidget(self.label_28)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_7.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_7.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_7.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 350, 700, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels([
            "病历号", "患者姓名", "性别", "出生年月", "科室名", "住院时长",
             "疾病编码", "疾病名称"
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
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.openQueryDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "疾病信息查询"))
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
        self.label_18.setText(_translate("MainWindow", "出生年月："))
        self.label_19.setText(_translate("MainWindow", "——"))
        self.label_24.setText(_translate("MainWindow", "患者年龄"))
        self.label_25.setText(_translate("MainWindow", "岁"))
        self.label_21.setText(_translate("MainWindow", "入院时间："))
        self.label_22.setText(_translate("MainWindow", "——"))
        self.label_23.setText(_translate("MainWindow", "出院时间："))
        self.label_20.setText(_translate("MainWindow", "——"))
        self.label_29.setText(_translate("MainWindow", "入院科室："))
        self.label_27.setText(_translate("MainWindow", "出院科室："))
        self.label_26.setText(_translate("MainWindow", "疾病名称："))
        self.label_28.setText(_translate("MainWindow", "诊断类型："))
        self.checkBox.setText(_translate("MainWindow", "门诊诊断"))
        self.checkBox_2.setText(_translate("MainWindow", "出院主要诊断"))
        self.checkBox_3.setText(_translate("MainWindow", "病理诊断"))
        self.lineEdit.setText("1")
        self.lineEdit_4.setText("4")
        self.lineEdit_5.setText("5")
        self.lineEdit_20.setText("20")
        self.lineEdit_17.setText("17")
        self.lineEdit_19.setText("19")
        self.lineEdit_18.setText("18")

    def openQueryDialog(self):

        search_info = {
            "medical_record_number": self.lineEdit.text(),  # 假设病历号是lineEdit控件
            "patient_name": self.lineEdit_4.text(),  # 假设患者姓名是lineEdit_4控件
            "gender": self.lineEdit_5.text(),
            "disease_name": self.lineEdit_18.text(),
            "unit_name": self.lineEdit_20.text(),
            "admission_date_from": self.dateTimeEdit_6.dateTime().toString('yyyy-MM-dd'),  # 入院时间开始
            "admission_date_to": self.dateTimeEdit_4.dateTime().toString('yyyy-MM-dd'),  # 入院时间结束
            "discharge_date_from": self.dateTimeEdit_5.dateTime().toString('yyyy-MM-dd'),  # 出院时间开始
            "discharge_date_to": self.dateTimeEdit_3.dateTime().toString('yyyy-MM-dd'),  # 出院时间结束
        }

        search_info = {k: v for k, v in search_info.items() if len(v) > 0}

        # 调用查询函数，将字典传递给查询函数
        records = search_disease_info(**search_info)

            # 清空现有表格内容
        self.tableWidget.setRowCount(0)

            # 将查询结果插入到表格中
        for row_number, record in enumerate(records):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(record):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
