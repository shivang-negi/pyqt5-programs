from email.mime import image
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("image.ui", self)

        self.label = self.findChild(QLabel, "label")
        self.button = self.findChild(QPushButton, "pushButton")

        self.button.clicked.connect(self.clicker)
        self.show()
    
    def clicker(self):
        fname = QFileDialog.getOpenFileName(self,"open file","C://Users//ACER//workspace//GUI practice//images")
        self.image = QPixmap(fname[0])
        self.label.setPixmap(self.image)


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()