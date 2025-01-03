def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age

print(get_name_with_age("Bipin", str(34)))

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

print(get_name_with_age("Bipin", 34))