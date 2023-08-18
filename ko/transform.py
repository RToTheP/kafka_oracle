from ko.model import Person, User


async def person_to_user(person: Person) -> User:
    return User(user_name=person.first_name + "." + person.last_name)