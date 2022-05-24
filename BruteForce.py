import random
import time
#import timeit

from timeit import default_timer as timer

bit = int(8)
num = int(2)
n = int(0)

i = num**bit

number = random.randint(0, i-1)
print(bit,"bit-rand:",number)

#startt = time.time()
start = timer()


while n < number:
#    print (n)
    n = n+1
    if n == number:
        end = timer()
        print("COMPLITE")
        print("corect",n)
        #print("all time=",time.perf_counter())
        break

timer = (end - start) * 1000
#endd = time.time()
print("work time=",timer)
#print(endd - startt)
#print(end - start)



