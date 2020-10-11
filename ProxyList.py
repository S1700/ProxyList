#!/usr/bin/env python3
import requests
import os
# from lxml import html, etree
# import sys
# import time
Otp1 = "Test"
Otp2 = "Test2"
Otp3 = "Test3"
Otp4 = "Test4"
Otp5 = "Test5"

os.system('clear')

print("""

\033[1;37;37m██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
                                                          Samuel20354

Please select a proxy level
Use Ctrl+C to skip any question

\033[1;31m1)\033[1;31m Elite

\033[1;31m2)\033[1;31m Anonymous

\033[1;31m3)\033[1;31m Transparent (Not Recomanded)


""")

try:                                                               
    num = int(input("OPTION : "))

    if num == 1:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
        
                Opt1 = ("elite")
   
        except:
            print (" Error ")

    elif num == 2:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt1 = ("anonymous")
                
        except:
            print (" Error ")
            
    elif num == 3:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt1 = ("transparent")
                
                
        except:
            print (" Error ")

    else:
        print("\nPlease select a valid option \n")

except KeyboardInterrupt:
    print ("\nCanceled by user \n")
    
os.system('clear')

print("""

\033[1;37;37m██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
                                                          Samuel20354

Please select a proxy protocal

\033[1;31m1)\033[1;31m Socks5

\033[1;31m2)\033[1;31m Socks4

\033[1;31m3)\033[1;31m Https

\033[1;31m4)\033[1;31m Http (Not Recomanded)

""")


try:                                                               
    num = int(input("OPTION : "))

    if num == 1:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
        
                Opt2 = ("&sock5")
   
        except:
            print (" Error ")

    elif num == 2:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt2 = ("&socks4")
                
        except:
            print (" Error ")
            
    elif num == 3:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt2 = ("&https")
                
        except:
            print (" Error ")
            
    elif num == 4:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt2 = ("&http")
                
        except:
            print (" Error ")

    else:
        print("\nPlease select a valid option \n")

except KeyboardInterrupt:
    print ("\nCanceled by user \n")    
    
    
os.system('clear')

print("""

\033[1;37;37m██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
                                                          Samuel20354

Please type a proxy port

\033[1;31m20, 21, 22, 80, 81, 443, 8080, 8081

\033[1;31m(0 = Any/Random)

\033[1;31mNote: Some port may not work

""")


try:                                                               
    num = int(input("OPTION : "))

    if num == 0:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
        
                Opt3 = ("")
   
        except:
            print (" Error ")

    elif num == 20:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt3 = ("&port=20")
                
        except:
            print (" Error ")
            
    elif num == 21:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt3 = ("&port=21")
                
        except:
            print (" Error ")
            
    elif num == 22:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt3 = ("&port=22")
                
        except:
            print (" Error ")
            
    elif num == 80:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt3 = ("&port=80")
                
        except:
            print (" Error ")
            
    elif num == 81:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt3 = ("&port=81")
                
        except:
            print (" Error ")
            
    elif num == 443:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt3 = ("&port=443")
                
        except:
            print (" Error ")
            
    elif num == 8080:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt3 = ("&port=8080")
                
        except:
            print (" Error ")
            
    elif num == 8081:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
            
                Opt3 = ("&port=8081")
                
        except:
            print (" Error ")
            
    else:
        print("\nPlease select a valid option \n")

except KeyboardInterrupt:
    print ("\nCanceled by user \n")   
    
os.system('clear')

print("""

\033[1;37;37m██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
                                                          Samuel20354

Please select the proxy country
(Country Code Alpha-2 Only eg: GB, US)

\033[1;31m

""")


try:                                                               
    num = str(input("OPTION : "))

    Opt4 = (num)

except KeyboardInterrupt:
    print ("\nCanceled by user \n") 
    
    
os.system('clear')

print("""

\033[1;37;37m██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
                                                          Samuel20354

Please type a list limit
(How many proxys you want to be listed)
\033[1;31m

""")


try:                                                               
    num = int(input("OPTION : "))

    Opt5 = (num)
    
except KeyboardInterrupt:
    print ("\nCanceled by user \n") 
    
os.system('clear')

print("""

\033[1;37;37m██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
                                                          Samuel20354

Please Select 1 to conform
\033[1;31mNote: There might be less IP's then requested

""")

print('\n')

try:                                                               
    num = int(input("OPTION : "))

    if num == 1:
        print("\n")     
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (1,2):
        
                url = ("https://www.proxyscan.io/api/proxy?format=txt&level="+str(Opt1)+str(Opt2)+str(Opt3)+"&"+str(Opt4)+"&"+str(Opt5))
                res = requests.post(url, headers=headers)
                
                print(res.text)
   
        except:
            print (" Error ")
            
    else:
        print("\nPlease select a valid option \n")

except KeyboardInterrupt:
    print ("\nCanceled by user \n")
