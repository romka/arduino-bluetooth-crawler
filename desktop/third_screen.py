"""
Robot controller interface. Third screen with platform controls
author: Roman Arkharov
website: romka.eu
last edited: 21 feb 2012
"""

import sys, struct
from PyQt4 import QtGui, QtCore

class ThirdScreen(QtGui.QWidget):
    def __init__(self, parent):
        super(ThirdScreen, self).__init__()
        
        self.parent = parent
        
        self.screen_box = QtGui.QGridLayout(self)
        
        self.left_up_btn = QtGui.QPushButton('left up')
        self.left_stop_btn = QtGui.QPushButton('left stop')
        self.left_down_btn = QtGui.QPushButton('left down')
        
        self.both_up_btn = QtGui.QPushButton('both up')
        self.both_stop_btn = QtGui.QPushButton('both stop')
        self.both_down_btn = QtGui.QPushButton('both down')
        
        self.right_up_btn = QtGui.QPushButton('right up')
        self.right_stop_btn = QtGui.QPushButton('right stop')
        self.right_down_btn = QtGui.QPushButton('right down')
        
        self.initUI()
        self.initEvents()

    def initUI(self):
        self.screen_box.addWidget(self.left_up_btn, 0, 0)
        self.screen_box.addWidget(self.left_stop_btn, 1, 0)
        self.screen_box.addWidget(self.left_down_btn, 2, 0)
        
        self.screen_box.addWidget(self.both_up_btn, 0, 1)
        self.screen_box.addWidget(self.both_stop_btn, 1, 1)
        self.screen_box.addWidget(self.both_down_btn, 2, 1)
        
        self.screen_box.addWidget(self.right_up_btn, 0, 2)
        self.screen_box.addWidget(self.right_stop_btn, 1, 2)
        self.screen_box.addWidget(self.right_down_btn, 2, 2)
        
        
        self.setLayout(self.screen_box)
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Robot Controller. Step 2')
        self.show()
        
        
    def onActivated(self, text):
        for device in self.parent.bt.devices:
            if device[1] == text:
                self.parent.bt.current_device = device
        
    def initEvents(self):
        """
          Events listeners for first screen elements
        """
        # next line emit signal "find_button_clicked" to parent class

        #self.next_btn.clicked.connect(lambda: self.parent.emit(QtCore.SIGNAL("device_selected")))
          
        #self.left_up_btn.clicked.connect(lambda: self.parent.bt.send('1'))
        #self.left_stop_btn.clicked.connect(lambda: self.parent.bt.send('2'))
        #self.left_down_btn.clicked.connect(lambda: self.parent.bt.send('3'))
          
        #self.both_up_btn.clicked.connect(lambda: self.parent.bt.send('4'))
        #self.both_stop_btn.clicked.connect(lambda: self.parent.bt.send('5'))
        #self.both_down_btn.clicked.connect(lambda: self.parent.bt.send('6'))

        #self.right_up_btn.clicked.connect(lambda: self.parent.bt.send('7'))
        #self.right_stop_btn.clicked.connect(lambda: self.parent.bt.send('8'))
        #self.right_down_btn.clicked.connect(lambda: self.parent.bt.send('9'))

        self.left_up_btn.clicked.connect(lambda: self.prepare_bt_data(1))
        self.left_stop_btn.clicked.connect(lambda: self.prepare_bt_data(2))
        self.left_down_btn.clicked.connect(lambda: self.prepare_bt_data(3))
          
        self.both_up_btn.clicked.connect(lambda: self.prepare_bt_data(4))
        self.both_stop_btn.clicked.connect(lambda: self.prepare_bt_data(5))
        self.both_down_btn.clicked.connect(lambda: self.prepare_bt_data(6))

        self.right_up_btn.clicked.connect(lambda: self.prepare_bt_data(7))
        self.right_stop_btn.clicked.connect(lambda: self.prepare_bt_data(8))
        self.right_down_btn.clicked.connect(lambda: self.prepare_bt_data(9))
          
    def prepare_bt_data(self, command):
      data = []
      data.append(command)
      data.append(255)
      self.parent.bt.send(struct.pack('i'*len(data), *data))
    
    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Q:
          self.parent.bt.send('1')
        elif key == QtCore.Qt.Key_A:
          self.parent.bt.send('2')
        elif key == QtCore.Qt.Key_Z:
          self.parent.bt.send('3')
        elif key == QtCore.Qt.Key_W:
          self.parent.bt.send('4')
        elif key == QtCore.Qt.Key_S:
          self.parent.bt.send('5')
        elif key == QtCore.Qt.Key_X:
          self.parent.bt.send('6')
        elif key == QtCore.Qt.Key_E:
          self.parent.bt.send('7')
        elif key == QtCore.Qt.Key_D:
          self.parent.bt.send('8')
        elif key == QtCore.Qt.Key_C:
          self.parent.bt.send('9')