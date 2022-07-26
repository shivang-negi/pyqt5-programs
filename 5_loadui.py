from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("load.ui", self)

		# Define Our Widgets
		self.label = self.findChild(QLabel, "label")
		self.textedit = self.findChild(QLineEdit, "lineEdit")
		self.button = self.findChild(QPushButton, "pushButton")

		# Do something
		self.button.clicked.connect(self.clicker)

		# Show The App
		self.show()
	
	def clicker(self):
		self.label.setText(f'Hello There {self.textedit.text()}')
		self.textedit.setText("");

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()