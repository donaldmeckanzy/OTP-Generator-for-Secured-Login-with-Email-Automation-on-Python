# import libraries we need

import math, random, smtplib, ssl 

# Get your email here
sender_email = input("type your email address here:") 

# function to generate OTP

def generateOTP() :
 

    # Declare a digits variable  

    # which stores all digits 

    digits = "0123456789"

    OTP = ""
 

   # length of password can be changed

   # by changing value in range

    for i in range(6) :

        OTP += digits[math.floor(random.random() * 10)]
 

    return OTP
 
# Driver code

if __name__ == "__main__" :

     

    print("Your OTP is: ", generateOTP())

# you don't have to print the OTP here, we will use it later

port = 587  # For starttls
smtp_server = "smtp.gmail.com"

#sender_email = " " we added this through the input command earlier

receiver_email = "donaldeffizy@gmail.com"
password = input("Type your password and press enter:")

message = f"""\
Subject: Your Secure OTP from Donald

Hi sender_email, This is your OTP {generateOTP()} Please do not share it with anyone."""


context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
 