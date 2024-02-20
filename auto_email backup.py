import math
import random
import smtplib      #SMTP - Simple mail transfer protocol
from email.mime.text import MIMEText
from tkinter import *

def otp_generator():
    digits="0123456789"
    OTP = ""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    return OTP


def automatic_email(OTP,name,email,pwd):
    #user = input("Enter your name : ")
    #email = input("Enter your Email : ")
    #pwd = input("Enter your Gmail password : ")
    message = (f"Dear {name}, welcome to TheWorld! Your OTP is {OTP}")
    try:
        # Create a secure MIME text email
        msg = MIMEText(message, 'plain')
        msg['Subject'] = "TheWorld OTP Verification"
        msg['From'] = "shivkumar.nagre.cs@ghrcem.raisoni.net" 
        msg['To'] = email
        # Connect to SMTP server with secure TLS
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("shivkumar.nagre.cs@ghrcem.raisoni.net", pwd)  
        server.sendmail('shivkumar.nagre.cs@ghrcem.raisoni.net',email,msg.as_string())
        server.quit()
        print("Varification email sent successfully!")

    except (smtplib.SMTPException, smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused) as e:
        print("Error sending email:", e)

    except Exception as e:
        print("Unexpected error:", e)

def verify_otp(entered_otp, generated_otp): 
    print(entered_otp, generated_otp)
    if entered_otp == generated_otp:
        print("Verified!")
    else:
        print("Please check your OTP again!")

def gui_window():
    #Create root window
    root = Tk() 
    root.title("Email verification!")
    root.geometry('550x300')    #Set geometry(WxH)

    name_lable = Label(root, text="Enter your name:") #Craeting lable to instruct a user
    name_lable.pack()
    name_field = Entry(root, width=30) #Input field with 20 char
    name_field.pack() #Place input field on the window
   
    email_lable = Label(root, text="Enter your email:")
    email_lable.pack()
    email_field = Entry(root,width=30)
    email_field.pack()
   
    pwd_lable = Label(root, text="Enter your password:")
    pwd_lable.pack()
    pwd_field = Entry(root, width=30)
    pwd_field.pack()

    #Generate OTP button
    generated_otp = otp_generator()
    generate_otp_btn = Button(root, text="Generate OTP", command=lambda: automatic_email(generated_otp, name_field.get(), email_field.get(),pwd_field.get()))
    generate_otp_btn.pack()
    
    #OTP entry field and verification button
    otp_label = Label(root, text="Enter OTP:")
    otp_label.pack()
    otp_field = Entry(root, width=30)
    otp_field.pack()

    verify_otp_btn = Button(root, text="Verify OTP", command=lambda: verify_otp(otp_field.get(), generated_otp))
    verify_otp_btn.pack()
   
    root.mainloop()

gui_window()

