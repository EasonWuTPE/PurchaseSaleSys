#!/usr/bin/python3.5 

# 1 

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QFormLayout, QVBoxLayout 
from PyQt5.QtCore import QCoreApplication  


class MainWindow(QWidget): 

	def __init__(self): 
		super(self.__class__, self).__init__()
		self.setupUi() 
		self.show() 

	def setupUi(self): 
		# Set Title 
		self.setWindowTitle("PurchaseSaleSys") 
		
		# Setting 
		self.label = QLabel() 
		self.label.setText("Welcome to PurchaseSaleSys!!\n \tPlease login your account.") 

		# Setting buttons and Text 
		self.line_User= QLineEdit() 
		self.line_Pass= QLineEdit() 
		self.label_User = QLabel("USER") 
		self.label_Pass = QLabel("Passwords") 

		self.button_Confirm = QPushButton("Comfirm")
		self.button_Confirm.clicked.connect(self.PSSsetupUi)
		self.button_Cancel = QPushButton("Cancel") 
		self.button_Cancel.clicked.connect( QCoreApplication.instance().quit ) 

		# Setting the format of the UI. 
		form_layout = QFormLayout() 
		form_layout.addRow( self.label_User, self.line_User)
		form_layout.addRow( self.label_Pass, self.line_Pass)
		form_layout.addRow(self.button_Confirm, self.button_Cancel)
		h_layout = QVBoxLayout() 
		h_layout.addWidget(self.label) 
		h_layout.addLayout(form_layout) 
		self.setLayout(h_layout) 


	def PSSsetupUi(self): 
		if self.line_User.text() == "ABC" and self.line_Pass.text() == "123":
			newWindow = PSSWindow() 
			newWindow.show()
			newWindow.exec_()


class PSSWindow(QWidget): 
	def __init__(self): 
		super(self.__class__, self).__init__()
		self.setupUi_PSS() 
		self.show()  
	
	def setupUi_PSS(self): 
		self.setWindowTitle("Success!!") 


if __name__ == "__main__": 
	app = QApplication( sys.argv ) 
	MainWindow = MainWindow() 
	sys.exit(app.exec_()) 


