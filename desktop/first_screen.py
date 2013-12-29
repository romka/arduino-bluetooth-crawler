"""
Robot controller interface. First screen with "find devices" button
author: Roman Arkharov
website: romka.eu
last edited: 29 jan 2012
"""

import sys
from PyQt4 import QtGui, QtCore

class FirstScreen(QtGui.QWidget):
    def __init__(self, parent):
        super(FirstScreen, self).__init__()
        
        self.parent = parent
        
        self.screen_box = QtGui.QVBoxLayout(self)
        
        self.label = QtGui.QLabel('Press button for scan BT devices nearby')
        self.find_btn = QtGui.QPushButton('Find BT devices')
        self.bt_log = QtGui.QTextEdit("Here'll be BT connection log")
        self.bt_log.setReadOnly(True)
        
        self.next_btn = QtGui.QPushButton('Next step')
        self.next_btn.setEnabled(False);

        self.initUI()
        self.initEvents()

    def initUI(self):
        self.screen_box.addWidget(self.label)
        self.screen_box.addWidget(self.find_btn)
        self.screen_box.addWidget(self.bt_log)
        self.screen_box.addWidget(self.next_btn)
        
        self.setLayout(self.screen_box)
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Robot Controller')
        self.show()
        
        
        """
        # code below emit signal to current class
        self.find_btn.clicked.connect(lambda: self.emit(QtCore.SIGNAL("find_button_clicked")))
        self.find_btn.clicked.connect(lambda: QtGui.QMessageBox.information(self, 'Message', "111", QtGui.QMessageBox.Ok))
        self.connect(self, QtCore.SIGNAL("find_button_clicked"), lambda: QtGui.QMessageBox.information(self, 'Message', "222", QtGui.QMessageBox.Ok))
        """
        
    def initEvents(self):
        """
          Events listeners for first screen elements
        """
        # next line emit signal "find_button_clicked" to parent class
        self.find_btn.clicked.connect(lambda: self.parent.emit(QtCore.SIGNAL("find_button_clicked")))
          
        self.next_btn.clicked.connect(lambda: self.parent.emit(QtCore.SIGNAL("next_button_clicked")))