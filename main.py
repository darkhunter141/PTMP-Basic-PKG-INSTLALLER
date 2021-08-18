# -*- coding: utf-8 -*-
import os
# here os means operating system.
os.system ("clear")
# os.system ("clear") means clear the terminal
# Now time to Banner Printing :)
print ('''
  ____            _        _____  _  _______ 
 |  _ \          (_)      |  __ \| |/ / ____|
 | |_) | __ _ ___ _  ___  | |__) | ' / |  __ 
 |  _ < / _` / __| |/ __| |  ___/|  <| | |_ |
 | |_) | (_| \__ \ | (__  | |    | . \ |__| |
 |____/ \__,_|___/_|\___| |_|    |_|\_\_____|
                                             
                                             
''')

# Text To Ascii Art converter site : https://patorjk.com/software/taag/
print (" Basic Pkg Installer Tools")
print ("\n Coded By Your Name ")

# "\n" means new line 

print ("\n $ PKG List : ")

print ("\n 1 . Python")
print ("\n 2 . SSH")
print ("\n 3 . Ruby")
print ("\n 4 . Wget")

print ("\n")

# pkg name done 
# pkg installation process 
def pkg () :
    os.system ("apt update && apt upgrade")
    os.system ("apt install python2")
    os.system ("apt install ruby")
    os.system ("apt install openssh")
    os.system ("apt install wget")

# def pkg () : means , pkg is a function 

# input
res = input ("Do You Want To install all pkgs ? (y or n) : ")

if res == "y" :
    pkg ()
   
else :
    print ("Good Bye")
    exit ()
    
# Done :*)
