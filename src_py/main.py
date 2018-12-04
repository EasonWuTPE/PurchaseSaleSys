#!/usr/bin/python3.5 

# Purchase Sales System for Python Version 
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
			try:
				record_ = record_.split(' ') 
				#print( "type: " ,type( record_ ) )
				ItemNo = record_[0]; Purchase_Date = record_[1]; item_class = record_[2]; color = record_[3]; Forex = record_[4]; 
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

			except ValueError: 
				print( "Unexpected input data type or format! Re-input again. Thanks!" ) 
		else:
			break;
	
	# Create a file to save data. 
	fwrite = open( r"./Files/records.dat", "a+" ) 
	#print( len( Data ) ) 
	for line in Data: 
		print( line, file = fwrite ) 
	fwrite.close() 

# update_data function 
def update_data():
	pass

# delete_data function 
def delete_data():
	pass
	AccNum = int( intput( "\n Choose the No. that you wnat to delete>> " ) ) 
	#if dataAccNum-1

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
		print( "%3s%14s%11s%6s%6s%13.2f%10.2f%18.2f%21.2f%18.2f%25.2f%11s%8.2f%7.2f%13.2f" %( lines["ItemNo"], lines["Purchase_Date"], lines["Spec"]["Class_Item"],
																    							  lines["Spec"]["Color"], lines["Forex"]["Forex"], lines["Forex"]["ExchangeRate"],
																								  lines["Weight_kg"]["Weight(KG)"], lines["Weight_kg"]["Weight_Price(TWD)"],
																								  lines["Cost"]["Purchase_Cost_Forex"], lines["Cost"]["Purchase_Cost(TWD)"],
																  				 				  lines["Cost"]["Total_Purchase_Cost(TWD)"], 
																								  lines["Sold_Date"], lines["Revenue"], lines["Profit"], lines["Profit_Margin"] ), 
																								  file = fstdout ) 
	


''' --------------------------- Definition End ------------------------------------- ''' 



''' --------------------------------- Main ----------------------------------------- ''' 
# Main Program 
while True:
	try:
		print( "\nInput your choice: " ) 
		choice = int( input( "  1 for adding record,\n  2 for updating the record,\n  3 for deleting record,\n  4 for exporting records,\n  5 for end.\n >> " ) ) 
		if choice == 1:
			build_data()
		elif choice == 2: 
			update_data() 
		elif choice == 3: 
			print( "\nAre you sure to delete specific record? <Y/n> " ) 
			delete_or_not = input( ) 
			if delete_or_not == 'Y' or delete_or_not == 'y':
				delete_data()
			else:
				continue
		elif choice == 4: 
			export_data() 
		elif choice == 5:
			break
		else:
			print( "\nUnexpected choice!!!! Try again!" ) 

	except ValueError:
		print( "\nUnexpected type of choice!!!! Try again! " );


