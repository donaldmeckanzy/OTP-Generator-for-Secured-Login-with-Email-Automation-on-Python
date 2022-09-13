## OTP-Generator-for-Secured-Login-with-Email-Automation-on-Python

##### You've probably used an OTP (One Time Password) when registering at a Fintech app. And this OTP was generated and sent to your phone.  

##### In this article, I'll show you an easy way to create an OTP and send to a user's email address using Python. For this tutorial, we will create a six digit number for the OTP.


### Python Code to Receive User's Email Address:

	receiver_email_id = input("type your email address here:") 


### Creating the OTP 
If you think about it, it's the same way you will create the numbers on your Master Card if you were to work on a Fintech that needed you to write a code to generate Mastercard card details. 

You will only need to put certain functions or constraints depending on what you want to achieve. 

To generate the random six digit number, we will use the random.random and math libraries in Python. 

The code:

# import libraries 

	import math, random
 
# function to generate OTP

def generateOTP() :
 

## Declare a digits variable which stores all digits 

    digits = "0123456789"

    OTP = ""
 

   ## length of password can be changed by changing value in range

    for i in range(6) :

        OTP += digits[math.floor(random.random() * 10)]
 

    return OTP
 
### Driver code

	if __name__ == "__main__" :

     

    print("Your OTP is: ", generateOTP())
#### you don't have to print the OTP here, we will use it later


## Send OTP to User's Email Address:
For this we will use the SMTP (Simple Mail Transfer Protocol) 

First, disable 2 Step verification in your Gmail account or go to your Gmail account settings then select App password and follow the steps to generate a 16 digit password that you will put in place of your Gmail password. 

Ps: Your normal password won't work if 2 step verification is enabled in your account. 

##### Code Implementation:

	import smtplib

	s = smtplib.SMTP('smtp.gmail.com', 587)

We will send the email from your Gmail account and thus you need to put your email and password (or App password if you have 2 Step verification enabled). Then the email message will contain the OTP we generated earlier.

##### Code Implementation:

------------------------------------------

	import smtplib, ssl

	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "youremail@gmail.com"
	receiver_email = "yourfriends@gmail.com"
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
