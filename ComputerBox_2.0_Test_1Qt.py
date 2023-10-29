import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, pyqtSlot
import subprocess
from PyQt_Fluent_Styles import dark, light
from PyQt_Fluent_Styles.styles import Fluent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ComputerBox')
        self.setFixedSize(480, 240)
        self.setStyleSheet(Fluent(dark))  # 使用深色主题
        self.initUI()

    def initUI(self):
        # 创建主布局
        layout = QVBoxLayout()

        # 创建按钮
        power_button = QPushButton('电源管理', self)
        power_button.clicked.connect(self.mod1code)
        layout.addWidget(power_button)

        sfc_button = QPushButton('SFC扫描修复', self)
        sfc_button.clicked.connect(self.mod2code)
        layout.addWidget(sfc_button)

        dism_button = QPushButton('DISM操作', self)
        dism_button.clicked.connect(self.mod3code)
        layout.addWidget(dism_button)

        # 创建中心部件并设置布局
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    @pyqtSlot()
    def mod1code(self):
        # mod1的代码
        pass

    @pyqtSlot()
    def mod2code(self):
        # mod2的代码
        pass

    @pyqtSlot()
    def mod3code(self):
        # mod3的代码
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())