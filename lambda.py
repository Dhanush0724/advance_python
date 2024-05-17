from functools import reduce
nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda n: n%2==0,nums))
print(evens)
sq = list(map(lambda n:n**2,evens))
print(sq)
add = reduce(lambda a,b:a+b,sq)
print(add)