import random

target = random.randint(1 ,100)



while True:
    userchioce  = int(input("Gusse the Target or Quit(Q) :"))
    if(userchioce == "Q"):
        break

    userchioce == int(userchioce)
    if(userchioce == target):
        print("Succes : Carrect Target : ")
        break
    elif(userchioce < target):
        print("your number is to small. Please Try Again..")
    else:
        print("your number is to Big. Please Try Again..") 
print("____GAME OVER ___")