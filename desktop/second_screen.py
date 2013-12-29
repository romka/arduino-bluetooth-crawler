"""
Robot controller interface. Second screen with found devices
author: Roman Arkharov
website: romka.eu
last edited: 29 jan 2012
"""

import sys
from PyQt4 import QtGui, QtCore

class SecondScreen(QtGui.QWidget):
    def __init__(self, parent):
        super(SecondScreen, self).__init__()
        
        self.parent = parent
        
        self.screen_box = QtGui.QVBoxLayout(self)
        
        self.combo = QtGui.QComboBox(self)
        for device in self.parent.bt.devices:
          self.combo.addItem(device[1])
        
        self.parent.bt.current_device = self.parent.bt.devices[0]
        
        self.combo.activated[str].connect(self.onActivated)  
        
        self.next_btn = QtGui.QPushButton('Next step')
        
        self.initUI()
        self.initEvents()

    def initUI(self):
        self.screen_box.addWidget(self.combo)
        self.screen_box.addWidget(self.next_btn)
        
        self.setLayout(self.screen_box)
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Robot Controller. Step 2')
        self.show()
        
        
    def onActivated(self, text):
        for device in self.parent.bt.devices:
            if device[1] == text:
                # see to bt.py
                self.parent.bt.current_device = device
        
    def initEvents(self):
        """
          Events listeners for first screen elements
        """
        # next line emit signal "find_button_clicked" to parent class

        self.next_btn.clicked.connect(lambda: self.parent.emit(QtCore.SIGNAL("device_selected")))
