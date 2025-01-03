class Person:
    def __init__(self, name: str):
        self.name = name

one_person = Person("Bipin")


def get_person_name(one_person: Person):
    return one_person.name      

print(get_person_name(one_person))