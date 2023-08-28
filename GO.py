class Human:
    def __init__(self, name, age, nationality, city):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.city = city


    def pokazaniya(self):
        print(f"name: {self.name}"
        f"\n age: {self.age}"
        f"\n nationality: {self.nationality}"
        f"\n city: {self.city}")


class Young(Human):
    def __init__(self, name, age, nationality, city, teeth, hair):
        super().__init__(name, age, nationality, city)
        self.teeth = teeth
        self.hair = hair


class Old(Human):
    def __init__(self, name, age, nationality, city, wrinkles, problems):
        super().__init__(name, age, nationality, city)
        self.wrinkles = wrinkles
        self.problems = problems



vova = Young("vova", 14, "rus", "volgograd", 28, 150000)

vasili = Old("vasili", 77, "uk", "kiev", 4, 1)

vova.pokazaniya()
vasili.pokazaniya()




#сам писал чесна чесна)))