#!/usr/bin/python3.5 

# Purchase Sales System for Python Version 
'''
 ItemNo
 Purchase_Date
 Spec: Describe the merchandises
 weight
 Cost
 Sold Date
 Revenue
 Profit 
 Profit Margin
'''


''' --------------------------- Function Definition --------------------------------- ''' 
# Build_data function 
def build_data( ):
	# Input the data.
	Data = [] 

	while True:
		record_ = input( " Tnput the data: \n ItemNo, Purchase Date, item_class, color, Forex, exchange_rate, weight(kg), weight cost(TWD), Purchase cost (Forex) >>\n" )  
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
							   Spec = [ item_class, color ],
							   Forex = [ Forex, exchange_rate ],
							   weight_kg = [ weight_kg, total_weight_TWD ],
							   Cost = [  purchase_cost_Forex, purchase_cost_Forex*exchange_rate, purchase_cost_Forex*exchange_rate + total_weight_TWD ], 
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

# update_data function 
def update_data():
	pass

# delete_data function 
def delete_data():
	pass

# export_data function 
def export_data():
	pass

''' --------------------------- Definition End ------------------------------------- ''' 



''' --------------------------------- Main ----------------------------------------- ''' 
# Main Program 
while True:
	try:
		choice = int( input( "  1 for adding record,\n  2 for updating the record,\n  3 for deleting record,\n  4 for exporting records,\n  5 for end. >> \n " ) ) 
		if choice == 1:
			build_data()
		elif choice == 2: 
			update_data() 
		elif choice == 3: 
			delete_data()
		elif choice == 4: 
			export_data() 
		elif choice == 5:
			break
		else:
			print( "\nUnexpected choice!!!! Try again!" ) 

	except ValueError:
		print( "\nUnexpected type of choice!!!! Try again! " );


