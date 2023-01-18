#encoding: utf-8


class Perros(object):

    def ladra(self):
        return False

class PastorAleman(Perros):

    def ladra(self):
        ladra = super(PastorAleman, self).ladra()
        if ladra:
            return "Guau guau (alemán)"
        return False

class Chihuahua(Perros):

    def ladra(self):
        return "Guaui guaui"




firulais = PastorAleman()
print(firulais.ladra())


