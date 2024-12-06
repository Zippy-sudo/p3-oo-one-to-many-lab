import ipdb

class Pet:

    all = []

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type , owner = "None"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise ValueError("Pet Type must be a valid pet type")
    
    def __repr__(self):
        return f"{self.name} {self.pet_type} {self.owner}"


class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("Argument must be an instance of Pet")

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)

# owner = Owner("John")
# pet1 = Pet("Fido", "dog", owner)
# pet2 = Pet("Clifford", "dog", owner)
# pet3 = Pet("Whiskers", "cat", owner)
# pet4 = Pet("Jerry", "reptile", owner)


# ipdb.set_trace()