
class Contact:
    def __init__(self, name, surname, phone_number, elect='нет', **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.add_info = kwargs
        self.elect = elect
        self.contact = {'Имя': self.name,
                        'Фамилия': self.surname,
                        'Телефон': self.phone_number,
                        'В избранных': self.elect,
                        'Дополнительная информация':
                            self.add_info
                        }

    def return_inf(self):
        print(f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}\n' \
        f'Телефон: {self.phone_number}\n' \
        f'В избранных: {self.elect}')
        print('Дополнительная информация:')
        for key, value in self.add_info.items():
            print('{0:>5}{1}: {2}'.format(' ',key,value))

    def __str__(self):
        self.return_inf()
        return str()


class PhoneBook:
    def __init__(self, phonebook_name):
        self.name = phonebook_name
        self.contacts = []

    def print_contact(self, contacts):
        for key, value in contacts.items():
            if isinstance(value, dict):
                print(f'{key}:')
                for keys, values in value.items():
                    print('{0:>5}{1}: {2}'.format(' ', keys, values))
            else:
                print('{}: {}'.format(key, value))

    def show_contacts(self):
        print('Список контактов:')
        for i,contacts in enumerate(self.contacts, 1):
            print('*'*25)
            print(f'Контакт №{i}')
            self.print_contact(contacts)


    def add_contact(self, name, surname, phone_number, *args, **kwargs):
        self.contacts.append(Contact(name, surname, phone_number, *args, **kwargs).contact)

    def del_contact_on_number(self, phone_number):
        for contact in self.contacts:
            if contact['Телефон'] == phone_number:
                self.contacts.remove(contact)
            if phone_number not in contact.values():
                print(f'Контакт с номером {phone_number} не найден.')

    def find_elect_numbers(self):
        for contact in self.contacts:
            if contact['В избранных'] == 'да':
                self.print_contact(contact)
            if 'да' not in contact['В избранных']:
                print(f'Избранные контакты отсутсвуют.')

    def find_on_name_surname(self, name, surname):
        full_name_f = name + ' ' + surname
        for contact in self.contacts:
            full_name = contact['Имя'] + ' ' + contact['Фамилия']
            if full_name == full_name_f:
                self.print_contact(contact)
            else:
                print(f'Контак {name} {surname} не найден.')

def main():
    name_phone_book = input('Введите название телефонной книги\n')
    phone_book = PhoneBook(name_phone_book)
    while True:
        action = input('Введите команду:\n' \
                 'a - добавить контакт в книгу\n' \
                 's - показать список конатктов\n' \
                 'd - удалить контакт по номеру телефона\n'
                 'f - найти избранные контакты\n'
                 'fns - найти контакт по имени и фамилии\n'
                 'q - выйти из программы\n')
        if action == 'a':
            while True:
                try:
                    name, surname = input('Введите имя и фамилию контакта через пробел:\n').split()
                except ValueError:
                    print('Введите данные корректно')
                else:
                    break
            phone_number = input('Введите номер телефона:\n')
            elect = input('Является ли контакт избранным? Введите да или нет\n').lower()
            add_info_dict = {}
            while True:
                try:
                    add_info = input('Введите дополнительную информацию: название соц сети и логин через пробел\n'
                                     'Для выхода нажмите q\n').split()
                    if add_info == ['q']:
                        break
                    else:
                        add_info_dict.update(dict([add_info]))
                except ValueError:
                    print('Введите корректно дополнительную информацию')
            cont = Contact(name, surname, phone_number, elect, **add_info_dict)
            print('Демонстрация работы print задания №1:')
            print(cont)
            phone_book.add_contact(name, surname, phone_number, elect, **add_info_dict)
        if action == 's':
            phone_book.show_contacts()
        if action == 'd':
            phone_number = input('Введите номер телефона, по которому нужно удалить контакт\n')
            phone_book.del_contact_on_number(phone_number)
        if action == 'f':
            phone_book.find_elect_numbers()
        if action == 'fns':
            while True:
                try:
                    name, surname = input('Введите имя и фамилию искомого контакта через пробел\n').split()
                except ValueError:
                    print('Введите данные корректно')
                else:
                    break
            phone_book.find_on_name_surname(name, surname)
        if action == 'q':
            break

main()
