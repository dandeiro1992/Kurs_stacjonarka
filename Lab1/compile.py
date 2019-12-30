import math, time

formulas_list = ["abs(x**3 - x**0.5)", "abs(math.sin(x) * x**2)"]

argument_list = []
for i in range(1000000):
    argument_list.append(i / 10)

for i in formulas_list:
    result_list = []
    print(i)
    start = time.time()
    for x in argument_list:
        result_list.append(eval(i))
    print("mini {}  maxi {}".format(min(result_list), max(result_list)))
    stop = time.time()
    print("czas trwania obliczen {}".format(stop - start))


for i in formulas_list:
    result_list = []
    print(i)
    start = time.time()
    compiled_formula=compile(i,"wykonanie sie kodu",'eval')
    for x in argument_list:
        result_list.append(eval(compiled_formula))
    print("mini {}  maxi {}".format(min(result_list), max(result_list)))
    stop = time.time()
    print("czas trwania obliczen {}".format(stop - start))
