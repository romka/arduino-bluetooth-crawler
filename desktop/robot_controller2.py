"""
Robot controller interface
author: Roman Arkharov
website: romka.eu
last edited: 29 jan 2012
"""

import sys
from PyQt4 import QtGui, QtCore

from first_screen import FirstScreen
from second_screen import SecondScreen
from third_screen import ThirdScreen
from bt import RobotBt

class RobotController(QtGui.QWidget):
    def __init__(self):
        super(RobotController, self).__init__()
        
        self.main_box = QtGui.QHBoxLayout(self)
        #self.second_box = QtGui.QHBoxLayout(self)
        
        #self.group_box = QtGui.QGroupBox()
        
        self.bt = RobotBt(self)

        self.initUI()
        self.initEvents()

    def initUI(self):
        self.screen = FirstScreen(self)
        
      
        self.setGeometry(300, 300, 600, 400)
        self.main_box.addWidget(self.screen)
        self.setLayout(self.main_box)
        self.setWindowTitle('Robot Controller')
        self.show()
        
    def initEvents(self):
        """
          catch events from all forms
        """
        self.connect(self, QtCore.SIGNAL("find_button_clicked"), self.find_devices) # clicked button "find device" on first screen
        self.connect(self, QtCore.SIGNAL("found_device"), self.found_device) # found device in bt.py
        self.connect(self.bt, QtCore.SIGNAL("finished()"), self.scanning_finished) # finished BT scanning
        self.connect(self.bt, QtCore.SIGNAL("terminated()"), self.scanning_finished) # BT scanning terminated
        
        self.connect(self, QtCore.SIGNAL("next_button_clicked"), self.switch_to_second_screen)
        self.connect(self, QtCore.SIGNAL("device_selected"), self.switch_to_third_screen)
        self.connect(self, QtCore.SIGNAL("service_not_found"), self.if_service_not_found)
        self.connect(self, QtCore.SIGNAL("device_connected"), self.if_device_connected)
    
    def find_devices(self):
        """
          Pressed button "find devices" on first screen (first screen.py)
        """
        #QtGui.QMessageBox.information(self, 'Message', "Find", QtGui.QMessageBox.Ok)
        #self.screen = SecondScreen(self)
        #self.screen.bt_log.clear()
        self.screen.next_btn.setEnabled(False)
        self.screen.find_btn.setEnabled(False)
        self.screen.bt_log.append('Scanning has been started')
        self.bt.start_scan()
        
    def found_device(self):
        """
          This method calling when new BT device is found nearby. Signal sent from bt.py
        """
        #QtGui.QMessageBox.information(self, 'Message', "Found device %s => %s" % (self.bt.current_device[0], self.bt.current_device[1],), QtGui.QMessageBox.Ok)
        self.screen.bt_log.append("Found device %s => %s" % (self.bt.current_device[0], self.bt.current_device[1],))
        
    def scanning_finished(self):
        """
          This method calls when BT scanning is finished or terminated
        """
        self.screen.find_btn.setEnabled(True)
        self.screen.bt_log.append('Scanning has been finished. Found %d devices. Press "next".' % (len(self.bt.devices)))
        self.screen.next_btn.setEnabled(True)
        
    def switch_to_second_screen(self):
        self.screen = SecondScreen(self)
        self.hide()
        
    def switch_to_third_screen(self):
        QtGui.QMessageBox.information(self, 'Message', 'Trying to connect to %s' % self.bt.current_device[1], QtGui.QMessageBox.Ok)
        self.bt.connect()
        self.screen = ThirdScreen(self)
        self.hide()
        
    
    def if_service_not_found(self):
        QtGui.QMessageBox.information(self, 'Message', 'Services on device %s not found' % (self.bt.current_device[1],), QtGui.QMessageBox.Ok)
        
    def if_device_connected(self):
        QtGui.QMessageBox.information(self, 'Message', 'device %s {port: %s, name: %s, host: %s} connected' % (self.bt.current_device[1], self.bt.current_device[2], self.bt.current_device[1], self.bt.current_device[0]), QtGui.QMessageBox.Ok)
      
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = RobotController()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()