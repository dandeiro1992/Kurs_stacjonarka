def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8

transformations = [double, root, div2, negative]
list = [root, root, div2, double]
tmp_return = number

for a in transformations:
    tmp_return = a(tmp_return)
    print(tmp_return)
print("number {}".format(number))
tmp_return=number
for a in list:
    tmp_return = a(tmp_return)
    print(tmp_return)