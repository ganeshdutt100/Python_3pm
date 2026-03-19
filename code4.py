# nested 
# num  = -4

# if num>=0:
#     if num == 0:

#         print("The number is zero")
#     else:
#         print("The number is positive")
# else:
#     print("The number is negative")    
    
pin_input = 9876
balance  = 40000
withdraw_amount = 4000

if pin_input == 1234:
    print("PIN sahi hai!")

    if withdraw_amount <= balance:
        print("Withdrawal successful!")
    else:
        print("Error:  Balance Kam hai")    
else:
    print("PIN galat hai.")    