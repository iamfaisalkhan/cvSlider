# -*- coding: utf-8 -*-
# @Author: Faisal Khan
# @Date:   2017-02-16 14:11:13
# @Last Modified by:   Faisal Khan
# @Last Modified time: 2017-02-16 16:39:51

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ControllerUI(QWidget):

    def __init__(self):
        super(ControllerUI, self).__init__()

        self.initUI()

    def initUI(self):

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.valueChanged[int].connect(self.changeValue)
        self.sld.setRange(0, 255)

        self.textValue = QLineEdit(self)
        self.textValue.setText("0")

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Min Thresh:"))
        hbox.addWidget(self.sld)
        hbox.addWidget(self.textValue)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def changeValue(self, value):
        self.textValue.setText("%d"%(value))




