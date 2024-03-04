from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.flag = True

    def initUI(self):
        
        self.setFixedSize(400, 100)
        self.setWindowTitle("Фокус со словами")
        self.layout = QHBoxLayout(self)
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.button = QPushButton('->')
        self.button.setFixedSize(40, 30)
        self.button.clicked.connect(self.clicked)
        self.layout.addWidget(self.textbox1)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.textbox2)
    
    def clicked(self):
        if self.flag == True:
            self.button.setText("<-")
            self.flag = False
            self.textbox2.setText(self.textbox1.text())
            self.textbox1.clear()
        else:
            self.button.setText("->")
            self.flag = True
            self.textbox1.setText(self.textbox2.text())
            self.textbox2.clear()

app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())   
