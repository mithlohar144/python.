import random
import string

pass_len = 12
charValue = string.ascii_letters + string.digits + string.punctuation

# list comprehension [function i in range(n)]

password = "".join([random.choice(charValue) for i in range(pass_len)])

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValue)


print("Your Randam pasword is :" , password)   