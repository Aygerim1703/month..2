
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    @property
    def occupation(self):
        return self.__occupation
    @occupation.setter
    def occupation(self ,value):
        self.__occupation = value

    @property
    def higher_education(self):
        return self.__higher_education

    @higher_education.setter
    def higher_education(self, value):
        self.__higher_education = value

    def introduce(self):
        edu_status = "с высшим образованием" if self.higher_education else "без высшего образования"
        print(f"приевет меня зовут {self.name} Я родился {self.birth_date} Я работаю {self.occupation} {edu_status}")
class Classmate(Person):
    def indroduce(self):
        edu_status = "с высшим образованием" if self.higher_education else "без высшего образования"
        print(f"Привет меня зовут {self.name}, я одноклассник Игоря, я родился {self.birth_date},"
              f" я работаю {self.occupation}, я учился с Игорем в одной группе. {edu_status}")
class Friends(Person):
    def introduce(self):
        edu_status = "с высшим образованием" if self.higher_education else "без высшего образования"
        print(f"привет меня зовут {self.name}, я друг игоря, я родился {self.birth_date},"
              f" я работаю {self.occupation}, {edu_status} ")


classmate1 = Classmate("Райли", '16.07.2005', "банкир", True)

classmate2 = Classmate("сабина", '16.06.2008', "сммщик", True)

friend1 = Friends("Ники", '16.09.2007', "стилист", False)

friend2 = Friends("Сьюзи", '16.10.2010', "айтишник", False)


for Person in (classmate1, classmate2, friend1, friend2):
    Person.introduce()
