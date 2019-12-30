import math
argument_list=[]

for i in range (100):
    argument_list.append(i/10)

print(argument_list)

formula=input("Wpisz wzor\n")

for x in argument_list:
    print(eval(formula))