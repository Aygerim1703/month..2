
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


    def introduce(self):
        edu_status = "с высшим образованием" if self.higher_education else "без высшего образования"
        print(f"приевет меня зовут {self.name} Я родился {self.birth_date} Я работаю {self.occupation} {edu_status}")
class Classmate(Person):
    def indroduce(self):
        print(f"Привет меня зовут {self.name}, я одноклассник Игоря, я родился {self.birth_date}, я работаю {self.occupation}")
class Friends(Person):
    def introduce(self):
        print(f"привет меня зовут {self.name}, я друг игоря, я родился {self.birth_date}, я работаю {self.occupation}")


classmate1 = Classmate("Райли", '16.07.2005', "банкир", True)

classmate2 = Classmate("сабина", '16.06.2008', "сммщик", True)

friend1 = Friends("Ники", '16.09.2007', "стилист", False)

friend2 = Friends("Сьюзи", '16.10.2010', "айтишник", False)


for Person in (classmate1, classmate2, friend1, friend2):
    Person.introduce()
