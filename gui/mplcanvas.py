#!/usr/bin/python
from __future__ import division
import sys
import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QApplication, QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MatplotlibCanvas(FigureCanvas) :
    """ This is borrowed heavily from the matplotlib documentation;
        specifically, see:
        http://matplotlib.org/examples/user_interfaces/embedding_in_qt5.html
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100) :
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
      
    def compute_initial_figure(self):
        self.x = np.arange(0.0, 3.0, 0.01)
        self.y = np.sin(2*np.pi*self.x)
        self.axes.plot(self.x, self.y)
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y(x)')    
        
    def redraw(self, x, y) :
        self.axes.plot(x, y)
        self.draw()    
        
app = QApplication(sys.argv)
widget = MatplotlibCanvas()
widget.show()
app.exec_()
