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
        self.initUI()

    def initUI(self):
        blocks = len(self.pipeline.stages)

        main = QVBoxLayout()

        for stage in self.pipeline.stages:
            # print ("\nFunction\n\t %s"%stage['name'])
            vbox = QVBoxLayout()
            vbox.addWidget(QLabel("Function : %s"%(stage['name'])))

            
            # if len(stage['parameters']) > 0:
            #     print("Args\n\t")

            for param in stage['parameters']:
                if param.isRange():
                    slider = SliderUI(param)
                    vbox.addWidget(slider)
                    
                # print("\t %s:%s"%(param.name, param.value))
            main.addLayout(vbox)
            # print()

        
        main.addStretch(1)

        self.setLayout(main)

    def changeValue(self, value):
        self.textValue.setText("%d"%(value))




