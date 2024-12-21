import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QDialog, QDesktopWidget
)
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter


class PrintDialog(QWidget):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.printer = QPrinter()
        self.initUI()

    def initUI(self):
        # 设置窗口大小
        self.resize(1000, 750)
        # 窗口居中
        self.center()
        # 设置窗口标题
        self.setWindowTitle('打印对话框')

        # 创建文本框组件
        self.editor = QTextEdit(self)
        # 设置位置和大小
        self.editor.setGeometry(20, 20, 500, 500)

        # 创建按钮
        self.openButton = QPushButton('打开文件', self)
        self.openButton.setGeometry(600, 50, 120, 40)

        self.settingsButton = QPushButton('打印设置', self)
        self.settingsButton.setGeometry(600, 120, 120, 40)

        self.printButton = QPushButton('打印文档', self)
        self.printButton.setGeometry(600, 190, 120, 40)

        # 绑定信号槽
        self.openButton.clicked.connect(self.openFile)
        self.settingsButton.clicked.connect(self.showSettingDialog)
        self.printButton.clicked.connect(self.showPrintDialog)

    # 窗口居中
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) // 2,
            (screen.height() - size.height()) // 2
        )

    # 槽方法
    # 打开文件
    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文本文件', './')
        if fname[0]:
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.editor.setText(f.read())

    # 显示打印设置对话框
    def showSettingDialog(self):
        printDialog = QPageSetupDialog(self.printer, self)
        printDialog.exec()

    # 显示打印对话框
    def showPrintDialog(self):
        printdialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printdialog.exec():
            self.editor.print(self.printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PrintDialog()
    gui.show()
    sys.exit(app.exec_())
