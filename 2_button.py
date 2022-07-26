import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Hello World!!")
        
        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())
        self.setGeometry(100,100,300,300)
        
        # Create A Label
        my_label = qtw.QLabel("Hello World!")
                
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)
        
        # Create an entry box
        my_entry=qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        self.layout().addWidget(my_entry)
        my_entry.setText("")
        
        # Create a button
        my_button = qtw.QPushButton("Press Me!",clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        # Show the app
        self.show()

        def press_it():
            my_label.setText(f'Hello {my_entry.text()}')

            new_label = qtw.QLabel(f"Hello {my_entry.text()}")
            self.layout().addWidget(new_label)
            my_entry.setText("")


app = qtw.QApplication (sys.argv)
mw = MainWindow()
# Run The App
sys.exit(app.exec_())