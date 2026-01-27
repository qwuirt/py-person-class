class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_data_list = []
    for person in people:
        Person(person.get("name"), person.get("age"))
    for person in people:
        if person.get("wife") is not None:
            setattr(
                Person.people[person.get("name")],
                "wife",
                Person.people[person.get("wife")]
            )
        elif person.get("husband") is not None:
            setattr(
                Person.people[person.get("name")],
                "husband",
                Person.people[person.get("husband")]
            )
        person_data_list.append(Person.people[person.get("name")])

    return person_data_list
