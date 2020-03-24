#ifndef DATA_H_ 
#define DATA_H_ 

/* define a struct */
struct item{
	size_t ItemNo_Internal_USE; /* Use it to locate the position of the record. */
	size_t Purchase_Date; /* The merchandise purchase date */
	char ItemNo[8]; /* The item number of merchandise defined by user */
	char Brand[20]; /* The detail of merchandise */
	char Scale[6]; 
	char Manufacture[20];
	char Detail_[20];
	char Color[9];
	size_t Cost; /* The purchase cost */
    size_t Sold_Date; /* The date of merchandise sold */
	size_t Revenue; /* The sold price of merchandise */
	size_t Profit; /* The profits */
	double ProfitMargin; 
};

#endif 
