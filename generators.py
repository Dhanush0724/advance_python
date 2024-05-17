def fib(n):
    a,b =0,1

    while a<n:
        yield a
        a,b = b,a+b

x = fib(6)
print(next(x))
print(next(x))

generator_exp = (i**2 for i in range(1,5) if i%2==0)

for i in generator_exp:
    print(i)