from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("main.ui", self)

        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.starto = self.findChild(QPushButton,"startover")
        self.counter = 0

        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2)) 
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.starto.clicked.connect(self.reset)

        self.show()

    def win(self):
        x = [self.button1,self.button2,self.button3,self.button4,self.button5,self.button6,self.button7,self.button8,self.button9]
        for n in x:
            n.setEnabled(False)

    def check_win(self):
        if self.button1.text()!="" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            print(f"{self.button1.text()} wins")
            self.win()
        if self.button4.text()!="" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            print(f"{self.button4.text()} wins")
            self.win()
        if self.button7.text()!="" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            print(f"{self.button7.text()} wins")
            self.win()

        if self.button1.text()!="" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            print(f"{self.button1.text()} wins")
            self.win()
        if self.button2.text()!="" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            print(f"{self.button2.text()} wins")
            self.win()
        if self.button3.text()!="" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            print(f"{self.button3.text()} wins")
            self.win()

        if self.button1.text()!="" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            print(f"{self.button1.text()} wins")
            self.win()
        if self.button3.text()!="" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            print(f"{self.button3.text()} wins")
            self.win()

    def clicker(self,a):
        if not self.counter:
            a.setText("X")
            a.setEnabled(False)
            self.counter = 1

        else:
            a.setText("O")
            a.setEnabled(False)
            self.counter = 0

        self.check_win()

    def reset(self):
        x = [self.button1,self.button2,self.button3,self.button4,self.button5,self.button6,self.button7,self.button8,self.button9]
        for n in x:
            n.setText("")
            n.setEnabled(True)
         
app = QApplication(sys.argv)
UIWindow = UI()
sys.exit(app.exec_())