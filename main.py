#!/usr/bin/python
# -*- coding: cp1251 -*-

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
from PyQt4 import QtGui, QtCore,QtNetwork
from PyQt4.QtNetwork import *
# from PyQt4.QtNetwork import QUdpSocket
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout,QSystemTrayIcon
import webbrowser
import MySQLdb
# import socket
 
class RedLabel(QtGui.QLabel):
    def __init__(self,text):
        QtGui.QLabel.__init__(self)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setBold(True)
        self.setFont(font)
        self.setText(text)
        self.setStyleSheet("QLabel { color : red; }")
 

class LineEdit(QtGui.QLineEdit):
    def __init__(self):
        QtGui.QLineEdit.__init__(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
 
 
class Example(QtGui.QWidget):
    def __init__(self):
            super(Example, self).__init__()        
            self.initUI()
    def openApex(self):
        
        if self.call_id:
            webbrowser.open("http://tca-db1.astrakhan.businesscar.ru:8080/apex/f?p=999:1:0::NO:1:P1_ID_CUSTOMER:"+self.customer_id)
     
    def openCrm(self):
        
        if self.customer_id:
           
            webbrowser.open("http://tca-crm/sugar/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DCalls%26offset%3D15%26stamp%3D1395146164095815300%26return_module%3DCalls%26action%3DDetailView%26record%3D"+self.call_id)
    
    
 
    def initUI(self):              
        self.icon=QSystemTrayIcon()
        r=self.icon.isSystemTrayAvailable()
        self.customer_id=""
        self.call_id = ""
        self.icon.setIcon( QtGui.QIcon('w:\icon.png') )
        self.icon.show()
        self.setGeometry(350, 30, 640, 480)
        self.setWindowIcon(QtGui.QIcon('w:\icon.png'))          
        self.setWindowTitle(u'CallCenter')    
        self.show()
        self.icon.activated.connect(self.activate)
        self.show()        
        self.icon.menu = QtGui.QMenu()
        exitAction = self.icon.menu.addAction(u"Выход")
        self.icon.setContextMenu(self.icon.menu)
        self.connect(exitAction, QtCore.SIGNAL('triggered()'),QtGui.qApp, QtCore.SLOT('quit()'))
        
        general_groupbox = QtGui.QGroupBox(u"Общая информация",self)
        general_groupbox.show()
        
        self.title_label = RedLabel(u"Название:")
        surname_label = QtGui.QLabel(u"Фамилия:")
        name_label = QtGui.QLabel(u"Имя:")
        secondName_label = QtGui.QLabel(u"Отчество:")
        clientType_label = RedLabel(u"Тип клиента:")
        gender_label = RedLabel(u"Пол:")
        burthday_label = RedLabel(u"Дата рождения:")
        regDate_label = QtGui.QLabel(u"Дата рег-ции:")
        
        
        phone_label = QtGui.QLabel(u"Тел.:")
        mobilePhone_label = QtGui.QLabel(u"Моб. тел.:")
        fax_label = QtGui.QLabel(u"Факс:")
        indexCity_label = QtGui.QLabel(u"Индекс\Город:")
        address_label = QtGui.QLabel(u"Адрес:")
        
        
        
        self.phone_text = LineEdit()
        mobilePhone_text = LineEdit()
        fax_text = LineEdit()
        indexCity_text = LineEdit()
        address_text = LineEdit()
        
        
        
        
        
        self.title_text = LineEdit()
        surname_text = LineEdit()
        name_text = LineEdit()
        secondName_text = LineEdit()
        clientType_text = LineEdit()
        clientCode_text = LineEdit()
        brunch_text = LineEdit()
        transport_text = LineEdit()
        paymentType_text = LineEdit()
        maxSale_text = LineEdit()
        gender_text = LineEdit()
        burthday_text = LineEdit()
        regDate_text = LineEdit()
        lastVisit_text = LineEdit()
        
       
       
       
       
        general_layoutBox = QtGui.QGridLayout(self)
        general_layoutBox.setSpacing(10)
        general_layoutBox.setColumnMinimumWidth(0,0)
        general_layoutBox.addWidget(self.title_label,0,0)
        general_layoutBox.addWidget(self.title_text,0,1)
        general_layoutBox.addWidget(surname_label)  
        general_layoutBox.addWidget(surname_text)  
        general_layoutBox.addWidget(name_label)         
        general_layoutBox.addWidget(name_text)
        general_layoutBox.addWidget(secondName_label)    
        general_layoutBox.addWidget(secondName_text)
        general_layoutBox.addWidget(clientType_label)         
        general_layoutBox.addWidget(clientType_text) 
        general_layoutBox.addWidget(gender_label)        
        general_layoutBox.addWidget(gender_text)  
        general_layoutBox.addWidget(burthday_label)          
        general_layoutBox.addWidget(burthday_text) 
        general_layoutBox.addWidget(regDate_label)         
        general_layoutBox.addWidget(regDate_text)    
        general_groupbox.setLayout(general_layoutBox)
        
        
        personal_groupbox = QtGui.QGroupBox(u"Персональные настройки",self)
        personal_groupbox.show()
        self.apex_button = QtGui.QPushButton(u"Подробно")
        self.apex_button.resize(100,50)
        self.apex_button.hide()
        self.connect(self.apex_button, QtCore.SIGNAL('clicked()'), self.openApex)
        
        
        self.crm_button = QtGui.QPushButton(u"CRM")
        self.crm_button.resize(100,50)
        self.crm_button.hide()
        self.connect(self.crm_button, QtCore.SIGNAL('clicked()'), self.openCrm)
        
        
        grid = QtGui.QGridLayout(self)
        grid.addWidget(lastVisit_text,0,0)
        grid.addWidget(self.apex_button)
        grid.addWidget(self.crm_button)
        # grid.addStretch(1)
        
        
        personal_groupbox.setLayout(grid)
        
        
        
        address_layoutBox = QtGui.QGridLayout(self)
        address_layoutBox.setSpacing(10)
        address_layoutBox.setColumnMinimumWidth(0,0)
        address_layoutBox.addWidget(phone_label,0,0)
        address_layoutBox.addWidget(self.phone_text,0,1)
        address_layoutBox.addWidget(mobilePhone_label)
        address_layoutBox.addWidget(mobilePhone_text)
        address_layoutBox.addWidget(fax_label)
        address_layoutBox.addWidget(fax_text)
        address_layoutBox.addWidget(indexCity_label)
        address_layoutBox.addWidget(indexCity_text)
        address_layoutBox.addWidget(address_label)
        address_layoutBox.addWidget(address_text)
        
        
        
        
        
        
        address_groupbox = QtGui.QGroupBox(u"Адрес",self)
        address_groupbox.setLayout( address_layoutBox)
        address_groupbox.show()
        
        
        
        
        
        
        
        
        vertbox = QtGui.QGridLayout(self)
        vertbox.setColumnMinimumWidth(1,0)

        vertbox.addWidget(general_groupbox,0,0)
        vertbox.addWidget(personal_groupbox,0,1,1,50)
        vertbox.addWidget(address_groupbox,1,0,10,50)
        
        
        self.udpSocket = QtNetwork.QUdpSocket()
        self.udpSocket.bind(14541)
        self.udpSocket.readyRead.connect(self.recieveCall)
        
    def recieveCall(self):
        # self.title_text.setText(self.udpSocket.readDatagram())
         while self.udpSocket.hasPendingDatagrams():
            datagram, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
 
            try:
                datagram = str(datagram, encoding='ascii')
            except TypeError:
                pass
            
            data = datagram.split(',')
            phone = data[0]
            self.customer_id = data[1] 
            self.call_id = data[2]
            self.phone_text.setText(phone)
            self.apex_button.show()
            self.crm_button.show()
            self.title_text.setText(self.getCustomer(self.customer_id))
    
    def getCustomer(self,customer_id):
        db = MySQLdb.connect(host="10.36.100.245",user="root", passwd="tcaadmin36", db="sugarcrm")
        cursormsql = db.cursor()
        db.set_character_set('utf8')
        cursormsql.execute('SET NAMES utf8;')
        cursormsql.execute('SET CHARACTER SET utf8;')
        cursormsql.execute('SET character_set_connection=utf8;')

        cursormsql.execute("""SELECT name FROM accounts WHERE id = %s""" ,(customer_id,))
        results = cursormsql.fetchone()
        return unicode(results[0],"utf-8")
        
        

            # webbrowser.open("http://tca-db1.astrakhan.businesscar.ru:8080/apex/f?p=999:1:0::NO:1:P1_ID_CUSTOMER:"+self.customer_id)
             
    def closeEvent(self, event):
 
 
            reply = QtGui.QMessageBox.question(self, u'Сообщение',u"Вы действительно хотите выйти?", QtGui.QMessageBox.Yes |
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