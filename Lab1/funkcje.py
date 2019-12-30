import os


def show_progress(how_many, character='*'):
    print(character * how_many)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')


def calculate_paint(efficiency_ltr_per_m2, *args):
    counter = 0
    for a in args:
        counter += a
    return counter * efficiency_ltr_per_m2


print(calculate_paint(5, 6, 3, 1, 2))

list = [10, 9, 8, 7, 6]

print(calculate_paint(5, *list))


def log_it(*args):
    path = os.getcwd() + '/log_it.txt'
    with open(path, 'a+') as file:
        for a in args:
            file.write(a + " ")
        file.write("\n")
    file.close()

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')