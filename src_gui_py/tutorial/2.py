#!/usr/bin/python3.5 

# Toturiol for PyQt5 

from PyQt5.QtWidgets import * 
import sys 

class Window(QWidget): 
	
	def __init__(self): 
		
		QWidget.__init__(self) # Let it define the setting of Window directly in this class. 
		self.setWindowTitle("Test1") 
		label = QLabel("Hellow, this is John.") 

		layout = QGridLayout() # Qt can only display one object at a time. Use the QGridLayout() to display multiple item.  
		self.setLayout(layout) 

		layout.addWidget( label, 0, 0 ) 

app = QApplication(sys.argv) 
screen = Window() 
screen.show() 

sys.exit(app.exec_()) 
		

