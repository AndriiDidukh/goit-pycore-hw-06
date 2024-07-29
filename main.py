from collections import UserDict


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        if len(str(value)) == 10:
            super().__init__(value)
        else:
            raise Exception("Wrong phone format")


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        for i in self.phones[:]:
            if i.value == phone:
                self.phones.remove(i)

    def edit_phone(self, phone_to_edit: str, new_phone: str):
        for i in self.phones[:]:
            if i.value == phone_to_edit:
                self.phones.remove(i)

        self.phones.append(Phone(new_phone))

    def find_phone(self, phone: str):
        for i in self.phones:
            if i.value == phone:
                return i

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def find(self, name: str):
        for k, v in self.data.items():
            if k == name:
                return v

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    def delete(self, name: str):
        del self.data[name]


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_phone("6666666666")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
john.remove_phone("6666666666")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("John")
print(book.find("John"))
