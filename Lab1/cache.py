import time
import functools

@functools.lru_cache()
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start=time.time()

for i in range (35):
    stop=time.time()
    print("i\t"+str(i)+"\t"+str(fib(i))+"\t time: "+str(stop-start))

print()