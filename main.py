from PyQt5 import QtCore, QtGui, QtWidgets

from db.login_op import sign, login
from ui.登录 import MainApplication

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApplication()
    main_app.setWindowTitle("用户管理系统")
    main_app.resize(1000, 800)
    main_app.show()
    sys.exit(app.exec_())