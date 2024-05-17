
def vow(text):
    vowels = ['a','e','i','o','u']

    count = 0
    for char in text:
        if char.lower() in vowels:
            count+=1
            

    return count

text = input("enter string")
x = vow(text)
print(x)

