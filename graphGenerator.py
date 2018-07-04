#####################################################
#
# Coded by: Enrique B. Dutra
# In : 07/03/18
#
#####################################################
import random
import string
numberNodes = int(input())
print(numberNodes)


for x in range(numberNodes):
    print(''.join(random.choices(string.ascii_uppercase, k=numberNodes%26)) + "      " + str(random.randint(0, 30)))






        

