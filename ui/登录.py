# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from db.login_op import sign, login
from ui.主界面 import Ui_MainWindow1

class LoginWindow(QtWidgets.QWidget):
    switch_to_register = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("登录界面")
        self.resize(1200, 1000)

        # 账号输入框
        self.label_account = QtWidgets.QLabel("账号：", self)
        self.label_account.setGeometry(400, 200, 100, 40)
        self.input_account = QtWidgets.QLineEdit(self)
        self.input_account.setGeometry(500, 200, 300, 40)

        # 密码输入框
        self.label_password = QtWidgets.QLabel("密码：", self)
        self.label_password.setGeometry(400, 300, 100, 40)
        self.input_password = QtWidgets.QLineEdit(self)
        self.input_password.setGeometry(500, 300, 300, 40)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)

        # 登录按钮
        self.button_login = QtWidgets.QPushButton("登录", self)
        self.button_login.setGeometry(500, 400, 120, 50)

        # 注册按钮
        self.button_register = QtWidgets.QPushButton("注册新用户", self)
        self.button_register.setGeometry(650, 400, 150, 50)

        # 信号连接
        self.button_login.clicked.connect(self.login_action)
        self.button_register.clicked.connect(self.switch_to_register.emit)

    def login_action(self):
        """登录按钮的动作"""
        account = self.input_account.text().strip()
        password = self.input_password.text().strip()

        if not account or not password:
            QtWidgets.QMessageBox.warning(self, "提示", "账号和密码不能为空！")
            return

        if login(account, password):
            QtWidgets.QMessageBox.information(self, "登录成功", f"欢迎登录，账号：{account}")
            self.close()


            self.main_window1 = QtWidgets.QMainWindow()  # 创建主窗口实例
            self.ui1 = Ui_MainWindow1()  # 创建 Ui_MainWindow 类的实例
            self.ui1.setupUi(self.main_window1)  # 设置主界面的UI
            self.main_window1.resize(1600, 1200)
            self.main_window1.show()

        else:
            QtWidgets.QMessageBox.warning(self, "登录失败", "账号或密码错误！")
class RegisterWindow(QtWidgets.QWidget):
    switch_to_login = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("注册界面")
        self.resize(1200, 1000)

        # 账号输入框
        self.label_account = QtWidgets.QLabel("新账号：", self)
        self.label_account.setGeometry(400, 150, 100, 40)
        self.input_account = QtWidgets.QLineEdit(self)
        self.input_account.setGeometry(500, 150, 300, 40)

        # 密码输入框
        self.label_password = QtWidgets.QLabel("新密码：", self)
        self.label_password.setGeometry(400, 250, 100, 40)
        self.input_password = QtWidgets.QLineEdit(self)
        self.input_password.setGeometry(500, 250, 300, 40)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)

        # 身份选择下拉框
        self.label_identity = QtWidgets.QLabel("身份：", self)
        self.label_identity.setGeometry(400, 350, 100, 40)
        self.combo_identity = QtWidgets.QComboBox(self)
        self.combo_identity.setGeometry(500, 350, 300, 40)
        self.combo_identity.addItems(["病人", "医生"])

        # 医生专属输入框
        self.label_department = QtWidgets.QLabel("科室名：", self)
        self.label_department.setGeometry(400, 450, 100, 40)
        self.input_department = QtWidgets.QLineEdit(self)
        self.input_department.setGeometry(500, 450, 300, 40)
        self.label_department.hide()
        self.input_department.hide()

        self.label_id_number = QtWidgets.QLabel("证件号：", self)
        self.label_id_number.setGeometry(400, 550, 100, 40)
        self.input_id_number = QtWidgets.QLineEdit(self)
        self.input_id_number.setGeometry(500, 550, 300, 40)
        self.label_id_number.hide()
        self.input_id_number.hide()

        self.label_name = QtWidgets.QLabel("姓名：", self)
        self.label_name.setGeometry(400, 650, 100, 40)
        self.input_name = QtWidgets.QLineEdit(self)
        self.input_name.setGeometry(500, 650, 300, 40)
        self.label_name.hide()
        self.input_name.hide()

        # 注册按钮
        self.button_register = QtWidgets.QPushButton("注册", self)
        self.button_register.setGeometry(500, 750, 120, 50)

        # 返回登录按钮
        self.button_back = QtWidgets.QPushButton("返回登录", self)
        self.button_back.setGeometry(650, 750, 150, 50)

        # 信号连接
        self.combo_identity.currentTextChanged.connect(self.update_doctor_fields_visibility)
        self.button_register.clicked.connect(self.register_action)
        self.button_back.clicked.connect(self.switch_to_login.emit)

    def update_doctor_fields_visibility(self):
        """根据身份选择显示或隐藏医生专属输入框"""
        if self.combo_identity.currentText() == "医生":
            self.label_department.show()
            self.input_department.show()
            self.label_id_number.show()
            self.input_id_number.show()
            self.label_name.show()
            self.input_name.show()
        else:
            self.label_department.hide()
            self.input_department.hide()
            self.label_id_number.hide()
            self.input_id_number.hide()
            self.label_name.hide()
            self.input_name.hide()

    def register_action(self):
        """注册按钮的动作"""
        account = self.input_account.text().strip()
        password = self.input_password.text().strip()
        identity = self.combo_identity.currentText()

        if not account or not password:
            QtWidgets.QMessageBox.warning(self, "提示", "账号和密码不能为空！")
            return

        if identity == "医生":
            department = self.input_department.text().strip()
            id_number = self.input_id_number.text().strip()
            name = self.input_name.text().strip()

            if not department or not id_number or not name:
                QtWidgets.QMessageBox.warning(self, "提示", "医生信息不能为空！")
                return

            success = sign(account, password, is_patient=False, is_doctor=True, name=name, id_number=id_number,
                           department_name=department)
        else:
            success = sign(account, password, is_patient=True, is_doctor=False, name=None, id_number=None,
                           department_name=None)

        if success:
            QtWidgets.QMessageBox.information(self, "注册成功", "您的账号已成功注册！")
        else:
            QtWidgets.QMessageBox.warning(self, "注册失败", "注册失败，可能是信息填写有误或账号已存在！")


class MainApplication(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.login_window = LoginWindow()
        self.register_window = RegisterWindow()

        self.addWidget(self.login_window)
        self.addWidget(self.register_window)

        # 切换信号
        self.login_window.switch_to_register.connect(lambda: self.setCurrentWidget(self.register_window))
        self.register_window.switch_to_login.connect(lambda: self.setCurrentWidget(self.login_window))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApplication()
    main_app.setWindowTitle("用户管理系统")
    main_app.resize(1200, 1000)
    main_app.show()
    sys.exit(app.exec_())
