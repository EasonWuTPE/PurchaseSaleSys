#include <stdio.h>
#include "lib/util.h" 

int main( void ) {
    FILE *cfPtr; /* DataBase.dat file pointer */
    int choice; /* user's choice */
    char newdata_or_not; 
    char account_name[500]; 
    char path[1000]; 

    printf( "\n\nWelcome to PurchaseSaleSys...\n" ); 
    printf( "Do you want to creat a new account? Y/N >> " ); 
    scanf( "%c", &newdata_or_not ); 
    if( newdata_or_not == 'Y' || newdata_or_not == 'y' ){ 
        cfPtr = RECREATE(); 
    }else{ 
        printf( "Input your account name >> " ); 
        scanf( "%s", account_name ); 
        strcpy( path, "./database/" ); 
        strcat( path, account_name ); 
        strcat( path, ".dat" ); 
        cfPtr = fopen( path, "rb+" ); 
    } 

    /* fopen opens the file; RECREATE if file cannot be opened */
    if ( cfPtr == NULL ) {
        printf( "Faile to open or create new files..." ); 
    } else {
        /* enable user to specify action */
        while ( ( choice = enterChoice() ) != 5 ) { 
            switch ( choice ) { 
                /* create text file from record file */
                case 1:
                    textFile( cfPtr, account_name );
                    break;
                    /* update record */
                case 2:
                    updateRecord( cfPtr );
                    break;
                    /* create record */
                case 3:
                    newRecord( cfPtr );
                    break;
                    /* delete existing record */
                case 4:
                    deleteRecord( cfPtr );
                    break;
                    /* display message if user does not select valid choice */
                default:
                    printf( "Incorrect choice\n" );
                    break;
            } /* end switch */
        } /* end while */

        fclose( cfPtr ); /* fclose closes the file */
    } /* end else */

    return 0; /* indicates successful termination */
} /* end main */

/* enable user to input menu choice */
int enterChoice( void ) {
    int menuChoice; /* variable to store user's choice */

    /* display available options */
    printf( "\nEnter your choice\n"
            "1 - store a formatted text file of records called\n"
            "    \"DataBase.dat\" for printing\n"
            "2 - update an record\n"
            "3 - add a new record\n"
            "4 - delete an record\n"
            "5 - end program\n "
			"p.s. Account # - 1  = ItemNo \n? " );


    scanf( "%d", &menuChoice ); /* receive choice from user */
    return menuChoice;
} /* end function enterChoice */



