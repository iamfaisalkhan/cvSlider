# app.y

import cv2

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from imageUI import ImageUI
from controllerUI import ControllerUI

from pipeline import Pipeline

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, Pipeline):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 1200, 1024)
        self.setWindowTitle('OpenCV-pipeline')
        #self.setWindowIcon(QtGui.QIcon('test.png'))

        self.cvImage = cv2.imread(r'signs_vehicles_xygrad.png')
        self.imageScene = ImageUI(self.cvImage)

        self.setCentralWidget(self.imageScene)

        # Right Dock Widget
        dock = QtGui.QDockWidget('Controls', self)
        dock.setAllowedAreas(Qt.RightDockWidgetArea)
        controllerWidget = ControllerUI()
        dock.setWidget(controllerWidget)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        self.show()
