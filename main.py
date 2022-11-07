#Copyright 2022
#Author: MythticalPlayz
#Code: Log in System and check if the user is admin

#import the json file with the admins
import json
import base64
f = open("admins.json")
admins = json.load(f)

#set the login to false
loggedin = False

#import username from user
name = input("Enter your name \n")

#loop through the admins
for i in range(0,dict.__len__(admins)):
    admintocheck = "admin" + str(i)

    #check if admin[number] exists
    if dict.get(admins,admintocheck):

         #get its username
       adminname = dict.get(dict.get(admins,admintocheck),"name")
       if adminname == name:

        #get the password for the account encoded in base64
        pswrd = input("To verify that you are an Admin, Please enter your password:\n")
        pswrd = base64.b64encode(pswrd.encode("utf-8")).decode('utf-8')
        if pswrd ==  dict.get(dict.get(admins,admintocheck),"password"): 

            #log in the user as Admin
            print("Welcome:",name,"\nRank: Admin")
            loggedin = True
            break
        else:

             #password incorrect; log in the user as a user
            print("Error: Wrong Password \nLogging in as a user")
            break    

#See if user logged in 
if not loggedin:

    #log in the user as a user
    print("Welcome:",name,"\nRank: User")

#flush memory
f.flush()