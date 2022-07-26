from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 40, 731, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.additem())
        self.pushButtonAdd.setGeometry(QtCore.QRect(30, 100, 121, 41))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.deleteitem())
        self.pushButton_delete.setGeometry(QtCore.QRect(160, 100, 121, 41))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.clearitems())
        self.pushButton_clear.setGeometry(QtCore.QRect(290, 100, 121, 41))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 180, 731, 351))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def additem(self):
        txt = self.textEdit.toPlainText()
        self.listWidget.addItem(txt)
        self.textEdit.setText("")

    def deleteitem(self):
        clicked = self.listWidget.currentRow()
        self.listWidget.takeItem(clicked)

    def clearitems(self):
        self.listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TODOLIST"))
        self.pushButtonAdd.setText(_translate("MainWindow", "Add to list"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete from List"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
