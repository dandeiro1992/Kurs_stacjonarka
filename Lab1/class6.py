# import pickle
# import os
# import glob
#
#
# class Cake:
#     known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
#     bakery_offer = []
#
#     def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
#
#         self.name = name
#         if kind in self.known_kinds:
#             self.kind = kind
#         else:
#             self.kind = 'other'
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
#         self.__gluten_free = gluten_free
#         if kind == 'cake' or text == '':
#             self.__text = text
#         else:
#             self.__text = ''
#             print('>>>>>Text can be set only for cake ({})'.format(name))
#
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:        {}".format(self.kind))
#         print("Taste:       {}".format(self.taste))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling:     {}".format(self.filling))
#         print("Gluten free: {}".format(self.__gluten_free))
#         if len(self.__text) > 0:
#             print("Text:      {}".format(self.__text))
#         print('-' * 20)
#
#     def save_to_file(self, path):
#         with open(path, "wb") as file:
#             pickle.dump(self, file)
#
#     def read_from_file(self, path):
#         with open(path, "rb") as file:
#             m = pickle.load(file)
#         Cake.bakery_offer.append(m)
#         return m
#
#     def set_filling(self, filling):
#         self.filling = filling
#
#     def add_additives(self, additives):
#         self.additives.extend(additives)
#
#     def __get_text(self):
#         return self.__text
#
#     def __set_text(self, new_text):
#         if self.kind == 'cake':
#             self.__text = new_text
#         else:
#             print('>>>>>Text can be set only for cake ({})'.format(self.name))
#
#     @staticmethod
#     def get_bakery_files(folder):
#         print(glob.glob(folder+"*.bakery"))
#
#     Text = property(__get_text, __set_text, None, 'Text on the cake')
#
#
# cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
# cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
# cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
# cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')
#
# print("Today in our offer:")
# for c in Cake.bakery_offer:
#     c.show_info()
#
# cake01.Text = 'Happy birthday!'
# cake02.Text = '18'
#
# for c in Cake.bakery_offer:
#     c.show_info()
#
# path = os.getcwd() + "/plik.txt"
# path_2 = os.getcwd() + "/"
# cake01.save_to_file(path)
# cake05 = cake01.read_from_file(path)
# print("ola" * 20)
# cake05.show_info()
#
# cake01.get_bakery_files(path_2)

import pickle
import glob


class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):

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
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

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
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return __text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog + '/*.bakery')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

cake01.save_to_file('c:/temp/cake01.bakery')
cake02.save_to_file('c:/temp/cake02.bakery')

cake05 = Cake.read_from_file('c:/temp/cake01.bakery')
cake05.show_info()

print(Cake.get_bakery_files('c:/temp'))
