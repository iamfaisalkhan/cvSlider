# app.y

import cv2

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from imageUI import ImageUI
from controllerUI import ControllerUI

from pipeline import Pipeline
from pipelineThread import PipelineThread

class MainWindow(QMainWindow):
    
    def __init__(self, pipeline = Pipeline):
        super(MainWindow, self).__init__()

        self.pipeline = pipeline

        self._initUI()

    def _initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 1200, 1024)
        self.setWindowTitle('OpenCV-Pipeline')

        self.cvImage = cv2.imread(r'signs_vehicles_xygrad.png')
        self.imageScene = ImageUI(self.cvImage)

        self.setCentralWidget(self.imageScene)

        # Right Dock Widget
        dock = QDockWidget('Controls', self)
        dock.setAllowedAreas(Qt.RightDockWidgetArea)
        self.controller = ControllerUI(self.pipeline)
        dock.setWidget(self.controller)

        self.connect(self.controller, SIGNAL("valueChanged()"), self._updateImage)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def _updateImage(self):
        self.pipelineThread = PipelineThread(self.pipeline)
        self.connect(self.pipelineThread, SIGNAL("finished()"), self._imageReady)
        self.pipelineThread.start()

    def _imageReady(self):
        self.imageScene.updateImage(self.pipeline.getOutput())

