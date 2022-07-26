from tabnanny import check
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5 import uic
import sys
from authentication import check_details

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("login.ui", self)

        self.user_label = self.findChild(QLabel, "username_label")
        self.pass_label = self.findChild(QLabel,"password_label")
        self.username = self.findChild(QLineEdit,"username")
        self.password = self.findChild(QLineEdit,"password")
        self.login_button = self.findChild(QPushButton,"login")
        self.newuser = self.findChild(QPushButton,"newuser")
        self.incorrect = self.findChild(QLabel,"incorrect")
        self.password.setEchoMode(QLineEdit.Password)

        self.login_button.clicked.connect(lambda: self.authenticate(self.username,self.password))

    def authenticate(self,username,password):
        x = check_details(username.text(),password.text())
        if not x:
            self.incorrect.setText("Enter valid details")
            return
        main = Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex() + 1)
         
class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("main.ui", self)
        self.logout = self.findChild(QPushButton,"logout")

        self.logout.clicked.connect(lambda:self.goback())

    def goback(self):
        # login = Login()
        # widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()-1)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
login = Login()

widget.addWidget(login)
widget.setFixedWidth(720)
widget.setFixedHeight(405)
widget.show()
sys.exit(app.exec_())