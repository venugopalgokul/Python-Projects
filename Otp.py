# import library
import random
# function to generate OTP
Mobile=input("Enter Your Mobile Number:")
if len(Mobile)==10:
    print("OTP Send To Your Mobile Number")
    OTP=random.randrange(0000,10000)
    print("Your OTP:",OTP)
    user=int(input("Enter Your OTP:"))
    if OTP==user:
        print("Verified Successfully")
    else:
        print("Invalid OTP,  Please Enter Valid OTP")
else:
   print("Please Enter Your 10 digit's Moblie Number")
   
