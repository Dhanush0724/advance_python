from time import sleep
from threading import *
class Hello(Thread):
    def run(Self):
        for i in range(10):
            print("Hello")
            sleep(0.2)

class Hi(Thread):
    def run(Self):
        for i in range(10):
            print("Hi")
            sleep(0.2)

t1 = Hello()
t2 = Hi()

t1.start()
t2.start()

t1.join()
t2.join()
print("Bye")