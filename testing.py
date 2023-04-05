print ('Hello World')

import random
roll = random.randint(1,20)
print(roll)

num_array = []
for i in range(20):
    num_array.append(random.randint(1,100))

print(num_array)
print(num_array[random.randint(0,len(num_array))])