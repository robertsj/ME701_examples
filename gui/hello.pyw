#!/usr/bin/python
import sys
from PyQt4.QtGui import * 
app = QApplication(sys.argv)
widget = QLabel('Hello World!')
# widget = QLabel("<font color=red size=72><b>{0}</b></font>"
#                .format('Hello World'))
# widget.setWindowTitle('Hello')
# widget.resize(250, 150)
# widget.move(600, 300)
widget.show()
app.exec_()
