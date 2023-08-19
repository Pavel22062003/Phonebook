from utils import PhoneBook, Contact

if __name__ == "__main__":
    phone_book = PhoneBook()

    while True:
        print("\nМеню:")
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Поиск записей")
        print("4. Редактировать запись")
        print("5. Выход")

        user_input = input("Выберите действие: ")

        if user_input == "1":
            phone_book.show_contacts()

        elif user_input == "2":
            last_name = input("Фамилия: ")
            first_name = input("Имя: ")
            middle_name = input("Отчество: ")
            organization = input("Организация: ")
            work_phone = input("Рабочий телефон: ")
            personal_phone = input("Личный телефон: ")

            new_contact = Contact(last_name, first_name, middle_name, organization, work_phone, personal_phone)
            phone_book.add_contact(new_contact)
            print("Запись добавлена.")
        elif user_input == "3":

            sign = input('Введите любое слово или телефон, по которому можно найти контакт')
            phone_book.search_filter(sign)


        elif user_input == "4":

            index = int(input("Введите номер контакта для редактирования: "))
            last_name = input("Фамилия: ")
            first_name = input("Имя: ")
            middle_name = input("Отчество: ")
            organization = input("Организация: ")
            work_phone = input("Рабочий телефон: ")
            personal_phone = input("Личный телефон: ")

            updated_contact = Contact(last_name, first_name, middle_name, organization, work_phone, personal_phone)
            phone_book.change_contact(index, updated_contact)
        elif user_input == "5":
            break
        else:
            print("Такой опции нет")
