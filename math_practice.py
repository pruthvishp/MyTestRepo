import math
print(10%3)
print(-10%3) # prints unexpected modulus
print("modulus using math module")
print(math.fmod(10,3))
print(math.fmod(-10,3)) # prints expected output
print(10/3)
print(10//3)
print(-10/3)
print(-10//3) # unexpected rounds away from 0
print(int(-10/3)) # this works around to 
print('floor')
print(math.floor(10/3)) #round to lower
print(math.floor(-10/3)) #round to lower
print(math.ceil(10/3)) #round to higher
print(math.ceil(-10/3))
print("power")
print(pow(2,3))
print(pow(2, -3))
print(pow(2, 3.5))
print(math.sqrt(2))
#float(intf)
#float(-intf)
print(10//3 == math.floor(10/3))
print(-10//3 == math.floor(-10/3))



