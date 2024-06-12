from collections import Counter

arr = [1,2,3,4,6,1,2,3,4,5,2,5]
x = Counter(arr)
print(x)

for i in x.keys():
    print(i,":",x[i])

max_count = max(x.values())
print(max_count)
min_count = min(x.values())
print(min_count)
# max_key = None
# for key,value in x.items():
#     if value==max_count:
#         max_key = key
#         break
max_keys = [key for key, values in x.items() if values==max_count]

min_keys = [key for key,values in x.items() if values == min_count ]
print("Key with maximum count",max_keys)
print("Key with minimum count",min_keys)
    