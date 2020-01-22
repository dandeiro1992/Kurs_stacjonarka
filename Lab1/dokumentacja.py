class Cake:
    """
    Tutaj jest dekumentowanie klasy
    """
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """

        :param name: v
        :param kind: fag
        :param taste: sf
        :param additives: sdd
        :param filling: ddsa
        """
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

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
        print('-' * 20)

    @property
    def full_name(self):
        """
        fdsafm
        :return:fsav
        """

        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

help(Cake)
print("@"*40)
help(Cake.full_name)