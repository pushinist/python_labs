from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Вычисление выражений")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()


        self.textbox1 = QLineEdit()        
        self.label1 = QLabel('Выражение')

        layout2.addWidget(self.label1)
        layout2.addWidget(self.textbox1)

        layout1.addLayout(layout2)


        self.button = QPushButton('->')
        self.button.setFixedSize(40, 30)
        self.button.clicked.connect(self.clicked)

        layout1.addWidget(self.button)


        self.textbox2 = QLineEdit()
        self.label2 = QLabel('Результат')

        layout3.addWidget(self.label2)
        layout3.addWidget(self.textbox2)


        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


    def clicked(self):
        try:
            self.textbox2.setText(str(eval(self.textbox1.text())))
            self.textbox1.clear()
        except:
            self.textbox2.setText('Error!!!!!')
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
