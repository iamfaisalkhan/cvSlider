# -*- coding: utf-8 -*-
# @Author: Faisal Khan
# @Date:   2017-02-16 14:11:13
# @Last Modified by:   Faisal Khan
# @Last Modified time: 2017-02-20 13:17:35

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

        toprow = QHBoxLayout()
        toprow.addStretch(1)
        main.addLayout(toprow)

        for stage in self.pipeline.stages:
            vbox = QVBoxLayout()
            vbox.addWidget(QLabel("Function : %s"%(stage['name'])))
            for param in stage['parameters']:
                if param.isRange():
                    slider = SliderUI(param)
                    self.connect(slider, SIGNAL("valueChanged()"), self._handleValueChange)
                    vbox.addWidget(slider)
            main.addLayout(vbox)
        
        main.addStretch(1)

        self.setLayout(main)

    def _handleValueChange(self):
        self.emit(SIGNAL("valueChanged()"))

