#Created by Joseph D. Cline Jr. ID: 060T9YXZD0 Copyright © 2018 JoeCline.
#This program is a calculator that prompts for 5 inputs, it takes the 5 inputs and computes the cost for each option picked by the user. It displays the price to the user and ask if the user wants to keep its options or start over.

import time
def roomidea():
    sBedsize = input("For your room do you want a queen-size bed or a king-size bed? Type Queen for queen-size or King for king-size:\t")
    sRoomview = input("For your room do you want the standard view or the atrium view? Type Standard for standard-view or Atrium for atrium-view:\t")
    sVehicle = input("Will you be parking at our hotel? Type Yes if you are, or No if you are not:\t")
    iRoomnum = int(input("Please enter the amount of rooms you wish to check out:\t"))
    iNights = int(input("Please enter the amount of nights you wish to stay:\t"))
    return sBedsize, sRoomview, sVehicle, iRoomnum, iNights


def price(iRoomnum, iNights):
    dPrice1 = iNights * 280
    dPrice2 = iNights * 320
    dPrice3 = iNights * 295.50
    dPrice4 = iNights * 335.50
    dPrice5 = iNights * 15.75
    dResortfee1 = iNights * 20
    dResortfee2 = iRoomnum * 20
    dTotalqs = dPrice1 + dPrice5 + dResortfee1 + dResortfee2
    dTotalqa = dPrice2 + dPrice5 + dResortfee1 + dResortfee2
    dTotalqsv = dPrice1 + dResortfee1 + dResortfee2
    dTotalqav = dPrice2 + dResortfee1 + dResortfee2
    dTotalks = dPrice3 + dPrice5 + dResortfee1 + dResortfee2
    dTotalka = dPrice4 + dPrice5 + dResortfee1 + dResortfee2
    dTotalksv = dPrice3 + dResortfee1 + dResortfee2
    dTotalkav = dPrice4 + dResortfee1 + dResortfee2
    dTaxqs = dTotalqs * 0.15
    dTaxqa = dTotalqa * 0.15
    dTaxqsv = dTotalqsv * 0.15
    dTaxqav = dTotalqav * 0.15
    dTaxks = dTotalks * 0.15
    dTaxka = dTotalka * 0.15
    dTaxksv = dTotalksv * 0.15
    dTaxkav = dTotalkav * 0.15
    dOverallqs = dTotalqs + dTaxqs
    dOverallqa = dTotalqa + dTaxqs
    dOverallqsv = dTotalqsv + dTaxqs
    dOverallqav = dTotalqav + dTaxqs
    dOverallks = dTotalks + dTaxqs
    dOverallka = dTotalka + dTaxqs
    dOverallksv = dTotalksv + dTaxqs
    dOverallkav = dTotalkav + dTaxqs
    return dPrice1, dPrice2, dPrice3, dPrice4, dPrice5, dResortfee1, dResortfee2, dTotalqs, dTotalqa, dTotalqsv, dTotalqav, dTotalks, dTotalka, dTotalksv, dTotalkav, dTaxqs, dTaxqa, dTaxqsv, dTaxqav, dTaxks, dTaxka, dTaxksv, dTaxkav, dOverallqs, dOverallqa, dOverallqsv, dOverallqav, dOverallks, dOverallka, dOverallksv, dOverallkav

sBedsize, sRoomview, sVehicle, iRoomnum, iNights = roomidea()
dPrice1, dPrice2, dPrice3, dPrice4, dPrice5, dResortfee1, dResortfee2, dTotalqs, dTotalqa, dTotalqsv, dTotalqav, dTotalks, dTotalka, dTotalksv, dTotalkav, dTaxqs, dTaxqa, dTaxqsv, dTaxqav, dTaxks, dTaxka, dTaxksv, dTaxkav, dOverallqs, dOverallqa, dOverallqsv, dOverallqav, dOverallks, dOverallka, dOverallksv, dOverallkav = price(iRoomnum, iNights)

if  sBedsize == "Queen" and sRoomview == "Standard" and sVehicle == "Yes":
    print("The price for a Queen-Size bed with the Standard view and you are parking a vehicle, this comes to the total of $%.2f" % dTotalqs + " If this is how you want your room, type Yes, if you want to pick another option, type No.")
elif sBedsize == "Queen" and sRoomview == "Atrium" and sVehicle == "Yes":
    print("The price of Queen-Size bed with the Atrium view and you are parking a vehicle, this comes to the total of $%.2f" % dTotalqa + " If this is how you want your room, type Yes, if you want to pick another option, type No.")
elif sBedsize == "Queen" and sRoomview == "Standard" and sVehicle == "No":
    print("The price for a Queen-Size bed with the Standard view and you are not parking a vehicle, this comes to the total of $%.2f" % dTotalqsv + " If this is how you want your room, type Yes, if you want to pick another option, type No.")
elif sBedsize == "Queen" and sRoomview == "Atrium" and sVehicle == "No":
    print("The price for a Queen-Size bed with the Atrium view and you are not parking a vehicle, this comes to the total of $%.2f" % dTotalqav + " If this is how you want your room, type Yes, if you want to pick another option, type No.")
elif sBedsize == "King" and sRoomview == "Standard" and sVehicle == "Yes":
    print("The price for a King-Size bed with the Standard view and you are parking a vehicle, this comes to the total of $%.2f" % dTotalks + " If this is how you want your room, type Yes, if you want to pick another option, type No.")
elif sBedsize == "King" and sRoomview == "Atrium" and sVehicle == "Yes":
    print("The price for a King-Size bed with the Atrium view and you are parking a vehicle, this comes to the total of $%.2f" % dTotalka + " If this is how you want your room, type Yes, if you want to pick another option, type No.")
elif sBedsize == "King" and sRoomview == "Standard" and sVehicle == "No":
    print("The price for a King-Size bed with the Standard view and you are not parking a vehicle, this comes to the total of $%.2f" % dTotalksv + " If this is how you want your room, type Yes, if you want to pick another option, type No.")
elif sBedsize == "King" and sRoomview == "Atrium" and sVehicle == "No":
    print("The price for a King-Size bed with the Standard view and you are not parking a vehicle, this comes to the total of $%.2f" % dTotalkav + " If this is how you want your room, type Yes, if you want to pick another option, type No.")
else:
    print("You did not enter the information correctly")
time.sleep(5)
feedback = input("Would you like to change your room choices? Type Yes or No for the options:\t").upper()
if feedback == "YES":
    print("Thank you for picking a room with us, I hope you enjoy your room and we are hoping to see you back again!")
elif feedback == "NO":
    print("We are sorry that the room you picked isn't how you wanted it, please retype how you want your room, if you want to leave just type quit:\n")
    time.sleep(5)
