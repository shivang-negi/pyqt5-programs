import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Hello World!!")
        
        # Set Vertical layout
        VBoxLayout = qtw.QVBoxLayout()
        self.setLayout(VBoxLayout)
        self.setGeometry(100,100,300,300)
        
        # Create A Label
        my_label = qtw.QLabel("Pick Something!")
                
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        VBoxLayout.addWidget(my_label)
        
        # Create an Combo box
        my_combo = qtw.QComboBox(self,
        editable=True,          #Combo box is editable
        insertPolicy = qtw.QComboBox.InsertAtTop)   #Where to insert new item

        # Add Items To The Combo Box
        my_combo.addItem("Pepperoni", "first")
        my_combo.addItem("Cheese", "Second")
        my_combo.addItem("Mushroom","Third")
        my_combo.addItem("Peppers","Fourth")
        # Put combobox on the screen
        VBoxLayout.addWidget (my_combo)
        
        # Create a button
        my_button = qtw.QPushButton("Press Me!",clicked = lambda: press_it())
        VBoxLayout.addWidget(my_button)
        
        # Show the app
        self.show()

        def press_it():
            my_label.setText(f'You picked {my_combo.currentData()}')

app = qtw.QApplication (sys.argv)
mw = MainWindow()
# Run The App
sys.exit(app.exec_())