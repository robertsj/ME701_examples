import sys
from PyQt5.QtWidgets import QApplication, QLabel
app = QApplication(sys.argv)
widget = QLabel('Hello World!')
widget.show()
app.exec_()
