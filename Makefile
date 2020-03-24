# Use gcc to compile this source files.
CC = gcc
# Complier flag.
FLAG = -Wall -pedantic 
# Delete object files.
RM = rm 
#code path 
MAIN=./PurchaseSaleSys/src/
LIBS=./PurchaseSaleSys/src/lib/

# Combine object files to form a binary execuatable file as PurchaseSaleSys

exec: clean build 
	@echo ' '
	@echo ' '
	@echo 'Starting system...' 
	@./PurchaseSaleSystem 

build: compile 
	@echo 'Building system...' 

compile: PurchaseSaleSystem clean
	@echo 'Complete compilation'

PurchaseSaleSystem: PurchaseSaleSys.o util.o
	@echo ' '
	@echo ' '
	@echo 'Compiling...'
	$(CC) -o PurchaseSaleSystem $(FLAG) $(MAIN)PurchaseSaleSys.c util.o

PurchaseSaleSys.o: $(MAIN)PurchaseSaleSys.c $(LIBS)util.h 
	$(CC) $(FLAG) -c $(MAIN)PurchaseSaleSys.c 

util.o: $(LIBS)util.c $(LIBS)util.h $(LIBS)data.h
	$(CC) $(FLAG) -c $(LIBS)util.c 

clean:
	@echo 'Cleaning...' 
	$(RM) -rf *.o
