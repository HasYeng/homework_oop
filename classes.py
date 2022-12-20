class Dog:
    def __init__(self, name, breed, owner):
        self._name = name
        self._owner = owner
        self._breed = breed

    def change_name(self, name):
        self._name = name

    def change_owner(self, new_owner):
        self._owner = new_owner

    def get_name(self):
        return f'{self._name}'

    def get_owner(self):
        return f"{self._name}'s owner is {self._owner}"

    def get_breed(self):
        return f"{self._name} is a {self._breed}"


dog1 = Dog("Max", "Husky", "Jessy")
dog2 = Dog("Oddy", "Labrador", "Nick")
print(dog1.get_name())
dog1.change_name("Kit")
print(dog1.get_name())
print(dog1.get_owner())
print(dog1.get_breed())
print(dog2.get_name())
dog2.change_owner("Emma")
print(dog2.get_breed())


class Helicopter:
    def __init__(self, model):
        self._model = model
        self._speed = 0
        self._fuel = False

    def get_model(self):
        return f'{self._model}'

    def filling_tank(self):
        if not self._fuel:
            self._fuel = True
        else:
            print("Tank is full")

    def flight(self):
        if not self._fuel:
            print("Please fill the tank")
        else:
            for i in range(6):
                self._speed += i
                print(f"current speed {self._speed}")
            for i in range(-5, 0):
                self._speed += i
                print(f"current speed {self._speed}")


heli = Helicopter("SA315B Lama")
heli.flight()
heli.filling_tank()
heli.filling_tank()
heli.flight()


class Hospital:
    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._patient_count = 0

    def get_name(self):
        return f'{self._name}'

    def get_city(self):
        return f'{self._city}'

    def patient_count(self):
        return f'current patient_count{self._patient_count}'

    def admit_patients(self):
        self._patient_count += 1

    def discharge_patients(self):
        if self._patient_count > 0:
            self._patient_count -= 1
        else:
            print("All patients are healthy")


hospital = Hospital("ABc", "Yerenan")
hospital.get_city()
hospital.get_name()
hospital.admit_patients()
hospital.admit_patients()
hospital.admit_patients()
hospital.discharge_patients()
hospital.discharge_patients()
print(hospital.patient_count())
hospital.admit_patients()
print(hospital.patient_count())
hospital.discharge_patients()
hospital.discharge_patients()
hospital.discharge_patients()
