import json
import time


class Contact:
    """Класс для ввода данных для нового контакта"""

    def __init__(self, last_name, first_name, middle_name, organization, work_phone, personal_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone


class PhoneBook:
    """Класс для работы с телефонным справочником"""
    contacts = []  # список контактов, которые нужно добавить в файл

    def __init__(self):
        self.load_contacts()  # вызов метода load_contacts, для предварительной выгрузки всех контактов, для дальнейшей работы с данными, а также последующей записи их в файл

    def load_contacts(self) -> None:

        """Метод сгружает все данные из файла в список contacts"""

        try:  # если это условие проходит, значит файл не пустой
            with open('PhoneBook.json', 'r', encoding='utf-8') as f:
                for i in json.load(f):
                    self.contacts.append(i)




        except:  # Если не проходит, то файл пустой
            pass

    def load_to_file(self) -> None:
        with open('PhoneBook.json', 'w', encoding='utf-8') as f:
            json.dump(self.contacts, f, ensure_ascii=False)

    def add_contact(self, data) -> None:
        """Метод для добавления нового контакта"""
        new_contact = {}

        contact_to_append = []

        for key, value in vars(data).items():  # цикл для получения ключа и значения из экземпляра класса Contact
            new_contact[key] = value  # запись в словарь new_contact новых данных

        contact_to_append.append(new_contact)  # добавление слваря new_contact в список contact_to_append

        self.contacts.append(contact_to_append)  # добавление списка contact_to_append в итоговый список данных contacts

        self.load_to_file()

        """Всё это сделано для того, чтобы данные в json файл записывались в правильном формате """

    def show_contacts(self, page=5) -> None:

        if len(self.contacts) != 0:

            for i, contact in enumerate(self.contacts, start=1):

                first_name = contact[0]['first_name']
                last_name = contact[0]['last_name']
                middle_name = contact[0]['middle_name']
                organization = contact[0]['organization']
                work_phone = contact[0]['work_phone']
                personal_phone = contact[0]['personal_phone']

                print(f'Контакт номер {i}')
                print(f'{last_name} {first_name} {middle_name}')
                print(f'Организация - {organization}')
                print(f'Рабочий телефон {work_phone}')
                print(f'Личный телефон - {personal_phone}')
                print()

                time.sleep(1)

                if i % page == 0:
                    print(input('Страница закончилась, для продолжения нажмите Enter'))

                elif i == len(self.contacts):
                    print('Контакты закончились')

        else:
            print('В справочнике не обнаружено ни одной записи')

    def search_filter(self, filter) -> None:
        """Метод для поиска по характеристикам """
        for index, i in enumerate(self.contacts):
            for key, value in i[0].items():
                if filter.lower() in value.lower():
                    print('Контакт найден')
                    print()
                    time.sleep(1)

                    first_name = self.contacts[index][0]['first_name']
                    last_name = self.contacts[index][0]['last_name']
                    middle_name = self.contacts[index][0]['middle_name']
                    organization = self.contacts[index][0]['organization']
                    work_phone = self.contacts[index][0]['work_phone']
                    personal_phone = self.contacts[index][0]['personal_phone']

                    print(f'{last_name} {first_name} {middle_name}')
                    print(f'Организация - {organization}')
                    print(f'Рабочий телефон {work_phone}')
                    print(f'Личный телефон - {personal_phone}')

    def change_contact(self, index, updated_contact) -> None:
        try:

            for key, value in vars(updated_contact).items():
                self.contacts[index - 1][0][key] = value
            self.load_to_file()
        except:
            print('Некорректный индекс ')


