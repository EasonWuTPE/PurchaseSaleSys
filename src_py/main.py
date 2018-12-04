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
							   weight_kg = { "Weight(KG)":weight_kg, "Total_Weight_Price_(TWD)":total_weight_TWD },
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
	pass

''' --------------------------- Definition End ------------------------------------- ''' 



''' --------------------------------- Main ----------------------------------------- ''' 
# Main Program 
while True:
	try:
		print( "Input your choice: " ) 
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


