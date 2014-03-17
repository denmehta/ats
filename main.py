def __init__(self):
  traySignal = "activated(QSystemTrayIcon::ActivationReason)"
  QtCore.QObject.connect(self.trayIcon, QtCore.SIGNAL(traySignal), self.__icon_activated)
 
def closeEvent(self, event):
  if self.okayToClose():
    
    self.trayIcon.hide()
    event.accept()
  else:
   
    self.hide()
    self.trayIcon.show()
    event.ignore()
 
def __icon_activated(self, reason):
  if reason == QtGui.QSystemTrayIcon.DoubleClick:
    self.show()
       
    self.connect(self.icon, SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.iconClicked)
       
    self.connect(self.icon, SIGNAL("activated(QSystemTrayIcon.ActivationReason)"), self.iconClicked)
       
def create_sys_tray(self):
    self.sysTray = QtGui.QSystemTrayIcon(self)
    self.sysTray.setIcon( QtGui.QIcon('w:\icon.png') )
    self.sysTray.setVisible(True)
    self.connect(self.sysTray, QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.on_sys_tray_activated)
 
    self.sysTrayMenu = QtGui.QMenu(self)
    act = self.sysTrayMenu.addAction("FOO")
 

       
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout,QSystemTrayIcon
 
class Example(QtGui.QWidget):
    def __init__(self):
            super(Example, self).__init__()        
            self.initUI()
 
    def initUI(self):              
        self.icon=QSystemTrayIcon()
        r=self.icon.isSystemTrayAvailable()
        self.icon.setIcon( QtGui.QIcon('w:\icon.png') )
        self.icon.show()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QtGui.QIcon('w:\icon.png'))          
        self.setWindowTitle('Message box')    
        self.show()
        self.icon.activated.connect(self.activate)
        self.show()        
        self.icon.menu = QtGui.QMenu()
        exitAction = self.icon.menu.addAction("Exit")
        self.icon.setContextMenu(self.icon.menu)
        self.connect(exitAction, QtCore.SIGNAL('triggered()'),QtGui.qApp, QtCore.SLOT('quit()'))

        
        
    def closeEvent(self, event):
 
 
            reply = QtGui.QMessageBox.question(self, 'Message',"Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
 
            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                self.icon.show()
 
                self.hide()
 
 
                event.ignore()      
    def activate(self,reason ):
        # print reason
        if reason==2:
            self.show()
 
 
 
    def __icon_activated(self, reason):
              if reason == QtGui.QSystemTrayIcon.DoubleClick:
                self.show()  
def main():
 
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
 
 
if __name__ == '__main__':
    main()