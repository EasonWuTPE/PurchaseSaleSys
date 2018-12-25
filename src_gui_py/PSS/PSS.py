#!/usr/bin/python3.5 

# 1 

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QFormLayout, QVBoxLayout 
from PyQt5.QtCore import QCoreApplication  
from main import *  

class MainWindow(QWidget): 

	def __init__(self): 
		super(self.__class__, self).__init__()
		self.setupUi() 
		self.show() 

	def setupUi(self): 
		# Set Title 
		self.setWindowTitle("PurchaseSaleSys/login") 
		
		# Setting 
		self.label = QLabel() 
		self.label.setText("Welcome to PurchaseSaleSys!!\n \tPlease login your account.") 

		# Setting buttons and Text 
		self.line_User= QLineEdit() 
		self.line_Pass= QLineEdit() 
		self.label_User = QLabel("USER") 
		self.label_Pass = QLabel("Passwords") 

		self.button_Confirm = QPushButton("Comfirm")
		self.button_Confirm.clicked.connect(self.PSScall)
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


	def PSScall(self): 
		if self.line_User.text() == "ABC" and self.line_Pass.text() == "123":
			self.newWindow = PSSWindow() 
			self.newWindow.show()
		else:
			self.WarningWindow_ = WarningWindow()
			self.WarningWindow_.show() 
			
class WarningWindow(QWidget): 
	def __init__(self): 
		super(self.__class__, self).__init__()
		self.setupUI_AccountError()
		self.show()
	def setupUI_AccountError(self): 
		self.setWindowTitle("ERROR!!") 
		self.line_warning_text = QLineEdit("Warning! Account ERROR!! Retry!!") 


class PSSWindow(QWidget): 
	def __init__(self): 
		super(self.__class__, self).__init__()
		self.setupUi_PSS() 
		self.show()  
	
	def setupUi_PSS(self): 
		
		self.setWindowTitle("PurchaseSaleSys/ABC") 
		'''
		action = { 1: build_data,
				   2: sell_data, 
	 			   3: warning, 
				   4: insert_data, 
				   5: modified_data, 
				   6: export_data,
				   7: analysis_report, 
				   8: exit } 
		'''
		self.Label = QLabel( "\nInput your choice:\n  1 for adding record,\n  2 for updating the record,\n  3 for deleting record,\n  4 for insert record\n  5 for modify records.\n  6 for exporting records,\n  7 for analysis report\n  8 for end.\n >> " ) 
		self.line_choice = QLineEdit() 
		self.button_Cancel = QPushButton("Cancel") 
		self.button_Cancel.clicked.connect( QCoreApplication.instance().quit ) 
		
		# Setting the format of the UI. 
		form_layout = QFormLayout() 
		form_layout.addRow( self.Label, self.line_choice)
		form_layout.addRow( self.button_Cancel)
		h_layout = QVBoxLayout() 
		h_layout.addWidget(self.Label) 
		h_layout.addLayout(form_layout) 
		self.setLayout(h_layout) 

if __name__ == "__main__": 
	app = QApplication( sys.argv ) 
	MainWindow = MainWindow() 
	sys.exit(app.exec_()) 

