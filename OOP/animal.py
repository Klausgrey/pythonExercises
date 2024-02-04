class livingThings:
    def __init__(self, kingdom, sounds):
        self.kingdom = kingdom
        self.sounds = sounds

class bird(livingThings):
    # def __init__(self, kingdom, sounds):
    #     super().__init__(kingdom, sounds)
        # self.kingdom = kingdom
    pass

class dog(livingThings):
    # def __init__(self, kingdom, sounds):
    #     super().__init__(kingdom, sounds)
    pass

class plants(livingThings):
    # def __init__(self, kingdom, sounds):
    #     super().__init__(kingdom, sounds)
    pass

p = bird("Aves", "Chrip Chrip")
q = dog("Marmalia", "Bark!!!")
r = plants("Plante", "No sound!!!")

print(f" Bird belongs to the {p.kingdom} and make {p.sounds} noises")
print(f" Dogs belongs to the {p.kingdom} and make {p.sounds} noises")
print(f" Plants belongs to the {p.kingdom} and make {p.sounds} noises")