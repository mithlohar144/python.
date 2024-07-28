email = str(input("Enter your email :"))
if len(email)>= 6:
    if email[0].isalpha():
       if ("@" in email) and (email.count("@")==1):
           pass
       else:
           print("Wroung Email 3...")
    else:
        print(" Wroung Email 2...")
else:
    print(" Wroung Email 1... ")
