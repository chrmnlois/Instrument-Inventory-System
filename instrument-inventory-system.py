# San Antonio, Charmaine Lois A. (BSIT 2-5)
# Activity 1 for 2nd Half

import csv

# == FUNCTIONS ==
def mainMenu(): #function for main menu
    print("\n        M  A  I  N     M  E  N  U     \n-------------------------------------------\nSWITCH Music\n")
    print("Welcome to the Instrument Inventory System!\n")
    print("PRODUCTS AVAILABLE:\n- Acoustic Guitar     - Drum Set\n- Electric Guitar     - Piano\n- Bass Guitar")
    print("\nMAIN MENU:\n(A) Write Products To A File\n(B) Read Products To A File\n(C) Exit")
    print("-------------------------------------------")

def writeProduct(): #function for write product
    try:
        fp = open('SWITCH_Inventory_System.csv','w',newline='') #open csv file with write function
        fprint = csv.writer(fp) #display purposes in csv file
        fprint.writerow(['PRODUCT CODE','BRAND','DESCRIPTION','COLOR','UNIT PRICE','STOCK']) #print headers in csv file
        records=[] #empty records list

        choiceWrite = '' #declare choiceWrite variable
        while True: #main while loop for writeProduct function
            print("\n\n               W  R  I  T  E\n===========================================\nSWITCH Music Instrument Inventory System\nWrite Products To A File")

            while True: #while loop for product code
                print("\n(1) PRODUCT CODE (Ex: AG01)\n\tPlease input\n\t'AG' for Acoustic Guitar\n\t'EG' for Electric Guitar""\n\t'BG' for Bass Guitar\n\t'DS' for Drum Set\n\t'PI' for Piano")
                try: #exception handling for product code
                    productCode = input("\n\tEnter product code here : ")
                    if productCode.isdigit():
                        raise ValueError
                    elif productCode.isalnum():
                        break #if input is correct, this loop will break
                except ValueError as e:
                    print("\n\tProduct Code: ERROR FOUND! Please enter the specific input.", type(e))
                except Exception as e:
                    print("\n\tProduct Code: ERROR FOUND! Please enter the specific input.", type(e))

            while True: #while loop for product brand
                print("\n(2) BRAND\n\t- Gibson\n\t- Harman\n\t- Roland\n\t- Yamaha\n\t- Zildjian")
                try: #exception handling for brand
                    productBrand = input("\n\tEnter product brand here : ")
                    if productBrand.isdigit():
                        raise ValueError
                    elif productBrand.isalpha():
                        break #if input is correct, this loop will break
                except ValueError as e:
                    print("\n\tBrand: ERROR FOUND! Please enter the specific input.", type(e))
                except Exception as e:
                    print("\n\tBrand: ERROR FOUND! Please enter the specific input.", type(e))

            while True: #while loop for product description
                print("\n(3) DESCRIPTION\n\t- Acoustic Guitar\n\t- Electric Guitar\n\t- Bass Guitar\n\t- Drum Set""\n\t- Piano")
                try: #exception handling for product description
                    productDesc = input("\n\tEnter product description here : ")
                    if productDesc.isdigit():
                        raise ValueError
                    if productDesc.isprintable():
                        break #if input is correct, this loop will break
                except ValueError as e:
                    print("\n\tDescription: ERROR FOUND! Please enter the specific input.", type(e))
                except Exception as e:
                    print("\n\tDescription: ERROR FOUND! Please enter the specific input.", type(e))

            while True: #while loop for product color
                print("\n(4) COLOR\n\t- Matte Black\n\t- Oak White\n\t- Pecan Brown\n\t- Midnight Blue\n\t- Ruby Red")
                try: #exception handling for product color
                    productColor = input("\n\tEnter product color here : ")
                    if productColor.isdigit():
                        raise ValueError
                    elif productColor.isprintable():
                        break #if input is correct, this loop will break
                except ValueError as e:
                    print("\n\tColor: ERROR FOUND! Please enter the specific input.", type(e))
                except Exception as e:
                    print("\n\tColor: ERROR FOUND! Please enter the specific input.", type(e))

            while True: #while loop for product price
                print("\n(5) PRICE")
                try: #exception handling for product price
                    productUPrice = (input("\tEnter unit price here : Php "))
                    if productUPrice.isalpha():
                        raise ValueError
                    elif productUPrice.isdigit():
                        break #if input is correct, this loop will break
                except ValueError as e:
                    print("\n\tPrice: ERROR FOUND! Please enter the specific input.", type(e))
                except Exception as e:
                    print("\n\tPrice: ERROR FOUND! Please enter the specific input.", type(e))

            while True: #while loop for product stock
                print("\n(6) STOCK AVAILABLE")
                try: #while loop for product stock
                    productStock = (input("\tEnter stock here : "))
                    if productStock.isalpha():
                        raise ValueError
                    elif productStock.isdigit():
                        break #if input is correct, this loop will break
                except ValueError as e:
                    print("\n\tStock: ERROR FOUND! Please enter the specific input.", type(e))
                except Exception as e:
                    print("\n\tStock: ERROR FOUND!\nPlease enter the specific input.", type(e))

            dummyRecord = [productCode, productBrand, productDesc, productColor, productUPrice, productStock] #temporary storage for all input attributes
            records.append(dummyRecord) #from dummy list, all input attributes will append to the main list

            ans = '' #declare ans variable
            while ans != 'n': #while loop for continue question
                try: #exception handling for continue question
                    choiceWrite = input("\nContinue Writing To File? : ")[0]
                    if choiceWrite.isdigit():
                        raise ValueError
                except ValueError as e:
                    print("\nERROR FOUND!\nPlease enter 'Yes' or 'No'.", type(e))
                    ans = 'y'

                if choiceWrite.isalpha(): #if input is yes or no, this loop will break. otherwise, continue
                    if choiceWrite == 'n' or choiceWrite == 'N':
                        ans = 'n' #loop breaker, continue to next statement outside of this loop
                    elif choiceWrite == 'y' or choiceWrite == 'Y':
                        ans = 'n' #loop breaker, continue to next statement outiside of this loop
                    else:
                        print("INVALID INPUT! Please enter 'Yes' or 'No'")

            # if choiceWrite == 'N' from the above statement, the if statement below will be processed then exit the main while loop.
            # else, if choiceWrite == 'Y', the main while loop will start again.
            if choiceWrite.upper() == 'N':
                for i in records:
                    fprint.writerow(i)
                print("\n                  ********** End Of Writing File **********                         ")
                print("\n")
                break
    except Exception as e:
        print("\nERROR FOUND! Please enter the specific input.", type(e))
    finally:
        fp.close() #close file

