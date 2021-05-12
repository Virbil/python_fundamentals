class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def make_sound(self, sound="speak"):
        print(f"The sound I use to communicate is: {sound}")

    def add_lion(self, name):
        self.animals.append( Lion(name) )
        return self

    def add_lemur(self, name):
        self.animals.append( Lemur(name) )
        return self

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Lion(Zoo):
    def __init__(self, zoo_name):
        super().__init__(zoo_name)

    def make_sound(self, sound):
        print(f"The sound I use to communicate is: {sound}! I am a Lion")

    def to_hunt(self, gender):
        print(f"The {gender} hunts for food")

    def display_info(self):
        print(f"I am a Lion named: {self.name}")

class Lemur(Zoo):
    def __init__(self, zoo_name):
        super().__init__(zoo_name)

    def make_sound(self, sound):
        print(f"The sound I use to communicate is: {sound}! I am a Lemur")

    def to_forage(self, food):
        print(f"My favorite food is: {food}!")
        
    def display_info(self):
        print(f"I am a lemur named: {self.name}")


zoo1 = Zoo("Bryce's Zoo")
zoo1.add_lion("Nala").add_lion("Simba").add_lemur("Julien").add_lemur("Maurice")
zoo1.print_all_info()
zoo1.animals[0].make_sound("roar")
zoo1.animals[2].make_sound("call")
zoo1.animals[1].to_hunt("female")
zoo1.animals[3].to_forage("figs")