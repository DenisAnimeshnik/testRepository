# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QVBoxLayout, QApplication

import sys

sc_size = (400, 240)

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        v_line = QVBoxLayout()
        test_label = QLabel("asd")
        self.setCentralWidget(test_label)

        self.resize(*sc_size)
        self.show()

def application():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()