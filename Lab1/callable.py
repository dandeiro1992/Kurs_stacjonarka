class NoDuplicates:
    lista_klasy=[]
    def __init__(self):
        self.list=[]

    def __call__(self, lista):
        self.new_items=lista.copy()
        for x in self.new_items:
            if x not in self.list:
                self.list.append(x)
                NoDuplicates.lista_klasy.append(x)


my_no_dup_list=NoDuplicates()

print(my_no_dup_list.list)

my_no_dup_list(["keyboard", "mouse"])
print(my_no_dup_list.list)
dama=NoDuplicates()
dama(["damian"])
print(dama.list)
print(dama.lista_klasy)
my_no_dup_list(['keyboard','mouse','pendrive'])
print(my_no_dup_list.list)