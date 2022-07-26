from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("dialog.ui", self)

        # Define Our Widgets
        self.label = self.findChild(QLabel, "label")
        self.button = self.findChild(QPushButton, "pushButton")

        self.button.clicked.connect(self.clicker)
        self.show()
    
    def clicker(self):
        fname = QFileDialog.getOpenFileName(self,"open file")
        if fname:
            self.label.setText(str(fname[0]))


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()