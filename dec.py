import time

series= "abcdefghijklmnopqrstuvwxyz"
series+=series.upper()
series+=" "

enc= input("Give encrypted message!\n")
val= 3

def dec(encrypted, value, series):
    decrypted=" "
    for letter in encrypted:
        position2= series.find(letter)
        og_position= (position2-value)%52
        if letter==" ":
            decrypted+=" "
        else:
            decrypted+=series[og_position]

    print("Decrypted Message: "+ decrypted)

dec(enc, val, series)