#!/usr/bin/python3.5 

# Purchase Sales System for Python Version 

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
import copy 


'''

 Keys Reference: 
 	

'''


''' --------------------------- Function Definition --------------------------------- ''' 
# Build_data function 
def build_data( ):
	# Input the data.
	Data = [] 

	while True:
		record_ = input( "Input the data: \nItemNo, Purchase Date, item_class, color, Forex, exchange_rate, weight(kg), weight cost(TWD), Purchase cost (Forex) >>\n" )  
		if record_:
			# build a dict
			record_ = record_.split(' ') 
			#print( "type: " ,type( record_ ) )
			try: 
				ItemNo = int(record_[0]); Purchase_Date = record_[1]; item_class = record_[2]; color = record_[3]; Forex = record_[4]; 
				exchange_rate = float(record_[5]) if record_[4] != '.' else 1.0; 
				weight_kg = float(record_[6]); total_weight_TWD = float(record_[7]); purchase_cost_Forex = float(record_[8]);
		
				Record = dict( ItemNo =  ItemNo, 
							   Purchase_Date = Purchase_Date,
							   Spec = { "Class_Item":item_class, "Color":color },
							   Forex = { "Forex":Forex, "ExchangeRate":exchange_rate },
							   Weight_kg = { "Weight(KG)":weight_kg, "Weight_Price(TWD)":total_weight_TWD },
							   Cost = {  "Purchase_Cost_Forex":purchase_cost_Forex, 
							   			 "Purchase_Cost(TWD)":purchase_cost_Forex*exchange_rate, 
										 "Total_Purchase_Cost(TWD)":purchase_cost_Forex*exchange_rate + total_weight_TWD }, 
							   Sold_Date = ".",
							   Revenue = 0,
							   Profit = 0, 
							   Profit_Margin = 0.0 ) 
				Data.append( Record ) 
			except:
				print( "\nUnexpected input data type or format! Re-input again. Thanks!" ) 

		else:
			break;
	
	# Create a file to save data. 
	fwrite = open( r"./Files/records.dat", "a+" ) 
	#print( len( Data ) ) 
	for line in Data: 
		print( line, file = fwrite ) 
	fwrite.close() 

# update_sell function 
def sell_data():
	try:
		choice = int( input( "Enter the No. to record the sold. >> " ) ) 
		lines_ = [ line.rstrip() for line in open( r"./Files/records.dat" ) ] 
		open( r"./Files/records.dat" ).close() 
		print( lines_ ) 
		if choice > len(lines_): 
			print( "The No. input is out of range." ) 
		else:
			sell_update = eval(lines_[ choice-1 ]) # dict  
			update = input( "Input your sold date and revenue>> " ).rstrip().split(' ') 
			sell_update["Sold_Date"] = update[0] 
			sell_update["Revenue"] = float(update[1])  
			sell_update["Profit"] = float(sell_update["Revenue"]) - sell_update["Cost"]["Total_Purchase_Cost(TWD)"] 
			sell_update["Profit_Margin"] = sell_update["Profit"] / sell_update["Cost"]["Total_Purchase_Cost(TWD)"] 
			#print( sell_update ) 
			lines_[choice-1] = str( sell_update )
			#print( lines_ ) 

			# Create a file to save data. 
			fwrite = open( r"./Files/records.dat", "w" ) 
			for line in lines_: 
				print( line, file = fwrite ) 
			fwrite.close() 
			
	except ValueError: 
		print( "Unexcepted input type!! Try again!! " ) 


# delete_data function 
def delete_data():
	AccNum = int( input( "\n Choose the No. that you wnat to delete>> " ) ) 
	while AccNum-1 >= len( LINE_FREAD ): 
		print( "The No. inputed dosen't exist. Try again!!" ) 
		AccNum = int( input( "Choose the No. that you wnat to delete or 'E' to return >> " ) ) 
		if AccNum == 'E': 
			break 
	LINE_FREAD.pop( AccNum-1 )
	for i in LINE_FREAD[AccNum-1:]:   
		change_No = eval( i ) 
		change_No["ItemNo"] -= 1 
		LINE_FREAD.insert( change_No["ItemNo"] - 1, change_No ) 
		LINE_FREAD.pop( change_No["ItemNo"] ) 
		#print( LINE_FREAD ) 
			

	# Create a file to save data. 
	fwrite = open( r"./Files/records.dat", "w" ) 
	#print( len( Data ) ) 
	for line in LINE_FREAD: 
		print( line, file = fwrite ) 
	fwrite.close() 


