class Human:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def __repr__(self):
        return f"Людина (ім'я = {self.name}, вік = {self.age}, національність = {self.nationality})"

    def get_info(self):
        return f"Ім'я: {self.name}\nВік: {self.age}\nНаціональність: {self.nationality}"


class Builder(Human):
    def __init__(self, name, age, nationality, specialization):
        super().__init__(name, age, nationality)
        self.specialization = specialization

    def __repr__(self):
        return f"Будівельник (ім'я = {self.name}, вік = {self.age}, національність = {self.nationality}, спеціалізація = {self.specialization})"

    def get_info(self):
        info = super().get_info()
        return f"{info}\nСпеціалізація: {self.specialization}"


class Sailor(Human):
    def __init__(self, name, age, nationality, rank):
        super().__init__(name, age, nationality)
        self.rank = rank

    def __repr__(self):
        return f"Моряк (ім'я={self.name}, вік = {self.age}, національність = {self.nationality}, звання = {self.rank})"

    def get_info(self):
        info = super().get_info()
        return f"{info}\nЗвання: {self.rank}"


class Pilot(Human):
    def __init__(self, name, age, nationality, license_type):
        super().__init__(name, age, nationality)
        self.license_type = license_type

    def __repr__(self):
        return f"Пілот (ім'я={self.name}, вік = {self.age}, національність = {self.nationality}, тип ліцензії = {self.license_type})"

    def get_info(self):
        info = super().get_info()
        return f"{info}\nТип ліцензії: {self.license_type}"


builder1 = Builder("Іван", 35, "Україна", "Муляр")
print(builder1)
print(builder1.get_info())
print("----------------------------------------")

sailor1 = Sailor("Петро", 28, "Україна", "Матрос")
print(sailor1)
print(sailor1.get_info())
print("----------------------------------------")

pilot1 = Pilot("Марія", 42, "Україна", "Комерційний пілот")
print(pilot1)
print(pilot1.get_info())


# завдання 2
class Passport:
    def __init__(self, name, country, id_number, date_of_birth, expiry_date):
        self.name = name
        self.country = country
        self.id_number = id_number
        self.date_of_birth = date_of_birth
        self.expiry_date = expiry_date

    def __repr__(self):
        return f"Паспорт (ім1я = {self.name}, країна = {self.country}, id номер = {self.id_number}, дата народження = {self.date_of_birth}, дата дії паспорта = {self.expiry_date})"

    def get_info(self):
        return f"Ім'я: {self.name}\nКраїна: {self.country}\nНомер паспорта: {self.id_number}\nДата народження: {self.date_of_birth}\nДата закінчення дії: {self.expiry_date}"


class ForeignPassport(Passport):
    def __init__(self, name, country, id_number, date_of_birth, expiry_date, visa_info):
        super().__init__(name, country, id_number, date_of_birth, expiry_date)
        self.visa_info = visa_info

    def __repr__(self):
        return f"Закордонний паспорт (ім'я = {self.name}, країна = {self.country}, номер iD = {self.id_number}, дата народження = {self.date_of_birth}, дата дії паспорта = {self.expiry_date}, візова інформація = {self.visa_info})"

    def get_info(self):
        info = super().get_info()
        return f"{info}\nВізова інформація: {self.visa_info}"


passport1 = Passport("Іван", "Україна", "AB123456", "01.01.2000", "01.01.2025")
print(passport1)
print(passport1.get_info())
print("--------------------------------")

visa_info = {"Тип візи": "Шенген", "Дата видачі": "01.01.2024", "Дата закінчення дії": "01.01.2025"}
foreign_passport1 = ForeignPassport("Петро", "Україна", "CD789012", "02.02.2001", "02.02.2026", visa_info)
print(foreign_passport1)
print(foreign_passport1.get_info())


# Завдання 3
class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Тварина (ім'я = {self.name})"

    def get_info(self):
        return f"Ім'я: {self.name}"


class Tiger(Animal):
    def __init__(self, name, species, habitat):
        super().__init__(name)
        self.species = species
        self.habitat = habitat

    def __repr__(self):
        return f"Тигр (ім'я = {self.name}, вид = {self.species}, Середовище проживання = {self.habitat})"

    def get_info(self):
        info = super().get_info()
        return f"{info}\nВид: {self.species}\nСередовище: {self.habitat}"

    def roar(self):
        return "Rrroar!"


class Crocodile(Animal):
    def __init__(self, name, species, length):
        super().__init__(name)
        self.species = species
        self.length = length

    def __repr__(self):
        return f"Крокодил (ім'я = {self.name}, вид = {self.species}, довжина = {self.length}м.)"

    def get_info(self):
        info = super().get_info()
        return f"{info}\nВид: {self.species}\nДовжина: {self.length}м."

    def swim(self):
        return "Плаває!"


class Kangaroo(Animal):
    def __init__(self, name, species, height):
        super().__init__(name)
        self.species = species
        self.height = height

    def __repr__(self):
        return f"Кенгуру (ім'я = {self.name}, вид = {self.species}, висота = {self.height}м.)"

    def get_info(self):
        info = super().get_info()
        return f"{info}\nВид: {self.species}\nВисота: {self.height}м."

    def jump(self):
        return "Стрибає!"


tiger1 = Tiger("Sherkhan", "Bengal tiger", "India")
print(tiger1)
print(tiger1.get_info())
print(tiger1.roar())
print("--------------------------------")

crocodile1 = Crocodile("Gena", "Nile crocodile", 3)
print(crocodile1)
print(crocodile1.get_info())
print(crocodile1.swim())
print("--------------------------------")

kangaroo1 = Kangaroo("Ken", "Gray kangaroo", 1.5)
print(kangaroo1)
print(kangaroo1.get_info())
print(kangaroo1.jump())


# Завдання 4
class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


class AnalogClock(Clock):
    def __init__(self, hour, minute):
        super().__init__(hour, minute)

    def display_time(self):
        return f"{self.hour}:{self.minute}"


class DigitalClock(Clock):
    def __init__(self, hour, minute):
        super().__init__(hour, minute)

    def display_time(self):
        return f"{self.hour:02d}:{self.minute:02d}"


analog_clock1 = AnalogClock(10, 30)
print(analog_clock1.display_time())

digital_clock1 = DigitalClock(14, 45)
print(digital_clock1.display_time())
