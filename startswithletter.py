
import string

def starts_with_name(names):
    for name in names :
        if name.startswith('A') or name.startswith('a'):
            print(name)

names = ['james','jonas','alice','akmal']
starts_with_name(names)