import random
import string

passwordLength = 10
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""

res = "".join(random.sample(charValues, passwordLength))
print(res)

# for i in range(passwordLength):
#     password += random.choice(charValues)
    
# print("Your random password is : ",password)
print("Your random password is : ",res)
