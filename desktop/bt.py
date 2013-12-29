"""
Robot controller interface. Bluetooth connection functions
author: Roman Arkharov
website: romka.eu
last edited: 29 jan 2012
"""

import sys
from bluetooth import *
from PyQt4 import QtCore

class RobotBt(QtCore.QThread):
    def __init__(self, parent):
        QtCore.QThread.__init__(self, parent)
        #super(RobotBt, self).__init__()
        
        self.parent = parent
        self.devices = []
        self.current_device = []
        self.service_matches = []
        self.sock = BluetoothSocket( RFCOMM )
        self.device_info = {}
        self.port = 1

    def start_scan(self):
        self.start()
        
    def run(self):
        self.devices = []
        self.current_device = []
        nearby_devices = discover_devices()
        counter = 0
        
        for bdaddr in nearby_devices:
            name = lookup_name( bdaddr )
            self.devices.append([bdaddr, name, self.port])
            counter = counter + 1
            
            self.current_device = [bdaddr, name, self.port] # this will be accessable in slot function
            self.parent.emit(QtCore.SIGNAL("found_device"))
            
            """
            if counter == 0:
                self.bt_log.append("could not find target bluetooth device nearby")
            
            for addr, name in self.devices:
                self.bt_log.append("Services for %s => %s" % (addr, name,))
                services = find_service(None, None, addr)
            """
    def connect(self):
        service_matches = find_service( address = self.current_device[0] )
        #if len(service_matches) == 0:
        #    self.parent.emit(QtCore.SIGNAL("service_not_found"))
        #    sys.exit(0)
        
        #first_match = service_matches[0]
        #self.device_info['port'] = first_match["port"]
        #self.device_info['name'] = first_match["name"]
        #self.device_info['host'] = first_match["host"]
        
        self.parent.emit(QtCore.SIGNAL("device_connected"))
        #self.sock.connect((self.device_info['host'], self.device_info['port']))
        self.sock.connect((self.current_device[0], self.current_device[2]))
        #self.send('111')
        
        #sock.send("hello!!")
        #sock.close()
    
    def send(self, data):
        self.sock.send(data)
        
    def colse(self):
        self.close()
