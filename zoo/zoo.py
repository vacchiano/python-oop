from animals import Animal, Lion, Tiger, Bear

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_new_lion(self, name):
        self.animals.append(Lion(name))
    def add_lion(self, name):
        self.animals.append(name)
    def add_new_tiger(self, name):
        self.animals.append(Tiger(name))
    def add_new_bear(self, name):
        self.animals.append(Bear(name))
    def print_info(self):
        print("-"*20, self.name, "-"*20)
        for animal in self.animals:
            animal.display_info()
        print("-"*(42+len(self.name)))


#run this if calling file itself
if __name__ == '__main__':

    my_zoo = Zoo("Dom's Zoo")
    Tim = Lion("Tim")
    my_zoo.add_lion(Tim)
    my_zoo.add_new_tiger("Jim")
    my_zoo.add_new_bear("Jay")
    my_zoo.add_new_bear("Jimbo")
    my_zoo.print_info()

    Tim.feed()
    my_zoo.print_info()

