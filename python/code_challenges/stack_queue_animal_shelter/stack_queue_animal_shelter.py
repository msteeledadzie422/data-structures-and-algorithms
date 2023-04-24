class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None


class AnimalShelterTest:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if animal.species != 'cat' and animal.species != 'dog':
            print('We only take cats or dogs')
            return
        if animal.species == 'cat':
            if not self.cats.front:
                self.cats.front = animal
                self.cats.back = animal
            self.cats.back.next = animal
            self.cats.back = animal
        if animal.species == 'dog':
            if not self.dogs.front:
                self.dogs.front = animal
                self.dogs.back = animal
            else:
                self.dogs.back.next = animal
                self.dogs.back = animal

    def dequeue(self, pref):
        if pref != 'cat' and pref != 'dog':
            return None
        if pref == 'dog':
            if self.dogs.front:
                output = self.dogs.front
                self.dogs.front = self.dogs.front.next
                if not self.dogs.front:
                    self.dogs.back = None
                return output
            else:
                print('We don\'t have any dogs at the moment')
                return
        if pref == 'cat':
            if self.cats.front:
                output = self.cats.front
                self.cats.front = self.cats.front.next
                if not self.cats.front:
                    self.cats.back = None
                return output
            else:
                print('We don\'t have any cats at the moment')
                return
