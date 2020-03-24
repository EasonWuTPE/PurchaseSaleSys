#ifndef UTIL_H_ 
#define UTIL_H_ 


/* Function prototypes */
FILE *RECREATE( void );
void textFile( FILE *readPtr, const char *account_name );
void updateRecord( FILE *fPtr );
void newRecord( FILE *fPtr );
void deleteRecord( FILE *fPtr );

#endif 
