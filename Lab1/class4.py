# class Cake:
#     known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
#     bakery_offer = []
#
#     def __init__(self, name, kind, taste, additives, filling, gluten_free):
#
#         self.name = name
#         if kind in self.known_kinds:
#             self.kind = kind
#         else:
#             self.kind = 'other'
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.__gluten_free = gluten_free
#         self.bakery_offer.append(self)
#
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:    {}".format(self.kind))
#         print("Taste:   {}".format(self.taste))
#         print("Gluten free {}".format(self.__gluten_free))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling: {}".format(self.filling))
#         print('-' * 20)
#
#     def set_filling(self, filling):
#         self.filling = filling
#
#     def add_additives(self, additives):
#         self.additives.extend(additives)
#
#
# cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False)
# cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', True)
# cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True)
# cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False)
#
# print("Today in our offer:")
# for c in Cake.bakery_offer:
#     c.show_info()
#
# print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
# print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
# print('vars cake01', vars(cake01))
# print('vars Cake?', vars(Cake))
# print('dir cake01', dir(cake01))
# print('dir Cake?', dir(Cake))
#
# cake01._Cake__gluten_free = True
# cake01.show_info()
# print(vars(cake01))
#

class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False)
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False)
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True)
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False)

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

cake03.__gluten_free = False
print(dir(cake03))
cake03._Cake__gluten_free = False
cake03.show_info()