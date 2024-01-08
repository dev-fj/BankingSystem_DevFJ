#%%



def SistemaBancario():

    global extrato, saldo, limite

    while True:
            try:
                
                print("""
If you want to Withdraw -> Type [1]
If you want to Deposit -> Type [2]
If you want to access the Statement -> Type [3]
To exit -> Type [0]
                      
                      """)
                print("".center(80,"+"))
                print()
                t1 = int(input("Choose an option: \n>"))

                if t1 == 1:
                    
                    if limite ==0:
                        templete("You have reached the daily withdrawal limit (3 per day)")

                    elif saldo == 0:
                        templete("You do not have sufficient funds to make a withdrawal.")
                    elif saldo > 0 and limite > 0:
                        while True:
                            try:
                                print()
                                print("Withdrawal option".upper())
                                saque = float(input("""
How much do you want to withdraw?

If you want to return to the main menu,
type any letter and press Enter. 
                                                    
>"""))

                                if saque > 500:
                                    templete("Withdraw a maximum of $500.00")

                                elif saque <= 0:
                                    templete("The withdrawal amount must be greater than $ 0.00")

                                elif (saque > 0) and (saldo < saque):
                                    templete("Nice try.")

                                elif (saque > 0) and (saldo >=saque):
                                    saldo -= saque
                                    extrato += f"-${saque:.2f}\n"
                                    limite -= 1

                                    templete(f"""
Withdrawal of ${withdrawal:.2f} successful.
Current balance: ${balance:.2f}""")
                                    break

                            except ValueError:
                                break
                    # else:
                    #     None

                elif t1 == 2:

                    while True:
                        try:
                            print()
                            print("Deposit option\n".upper())
                            deposito = float(input("""
Enter the deposit amount:

If you want to return to the main menu,
type any letter and press Enter.
                                                   
>"""))
                            


                            if deposito >= 0:
                                saldo += deposito
                                extrato += f"+${deposito:.2f}\n"
                                templete(f"""
Deposit of ${deposit:.2f} successful.
Current balance: ${balance:.2f}""")
                                break
                            else:
                                print("""
Incorrect value. 
Please enter a positive numerical value.
Example: 50.00""")
                                
                        except ValueError:
                            break

                elif t1 == 3:

                    if extrato == "":
                        templete("""
                                    STATEMENT

                                    R$ 0,00
                                 """)

                    else:
                        templete(f"""
STATEMENT:
                                 
{extrato}

Total balance: ${saldo:.2f}""")
                        

                elif t1 == 0:
                    templete("""
                                Thank you for coming. 
                               Your money is safe with us. 
                                Come back anytime.""")
                    break

                else:
                    print("""

I need a number between 0 and 3.
Please enter the desired option without using [ ].
For example: 1""")

            except ValueError:
                print("""
I need a number.
Please enter the desired option without using [ ].
For example: 1 """)

    return

def templete(y):
    x = ""
    x += y
    logo1 = " Banco Python "
    print()
    print(logo1.center(80,'+'))
    print()
    print(x.center(80))
    print()
    print("".center(80,'+'))
    print()
    print()






extrato = ""
limite = 3
saldo = 0

templete("We at Python Bank welcome you to the bank of your dream$ !")


SistemaBancario()