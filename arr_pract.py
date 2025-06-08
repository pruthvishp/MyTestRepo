a,b,c = [1,2,3]
print(a)
print(b)
print(c)

k = [1,2,3]
print(k[-1])

print(k[0:0])
print(k[0:1])
print(k[1:2])
print(k[0:-1]) #a:b means print from index a to index b-1

nums1 = [1,2,3]
alps1 = ['a','b','c']
print(zip(nums1 , alps1))

for index,value in enumerate(['a','b','c']):
    print(f'index of value {value} is {index}')
arr = ["aadsafaf", "sfsfsf", "df" , "a"]
arr.sort()
print(arr)
arr.sort(key = lambda x: len(x))
print(arr)
arr.sort(key = lambda x: 1/len(x))
print(arr)
print(ord("a")) #ascii

