import datetime
exit = False
inserted = False
balance = 20000
actual_pin=None
blocked=None
attempt = 0
transactions=[]


while True:
    print("welcome to SBI")
    print("enter the ATM card")
    if not inserted:
        print("PLEASE insert card")
        x = int(input("1 for CONTINUE,2 for EXIT"))
        if x==1:
            inserted = True
            if blocked:
               print("your card has been blocked contack your branch for further quires")
               inserted=False
               continue
            if actual_pin== None:
                actual_pin = int(input("set your new PIN"))
                print("enter the PIN")
                pin=int(input())
                if pin == actual_pin:
                    while True:
                        print("1.DEPOSITE\n2.WITHDRAWAL\n3.MINI STATEMENT\n4.PIN CHANGE\n5.EXIT\n")
                        option=int(input("select one of the option above:"))
                        if option ==1:
                                print("deposite")
                                amount=int(input("enter the amount:"))
                                if amount%100 == 0:
                                        balance+=amount
                                        transactions.append(amount)
                                        print("cash has been accepted")
                                        print("Available balance=",balance)
                                else:
                                        print("feed the multiples 100 only")
                        if option ==2:
                                    print("withdrawal")
                                    amount=int(input("enter the amount:"))
                                    if amount<balance:
                                        if amount%100 == 0:
                                            balance-=amount
                                            transactions.append(-amount)
                                            print("cash has been withdrawed")
                                            print("Available balance=",balance)
                                        else:
                                            print("enter the multiples 100 only")    
                                    else:
                                        print("insufficient funds")  
                        if option==3: 
                            print("mini statement")
                            realtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            print(realtime)
                            print(transactions)
                            print(balance)

                        if option==4:
                            print("PIN change")
                            pin2=int(input("Enter the old PIN:"))
                            if pin2==pin:
                                 print("enter the new pin")
                                 pin3=int(input(":"))
                                 pin3=pin
                                 print("pin has been changed successfully")
                            else:
                                 print("incorrect old pin")
                        if option==5:
                             print("thank you visit again")
                             break  
                                        
            else:
              print("Invalid PIN")
              attempt+=1
              if attempt>=2:
                blocked=True
                print("ur card has been blocked")
        if x==2:
          print("thank you visit again")
            

    else:           
      inserted=False
      
 