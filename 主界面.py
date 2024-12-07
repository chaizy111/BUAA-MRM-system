# -*- coding: utf-8 -*-
import os
import subprocess

# Form implementation generated from reading ui file '主界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 718)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 22))
        self.menubar.setObjectName("menubar")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        self.menu_S = QtWidgets.QMenu(self.menubar)
        self.menu_S.setObjectName("menu_S")
        self.menu_R = QtWidgets.QMenu(self.menubar)
        self.menu_R.setObjectName("menu_R")
        self.menu_X = QtWidgets.QMenu(self.menubar)
        self.menu_X.setObjectName("menu_X")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionb_B = QtWidgets.QAction(MainWindow)
        self.actionb_B.setObjectName("actionb_B")
        self.actiond_D = QtWidgets.QAction(MainWindow)
        self.actiond_D.setObjectName("actiond_D")
        self.actionf_F = QtWidgets.QAction(MainWindow)
        self.actionf_F.setObjectName("actionf_F")
        self.actionh_H = QtWidgets.QAction(MainWindow)
        self.actionh_H.setObjectName("actionh_H")
        self.actione = QtWidgets.QAction(MainWindow)
        self.actione.setCheckable(True)
        self.actione.setChecked(False)
        self.actione.setObjectName("actione")
        self.actiona = QtWidgets.QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.actionb = QtWidgets.QAction(MainWindow)
        self.actionb.setObjectName("actionb")
        self.actionb_2 = QtWidgets.QAction(MainWindow)
        self.actionb_2.setObjectName("actionb_2")
        self.actiong = QtWidgets.QAction(MainWindow)
        self.actiong.setObjectName("actiong")
        self.actionk = QtWidgets.QAction(MainWindow)
        self.actionk.setObjectName("actionk")
        self.actionl = QtWidgets.QAction(MainWindow)
        self.actionl.setObjectName("actionl")
        self.actionm = QtWidgets.QAction(MainWindow)
        self.actionm.setObjectName("actionm")
        self.actionn = QtWidgets.QAction(MainWindow)
        self.actionn.setObjectName("actionn")
        self.actionh = QtWidgets.QAction(MainWindow)
        self.actionh.setObjectName("actionh")
        self.actionk_2 = QtWidgets.QAction(MainWindow)
        self.actionk_2.setObjectName("actionk_2")
        self.actiong_2 = QtWidgets.QAction(MainWindow)
        self.actiong_2.setObjectName("actiong_2")
        self.actionf = QtWidgets.QAction(MainWindow)
        self.actionf.setObjectName("actionf")
        self.actiond = QtWidgets.QAction(MainWindow)
        self.actiond.setObjectName("actiond")
        self.actions = QtWidgets.QAction(MainWindow)
        self.actions.setObjectName("actions")
        self.actiona_2 = QtWidgets.QAction(MainWindow)
        self.actiona_2.setObjectName("actiona_2")
        self.actionb_3 = QtWidgets.QAction(MainWindow)
        self.actionb_3.setObjectName("actionb_3")
        self.actionc = QtWidgets.QAction(MainWindow)
        self.actionc.setObjectName("actionc")
        self.actiond_2 = QtWidgets.QAction(MainWindow)
        self.actiond_2.setObjectName("actiond_2")
        self.actione_2 = QtWidgets.QAction(MainWindow)
        self.actione_2.setObjectName("actione_2")
        self.actionf_2 = QtWidgets.QAction(MainWindow)
        self.actionf_2.setObjectName("actionf_2")
        self.actionw = QtWidgets.QAction(MainWindow)
        self.actionw.setObjectName("actionw")
        self.actiona_3 = QtWidgets.QAction(MainWindow)
        self.actiona_3.setObjectName("actiona_3")
        self.actionchu = QtWidgets.QAction(MainWindow)
        self.actionchu.setObjectName("actionchu")

        # 退出操作的菜单项
        self.actione.setText("退出(&Q)")  # 修改文本为"退出(&Q)"

        self.menu_H.addAction(self.actiona_2)
        self.menu_H.addAction(self.actionb_3)
        self.menu_H.addAction(self.actione_2)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.actionc)
        self.menu_H.addAction(self.actiond_2)
        self.menu_H.addSeparator()
        self.menu_S.addAction(self.actions)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.actiong_2)
        self.menu_S.addAction(self.actionf)
        self.menu_S.addAction(self.actiona_3)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.actionh)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.actionm)
        self.menu_S.addAction(self.actionchu)
        self.menu_R.addAction(self.actiona)
        self.menu_R.addSeparator()
        self.menu_R.addAction(self.actionb_2)
        self.menu_R.addSeparator()
        self.menu_R.addAction(self.actiong)
        self.menu_R.addSeparator()
        self.menu_R.addAction(self.actionl)
        self.menubar.addAction(self.menu_H.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_R.menuAction())
        self.menubar.addAction(self.menu_X.menuAction())

        self.menu_X.addAction(self.actione)

        self.retranslateUi(MainWindow)
        self.connection()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主界面"))
        self.menu_H.setTitle(_translate("MainWindow", "日常业务(&F)"))
        self.menu_S.setTitle(_translate("MainWindow", "信息查询(&S)"))
        self.menu_R.setTitle(_translate("MainWindow", "统计报表(&R)"))
        self.menu_X.setTitle(_translate("MainWindow", "退出系统(&X)"))
        self.actionb_B.setText(_translate("MainWindow", "b(&B)"))
        self.actiond_D.setText(_translate("MainWindow", "d(&D)"))
        self.actionf_F.setText(_translate("MainWindow", "z(&Z)"))
        self.actionh_H.setText(_translate("MainWindow", "h(&H)"))
        self.actione.setText(_translate("MainWindow", "退出(&Q)"))
        self.actiona.setText(_translate("MainWindow", "医疗费用报表"))
        self.actionb.setText(_translate("MainWindow", "疾病分类年龄段报表"))
        self.actionb_2.setText(_translate("MainWindow", "科室就诊情况报表"))
        self.actiong.setText(_translate("MainWindow", "疾病分类年报表"))
        self.actionk.setText(_translate("MainWindow", "门诊动态日报统计表"))
        self.actionl.setText(_translate("MainWindow", "出院病人信息报表"))
        self.actionm.setText(_translate("MainWindow", "入院信息查询"))
        self.actionn.setText(_translate("MainWindow", "出院患者信息查询"))
        self.actionh.setText(_translate("MainWindow", "借阅信息查询"))
        self.actionk_2.setText(_translate("MainWindow", "病案归还信息查询"))
        self.actiong_2.setText(_translate("MainWindow", "疾病信息查询"))
        self.actionf.setText(_translate("MainWindow", "手术信息查询"))
        self.actiond.setText(_translate("MainWindow", "疾病诊断信息查询"))
        self.actions.setText(_translate("MainWindow", "病案检索"))
        self.actiona_2.setText(_translate("MainWindow", "新建病案"))
        self.actionb_3.setText(_translate("MainWindow", "修改病案"))
        self.actionc.setText(_translate("MainWindow", "病案借阅"))
        self.actiond_2.setText(_translate("MainWindow", "病案归还"))
        self.actione_2.setText(_translate("MainWindow", "清除病案"))
        self.actionf_2.setText(_translate("MainWindow", "病案字典维护"))
        self.actionw.setText(_translate("MainWindow", "基本数据维护"))
        self.actiona_3.setText(_translate("MainWindow", "患者信息查询"))
        self.actionchu.setText(_translate("MainWindow", "出院信息查询"))

    def connection(self):
        actions = {
            "actiona_2": "新建病案.py",
            "actionb_3": "修改病案.py",
            "actione_2": "清除病案.py",
            "actionc": "病案借阅.py",
            "actiond_2": "病案归还.py",

            "actions": "病案检索.py",
            "actiong_2": "疾病信息查询.py",
            "actionf": "手术信息查询.py",
            "actiona_3": "患者信息查询.py",
            "actionh": "借阅信息查询.py",
            "actionm": "入院信息查询.py",
            "actionchu": "出院信息查询",

            "actiona": "医疗费用报表.py",
            "actionb_2": "科室就诊情况报表.py",
            "actiong": "疾病分类年报表.py",
            "actionl": "出院病人信息报表.py",
        }

        for action_name, script_name in actions.items():
            action = getattr(self, action_name, None)
            if action:
                action.triggered.connect(lambda _, script=script_name: self.open_script(script))

            # 连接退出操作槽
        self.actione.triggered.connect(self.exit_application)

    def open_script(self, script):

        s_path = os.path.join(os.getcwd(), script)
        if os.path.exists(s_path):
            try:
                subprocess.Popen([sys.executable, s_path])  # 打开新的窗口
            except Exception as e:
                print(f"Error opening script: {e}")
        else:
            print(f"Script not found: {script}")

    def exit_application(self):
        """槽函数，退出应用程序"""
        QtWidgets.QApplication.quit()  # 退出应用程序


from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())