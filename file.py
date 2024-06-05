filename = input("enter the filename:")
f1 = open(filename)
N = int(input("enter the number of lines to be displayed"))
word = input("enter the word to count it's frequency")
linenumber = 0
for line in f1:
    if linenumber==N:
        break
    print(line)
    linenumber+=1
    f1 = open(filename)
    count = 0
    for line in f1:
        if word in line.split():
            count+=1
print("frequency of word %s in %d"%(word,count))