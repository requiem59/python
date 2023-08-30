class Animales:
    def __init__(self, alim, habitat):
        self.alim = alim
        self.habitat = habitat
        print("Se creó un animal {} que vive en {}".format(alim, habitat))
        
cabra = Animales("herviboro", "montañas")

hiena = Animales("carnivoro", "sabana")