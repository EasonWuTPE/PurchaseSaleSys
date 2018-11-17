# Use gcc to compile this source files.
CC = gcc
# Complier flag.
FLAG = -Wall -pedantic 
# Delete object files.
RM = rm

# Combine object files to form a binary execuatable file as Retail
Retail: Retail.o IN.o OUT.o
	$(CC) -o Retail $(FLAG) Retail.o IN.o OUT.o 

Retail.o: Retail.c IN.h OUT.h
	$(CC) $(FLAG)-c Retail.c 

IN.o: IN.h IN.c
	$(CC) $(FLAG) -c IN.c 

OUT.o: OUT.h OUT.c
	$(CC) $(FLAG) -c OUT.c

clean:
	$(RM) -rf *.o
