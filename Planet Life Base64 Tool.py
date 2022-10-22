import base64
import os
from time import sleep
from datetime import date

today = date.today()
textfile_exist = os.path.exists('Input_Base64.txt')
data = "Q3JlYXRlZCBCeTogQ3JhY2tvMjk4"
dat_check = "VGhlIFNjcmlwdCBXYXMgVGFtcGVyZWQgV2l0aC4gUGxlYXNlIEdldCBUaGUgT3JpZ2luYWwgU2NyaXB0IGF0ICdodHRwczovL2dpdGh1Yi5jb20vQ3JhY2tvMjk4L1BsYW5ldC1MaWZlLUNoZWF0Jy4="
data0 = base64.b64decode(data)
dat_check_success = base64.b64decode(dat_check)
num0 = 2 ; num1 = -1 ; num2 = dat_check

def Start():
    if dat_check != "VGhlIFNjcmlwdCBXYXMgVGFtcGVyZWQgV2l0aC4gUGxlYXNlIEdldCBUaGUgT3JpZ2luYWwgU2NyaXB0IGF0ICdodHRwczovL2dpdGh1Yi5jb20vQ3JhY2tvMjk4L1BsYW5ldC1MaWZlLUNoZWF0Jy4=":
        os.system('clear')
        print(dat_check_success)
        print(" ")
        input("Press The 'Enter' Key To Exit.")
        exit()
    os.system('clear')
    print(" ")
    print(data0)
    print(" ")
    print("0 = Convert 'Base64' String To '.planet' File.")
    print("1 = Convert '.planet' File To 'Base64 String.")
    print(" ")

    choice = int(input("Type 0/1 For Your Choice: "))

    if choice == 0: 
        os.system('clear')
        print(" ")
        create = "Q3JlYXRlZCBCeTogQ3JhY2tvMjk4"
        with open('Input_Base64.txt', 'rb') as fileX:
            base64toStr1 = fileX.read()
            
            with open('Save-'+str(today)+'.planet', 'wb') as file1:
                base64toStr2 = base64.b64decode(base64toStr1)
                file1.write(base64toStr2)
                file1.close()
        if create != data:
            if data != "Q3JlYXRlZCBCeTogQ3JhY2tvMjk4":
                print(dat_check_success)
                print(" ")
                input("Press The 'Enter' Key To Exit.")
                exit()
        sleep(1)
        os.system('clear')
        print(" ")
        print("The Script Was Successful At Decrypting The Base64 Key.")
        print(" ")
        input("Press the 'Enter' To Continue To The Menu.")
        Start()

    if choice == 1:
        os.system('clear')
        print(" ")
        user_input = input("What Is The '.planet' File's Name (Do NOT Include The Extension): ")
        with open(user_input +'.planet', 'rb') as fileA:
            StrToBase64_1 = fileA.read()

            with open('BASE64 - '+ str(today)+'.txt', 'wb') as fileB:
                StrToBase64_2 = base64.b64encode(StrToBase64_1)
                fileB.write(StrToBase64_2)
                fileB.close()
                sleep(1)
                os.system('clear')
                print(" ")
                print("The Script Was Successful At Decrypting The Base64 Key.")
                print(" ")
                input("Press the 'Enter' To Continue To The Menu.")
                Start()

    if choice >= num0:
        os.system('clear')
        print(" ")
        print("The Script Didn't Seem To Understand Your Input of " + str(choice))
        sleep(2.5)
        Start()

def check():
    if num2 != "VGhlIFNjcmlwdCBXYXMgVGFtcGVyZWQgV2l0aC4gUGxlYXNlIEdldCBUaGUgT3JpZ2luYWwgU2NyaXB0IGF0ICdodHRwczovL2dpdGh1Yi5jb20vQ3JhY2tvMjk4L1BsYW5ldC1MaWZlLUNoZWF0Jy4=":
        os.system('clear')
        print(dat_check_success)
        print(" ")
        input("Press The 'Enter' Key To Exit.")
        exit()

    bytes_of_text = [48,48,48,48]
    bytes_of_text1 = b'\x30\x30\x30\x30'
    with open('Input_Base64.txt', 'rb') as text_file:
        byte_chosen1 = text_file.read(4)
        byte_chosen = list(text_file.read(4))
    if bytes_of_text <= byte_chosen:
        Start()
    else:
        print(" ")
        print("An Error Has Occurred. Whoops! Here's Some Information...")
        print(" ")
        print("Required Base64 Data Was 'NOT' Found.")
        print(" ")
        print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        print(" ")

        print("Data Below Is The Bare Minimium (Not Actual Base64 Code)")
        print(" ")
        print("Decimals Codes Needed:                                                 " + str(bytes_of_text))
        print("Hexadecimal Codes Needed:                                              " + str(bytes_of_text1))
        print(" ")
        print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        print(" ")
        print("Data Given To Script Is Listed Below.")
        print(" ")

        print("Decimals Codes Found:                                                  " + str(byte_chosen))
        print("Hexadecimal Codes Found:                                               " + str(byte_chosen1))
        print(" ")
        print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        print(" ")
        input("Press The 'Enter' Key To Exit.")
        exit()

def if_text():
    if textfile_exist == True:
        check()
    else:
        file10 = open('Input_Base64.txt', 'w')
        file10.close
        os.system('clear')
        print(" ")
        print("The Script Has Created A New File. Please Paste Your 'Base64' String Into It. (And Yes, You Have Save It)")
        print(" ")
        input("Press The 'Enter' Key To Exit.")
        exit()

if data != "Q3JlYXRlZCBCeTogQ3JhY2tvMjk4":
    print("The Application Encountered An Error While Starting...")
    sleep(5)
    exit()

if_text()

# bytes1 = base64toStr2.decode('ascii')
# file0 = open('converted_save.planet', 'x')
# file0.close()
# decl_bytes0 = base64toStr1.encode('utf-8')



# decode('ascii')