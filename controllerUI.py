# -*- coding: utf-8 -*-
# @Author: Faisal Khan
# @Date:   2017-02-16 14:11:13
# @Last Modified by:   Faisal Khan
# @Last Modified time: 2017-02-17 16:58:12

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from sliderUI import SliderUI

from pipeline import Pipeline

class ControllerUI(QWidget):

    def __init__(self, pipeline):
        super(ControllerUI, self).__init__()        

        self.pipeline = pipeline
        self._initUI()

    def _initUI(self):
        blocks = len(self.pipeline.stages)

        main = QVBoxLayout()

        self.btn = QPushButton("Apply Changes", self)
        self.btn.clicked.connect(self._updateClicked)
        toprow = QHBoxLayout()
        toprow.addStretch(1)
        toprow.addWidget(self.btn)
        main.addLayout(toprow)

        for stage in self.pipeline.stages:
            vbox = QVBoxLayout()
            vbox.addWidget(QLabel("Function : %s"%(stage['name'])))
            for param in stage['parameters']:
                if param.isRange():
                    slider = SliderUI(param)
                    vbox.addWidget(slider)
            main.addLayout(vbox)
        
        from qrangeslider import QRangeSlider
        slider = QRangeSlider(self)
        main.addWidget(slider)

        main.addStretch(1)

        self.setLayout(main)

    def _updateClicked(self):
        self.emit(SIGNAL("applyChangesClicked()"))

    def setEnabledApplyChanges(self, state = True):
        self.btn.setEnabled(state)



