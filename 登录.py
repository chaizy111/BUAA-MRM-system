# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


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

        # 身份选择下拉框
        self.label_identity = QtWidgets.QLabel("身份：", self)
        self.label_identity.setGeometry(400, 400, 100, 40)
        self.combo_identity = QtWidgets.QComboBox(self)
        self.combo_identity.setGeometry(500, 400, 300, 40)
        self.combo_identity.addItems(["病人", "医生", "维护"])

        # 证件号输入框
        self.label_id_number = QtWidgets.QLabel("证件号：", self)
        self.label_id_number.setGeometry(400, 500, 100, 40)
        self.input_id_number = QtWidgets.QLineEdit(self)
        self.input_id_number.setGeometry(500, 500, 300, 40)
        self.label_id_number.hide()
        self.input_id_number.hide()

        # 登录按钮
        self.button_login = QtWidgets.QPushButton("登录", self)
        self.button_login.setGeometry(500, 600, 120, 50)

        # 注册按钮
        self.button_register = QtWidgets.QPushButton("注册新用户", self)
        self.button_register.setGeometry(650, 600, 150, 50)

        # 信号连接
        self.combo_identity.currentTextChanged.connect(self.update_id_number_visibility)
        self.button_login.clicked.connect(self.login_action)
        self.button_register.clicked.connect(self.switch_to_register.emit)

    def update_id_number_visibility(self):
        """根据身份选择，显示或隐藏证件号输入框"""
        selected_identity = self.combo_identity.currentText()
        if selected_identity in ["医生", "维护"]:
            self.label_id_number.show()
            self.input_id_number.show()
        else:
            self.label_id_number.hide()
            self.input_id_number.hide()

    def login_action(self):
        """登录按钮的动作"""
        account = self.input_account.text().strip()
        password = self.input_password.text().strip()
        identity = self.combo_identity.currentText()
        id_number = self.input_id_number.text().strip() if identity in ["医生", "维护"] else None

        # 简单验证和输出（可以扩展为后台验证）
        if not account or not password:
            QtWidgets.QMessageBox.warning(self, "提示", "账号和密码不能为空！")
            return

        if identity in ["医生", "维护"] and not id_number:
            QtWidgets.QMessageBox.warning(self, "提示", "证件号不能为空！")
            return

        QtWidgets.QMessageBox.information(self, "登录成功", f"欢迎 {identity}，账号：{account}")


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
        self.label_account.setGeometry(400, 200, 100, 40)
        self.input_account = QtWidgets.QLineEdit(self)
        self.input_account.setGeometry(500, 200, 300, 40)

        # 密码输入框
        self.label_password = QtWidgets.QLabel("新密码：", self)
        self.label_password.setGeometry(400, 300, 100, 40)
        self.input_password = QtWidgets.QLineEdit(self)
        self.input_password.setGeometry(500, 300, 300, 40)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)

        # 注册按钮
        self.button_register = QtWidgets.QPushButton("注册", self)
        self.button_register.setGeometry(500, 400, 120, 50)

        # 返回登录按钮
        self.button_back = QtWidgets.QPushButton("返回登录", self)
        self.button_back.setGeometry(650, 400, 150, 50)

        # 信号连接
        self.button_register.clicked.connect(self.register_action)
        self.button_back.clicked.connect(self.switch_to_login.emit)

    def register_action(self):
        """注册按钮的动作"""
        account = self.input_account.text().strip()
        password = self.input_password.text().strip()

        if not account or not password:
            QtWidgets.QMessageBox.warning(self, "提示", "账号和密码不能为空！")
            return

        QtWidgets.QMessageBox.information(self, "注册成功", f"账号：{account} 已注册成功！")


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
