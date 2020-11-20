#Caesar's Cipher Algorithm
import smtplib
import time
import getpass

def mail(encrypted):
    server = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
    eid= input("Enter your email-id\n")
    epass= getpass.getpass(prompt= "Enter your password\n")
    server.login(eid,epass)
    sid= input("Enter Receiver's id:\n")
    server.sendmail(eid, sid, encrypted)
    print("Mail Sent!")
    server.quit()


def enc():
    message= input("Type your text!\n")
    value=3
    encrypted=""
    series= "abcdefghijklmnopqrstuvwxyz"
    series+=series.upper()
    series+=" "

    for letter in message:
        position=series.find(letter)
        new_position= (position+value)%52
        if letter== " ":
            encrypted+=" "
        else:
            encrypted+=series[new_position]
    print("Encrypted text: "+ encrypted )
    mail(encrypted)

enc()