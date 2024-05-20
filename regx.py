import re



pattern = re.compile('^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$')
print(pattern.search('john@example.com'))

text = "Jwings Acadamy powered by James"

print(re.search('^Jwings.*James$',text))
print(re.findall('James',text))
x = re.sub("\s",",",text,1)
print(x)