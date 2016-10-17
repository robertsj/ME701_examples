#!/usr/bin/python2.7
import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout

class Form(QLabel) :

    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)

        # Define three text boxes, one each for f(x), the value x, and
        # the output.  I've done the first for you.

        self.function_edit = QLineEdit("f(x) = ...")
        self.function_edit.selectAll() # What does selectAll() do?

        # Step 1. Add box for "x"

        # Step 2. Add box for "output"

        # Step 3. How do we combine these widgets?  Use a *layout*....

        # Step 4. Make sure the function box is the default one active.

        # Step 5. Connect updateUI to the event that one returns while the 
        #         output box is active

        # Step 6. Implement updateUI.

        # Step 7. Give the GUI a title.
 

    def updateUI(self) :
        """ Method for updating the user interface.

        This is called whenever an event triggers an update.  Specifically,
        this event is when the return key is pressed when the output box
        is active.  The result of this method should be to show the 
        resulting function value (f of x) in the output box."""

        pass

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