def readProduct(): #function for read product
    try:
        fp = open('SWITCH_Inventory_System.csv','r') #open csv file with read function
        fscan = csv.reader(fp) #scan purposes in csv file
        next(fscan) #scan the next record so the headers from the csv file will not be read again
        print("\n\n                R  E  A  D\n===========================================\nSWITCH Music Instrument Inventory System\nRead Products To A File\n")
        print("_____________________________________________________________________________________________________________________________")
        print("   PRODUCT CODE   |      BRAND      |       DESCRIPTION       |      COLOR      | UNIT PRICE | STOCK | TOTAL PRICE PER STOCK ")
        print("-----------------------------------------------------------------------------------------------------------------------------")

        for i in fscan: #for loop for scanning the contents of the csv file
            tpStock = (float(i[4]) * float(i[5])) #formula for total price per stock feature
            print("",i[0]," "*(15-len(i[0])),"|",i[1]," "*(14-len(i[1])),"|",i[2]," "*(22-len(i[2])),"|",i[3]," "*(14-len(i[3])),"|",i[4]," "*(9-len(i[4])),"|",i[5]," "*(4-len(i[5])),"|",thousand_separator(tpStock))
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("\n                                       ********** End Of Reading File **********                           ")
        print("\n")
    except Exception as e:
        print("\nERROR FOUND! Please enter the specific input.", type(e))
    finally:
        fp.close() #close file

def thousand_separator(num): #function to display comma separators in tpStock
	return ("{:,}".format(num))

# == MAIN PROGRAM ==
mainMenu() #call main menu function
try: #exception handling for main menu
    choiceMenu = input("Enter your choice here : ")[0]
    if choiceMenu.isdigit():
        raise ValueError
except ValueError as e:
    print("\nMain Menu: ERROR FOUND! Please enter the specific input.", type(e))
    print("\n\n")
except Exception as e:
    print("\nMain Menu: ERROR FOUND! Please enter the specific input.", type(e))
    print("\n\n")

while choiceMenu.upper() != 'C': #if statements to call certain functions in main menu
        if choiceMenu.isalpha():
            if choiceMenu == 'A' or choiceMenu== 'a':
                writeProduct()
            elif choiceMenu== 'B' or choiceMenu== 'b':
                readProduct()
            else:
                print("\nINVALID INPUT! Please enter from the choices only.")
                print("\n\n")

        mainMenu()
        choiceMenu = input("Enter your choice here : ")[0]

print("\nThank you for using our inventory!\n==  E N D   O F   P R O G R A M  ==")