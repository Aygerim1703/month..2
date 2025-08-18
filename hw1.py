class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


person1 = Person("Айгерим", "12.04.2003", "Учитель рисования", True)
person2 = Person("Марсель", "03.09.2000", "Программист", True)
person3 = Person("Айдай", "25.11.2002", "Дизайнер", False)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)