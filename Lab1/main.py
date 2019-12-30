a = b = c = [1, 2, 3]

print(a, b, c)
print(id(a), id(b), id(c))

a += [4]

print(a, b, c)
print(id(a), id(b), id(c))

x = 10
y = 10
print(x, y)
print(id(x), id(y))

y = y + 1234567890 - 1234567890
print(x, y)
print(id(x), id(y))

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

workdays = days #(days[:-2]).copy()
print(days)
print(workdays)

options = ['load data', 'export data', 'analyze & predict']


def DisplayOptions():
    print("1-s" + "\n" + "2=ex" + "\n" + "3-anal" + "\n" + "select or enter")

choice='x'
flag = True
while flag:
    DisplayOptions()
    choice = input("Wybierz opcje:")
    print("wybrales"+str(choice)+"\n")
    if choice:
        try:
            choice_num = int(choice)
            print("ale mamy"+str(choice_num)+"\n")
            if 0 < choice_num <= 3:
                print("zostalo wybrane" + str(choice_num))
            else:
                print("Dokonano zlego wyboru")
        except:
            print("ma byc wprowadzona liczba")
    else:
        print("koncze dzialanie programu")
        flag = False
