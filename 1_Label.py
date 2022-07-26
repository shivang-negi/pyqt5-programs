from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0,500,500)
    win.setWindowTitle("Title")
    label = QLabel(win)
    label.setText("Label")
    label.move(250,250)
    win.show()
    sys.exit(app.exec_())

window()