# insert_data function 
def insert_data():
	#pass
	AccNum = int( input( "\n Choose the No. that you wnat to insert> " ) ) 
	while AccNum-1 >= len( LINE_FREAD): 
		print( "The No. inputed dosen't exist. Try again!!" ) 
		AccNum = int( input( "Choose the No. that you wnat to delete or 'E' to return >> " ) ) 
		if AccNum == 'E': 
			break 
	record_ = input( "Input the data: \nItemNo, Purchase Date, item_class, color, Forex, exchange_rate, weight(kg), weight cost(TWD), Purchase cost (Forex) >>\n" ).split(' ')  
	# build a dict
	try: 
		ItemNo = int(record_[0]); Purchase_Date = record_[1]; item_class = record_[2]; color = record_[3]; Forex = record_[4]; 
		exchange_rate = float(record_[5]) if record_[4] != '.' else 1.0; 
		weight_kg = float(record_[6]); total_weight_TWD = float(record_[7]); purchase_cost_Forex = float(record_[8]);

		Record = dict( ItemNo =  ItemNo, 
					   Purchase_Date = Purchase_Date,
					   Spec = { "Class_Item":item_class, "Color":color },
					   Forex = { "Forex":Forex, "ExchangeRate":exchange_rate },
					   Weight_kg = { "Weight(KG)":weight_kg, "Weight_Price(TWD)":total_weight_TWD },
					   Cost = {  "Purchase_Cost_Forex":purchase_cost_Forex, 
					   			 "Purchase_Cost(TWD)":purchase_cost_Forex*exchange_rate, 
								 "Total_Purchase_Cost(TWD)":purchase_cost_Forex*exchange_rate + total_weight_TWD }, 
					   Sold_Date = ".",
					   Revenue = 0,
					   Profit = 0, 
					   Profit_Margin = 0.0 ) 
	except:
		print( "\nUnexpected input data type or format! Re-input again. Thanks!" ) 


	LINE_FREAD.insert( AccNum-1, Record )

	for i in LINE_FREAD[AccNum:]:   
		change_No = eval( i ) 
		change_No["ItemNo"] += 1 
		LINE_FREAD.insert( change_No["ItemNo"]-1, change_No ) 
		LINE_FREAD.pop( change_No["ItemNo"] ) 
		#print( LINE_FREAD ) 

	# Create a file to save data. 
	fwrite = open( r"./Files/records.dat", "w" ) 
	#print( len( Data ) ) 
	for line in LINE_FREAD: 
		print( line, file = fwrite ) 
	fwrite.close() 


# modify your record 
def modified_data(): 
	modify_ = input( "Input the the No., column name and value that you want to modify. >> " ).split(' ') 
	modify_reocrds = eval( LINE_FREAD[modify_[0]-1] ) 
	print( modify_reocrds ) 
		


# export_data function 
def export_data():
	fread = open( r"./Files/records.dat" ) 
	fstdout = open( r"./Files/PurchaseSaleReocrds.txt", "w+" ) 
	fstdout.write( "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n"%( "No.", "Purchase_Date", "Class_Item", "Color", "Forex", "ExchangeRate", "Weight(KG)",
																	  "Weight_Price(TWD)", "Purchase_Cost_Forex", "Purchase_Cost(TWD)", "Total_Purchase_Cost(TWD)",
																	  "Sold_Date", "Revenue", "Profit", "Profit_Margin" ) ) 
	
	stdout_lines = [ lines for lines in fread ] 
	
	for line_ in stdout_lines:
		lines = eval( line_ )
		#print( type(lines ) ) 
		try:
			print( "%3s%14s%11s%6s%6s%13.2f%10.2f%18.2f%21.2f%18.2f%25.2f%11s%8.2f%7.2f%13.2f" %( lines["ItemNo"], lines["Purchase_Date"], lines["Spec"]["Class_Item"],
																    						  lines["Spec"]["Color"], lines["Forex"]["Forex"], lines["Forex"]["ExchangeRate"],
																							  lines["Weight_kg"]["Weight(KG)"], lines["Weight_kg"]["Weight_Price(TWD)"],
																							  lines["Cost"]["Purchase_Cost_Forex"], lines["Cost"]["Purchase_Cost(TWD)"],
																  				 			  lines["Cost"]["Total_Purchase_Cost(TWD)"], 
																							  lines["Sold_Date"], lines["Revenue"], lines["Profit"], lines["Profit_Margin"] ), 
																							  file = fstdout )
		except EOFError: 
			pass 
	fread.close() 
	fstdout.close() 


# analysis_report function 
def analysis_report(): 
	pass



''' --------------------------- Definition End ------------------------------------- ''' 



''' --------------------------------- Main ----------------------------------------- ''' 
# Main Program 
try:
	FREAD = open( r"./Files/records.dat" )  
	LINE_FREAD = [ LINES.rstrip() for LINES in FREAD ] 
except IOError:
	pass 


while True:
	try:
		print( "\nInput your choice: " ) 
		choice = int(input( "  1 for adding record,\n  2 for updating the record,\n  3 for deleting record,\n  4 for insert record\n  5 for modify records.\n  6 for exporting records,\n  7 for analysis report\n  8 for end.\n >> " )) 
		if choice == 1:
			build_data()
		elif choice == 2: 
			sell_data() 
		elif choice == 3: 
			print( "\nAre you sure to delete specific record? <Y/n> " ) 
			delete_or_not = input( ) 
			if delete_or_not == 'Y' or delete_or_not == 'y':
				delete_data()
			else:
				continue
		elif choice == 4: 
			insert_data() 
		elif choice == 5: 
			modified_data() 
		elif choice == 6: 
			export_data()
		elif choice == 7: 
			analysis_report() 
		elif choice == 8:
			#FREAD.close() 	
			break
		else:
			print( "\nUnexpected choice!!!! Try again!" ) 

	except ValueError:
		print( "\nUnexpected type of choice!!!! Try again! " );


