import math
import random
import string

alpha = string.ascii_letters
nums = string.digits
symbol = string.punctuation

all_password = list(str(alpha+nums+symbol))

random.shuffle(all_password)
new_gen = ''.join(all_password)
length = int(input("Enter length of password:   "))

password = ''.join(random.sample(new_gen, length))

print(password)
