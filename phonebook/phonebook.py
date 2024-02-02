# '''
# 55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные.
# Программа должна сохранять данные в текстовом файле.
# Пользователь может ввести одну из характеристик для поиска определенной записи (нпр. имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# '''

# ДЗ:
# Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# Формат сдачи: ссылка на свой репозиторий.


import os

def input_surname():
    return input('Введите фамилию: ').title()

def input_name():
    return input('Введите имя: ').title()

def input_patronymic():
    return input('Введите отчество: ').title()

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес (город): ').title()

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}'

def data_input(file_name='phonebook.txt'):
    contact = create_contact()
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'{contact}\n\n')

def read_file(file_name='phonebook.txt'):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def print_data(file_name='phonebook.txt'):
    contacts = read_file(file_name)
    contacts_list = contacts.strip().split('\n\n')
    for contact in enumerate(contacts_list, 1):
        print(*contact)

def search_contact(file_name='phonebook.txt'):
    print(
        'Варианты поиска:\n'
        '1 - по фамилии\n'
        '2 - по имени\n'
        '3 - по отчеству\n'
        '4 - по телефону\n'
        '5 - по адресу(городу)'
    )
    var = input('Выберите необходимый вариант: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод данных!')
        var = input('Выберите необходимый вариант: ')
        print()
    i_var = int(var) - 1

    find = input('Введите данные для поиска: ').title()
    print()
    contacts = read_file(file_name)
    contacts_list = contacts.strip().split('\n\n')
    found_contacts = []
    for index, contact_str in enumerate(contacts_list, 1):
        contact_lst = contact_str.replace('\n', ' ').split()
        if find in contact_lst[i_var]:
            found_contacts.append((index, contact_str))

    if found_contacts:
        for index, contact in enumerate(found_contacts, 1):
            print(f'{index}. {contact[1]}')
        return found_contacts
    else:
        print('Контакты не найдены.\n')
        return []

def contacts_to_copy_1(contact_nums, file_name='phonebook.txt', target_file='copied_contacts.txt'):
    contacts = read_file(file_name)
    contacts_list = contacts.strip().split('\n\n')
    copied_contacts = []

    for num, _ in contact_nums:
        try:
            original_num = int(num)
            contact_str = contacts_list[original_num - 1]
            copied_contacts.append(contact_str)
        except (ValueError, IndexError):
            print(f'Некорректный номер контакта {num}. Пропускаем.\n')

    if copied_contacts:
        existing_contacts = read_file(target_file).strip().split('\n\n')

        if existing_contacts:
            last_contact = existing_contacts[-1]
            # Используем регулярное выражение для извлечения порядкового номера
            import re
            last_contact_num_match = re.match(r'^(\d+)', last_contact)
            if last_contact_num_match:
                last_contact_num = int(last_contact_num_match.group(1)) + 1
            else:
                last_contact_num = 1
        else:
            last_contact_num = 1

        new_contacts = []

        for i, contact_str in enumerate(copied_contacts, start=last_contact_num):
            # Добавляем новый контакт с порядковым номером            
            new_contact = f'{contact_str}'
            new_contacts.append(new_contact)

        with open(target_file, 'a', encoding='utf-8') as f:
            if existing_contacts:
                f.write('\n\n')
            f.write('\n\n'.join(new_contacts))
            print('Контакт(ы) скопирован(ы) успешно!\n')
    else:
        print('Контакт(ы) с такими данными уже существуют в файле.\n')

def contacts_to_copy_2(found_contacts, contact_nums, target_file='copied_contacts.txt'):
    if not found_contacts:
        print('Нет контактов для копирования.\n')
        return

    copied_contacts = []
    for num in contact_nums:
        try:
            original_num = int(num)
            contact_str = found_contacts[original_num - 1][1]
            copied_contacts.append(contact_str)
        except (ValueError, IndexError):
            print(f'Некорректный номер контакта {num}. Пропускаем.\n')

    if copied_contacts:
        existing_contacts = read_file(target_file).strip().split('\n\n')

        if existing_contacts:
            last_contact = existing_contacts[-1]
            # Используем регулярное выражение для извлечения порядкового номера
            import re
            last_contact_num_match = re.match(r'^(\d+)', last_contact)
            if last_contact_num_match:
                last_contact_num = int(last_contact_num_match.group(1)) + 1
            else:
                last_contact_num = 1
        else:
            last_contact_num = 1

        new_contacts = []

        for i, contact_str in enumerate(copied_contacts, start=last_contact_num):
            # Добавляем новый контакт с порядковым номером            
            new_contact = f'{contact_str}'
            new_contacts.append(new_contact)

        with open(target_file, 'a', encoding='utf-8') as f:
            if existing_contacts:
                f.write('\n\n')
            f.write('\n\n'.join(new_contacts))
            print('Контакт(ы) скопирован(ы) успешно!\n')
    else:
        print('Контакт(ы) с такими данными уже существуют в файле.\n')

def search_contact_with_numbers(file_name='phonebook.txt'):
    print(
        'Варианты поиска:\n'
        '1 - по фамилии\n'
        '2 - по имени\n'
        '3 - по отчеству\n'
        '4 - по телефону\n'
        '5 - по адресу(городу)'
    )
    var = input('Выберите необходимый вариант: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод данных!')
        var = input('Выберите необходимый вариант: ')
        print()
    i_var = int(var) - 1

    find = input('Введите данные для поиска: ').title()
    print()
    contacts = read_file(file_name)
    contacts_list = contacts.strip().split('\n\n')
    found_contacts = []

    for index, contact_str in enumerate(contacts_list, 1):
        contact_lst = contact_str.replace('\n', ' ').split()
        if find in contact_lst[i_var]:
            found_contacts.append((index, contact_str))

    if found_contacts:
        for index, contact in enumerate(found_contacts, 1):
            print(f'{index}. {contact[1]}')
        return found_contacts
    else:
        print('Контакты не найдены.\n')
        return []    

def copy_all_contacts(file_name='phonebook.txt', target_file='copied_contacts.txt'):
    existing_contacts = read_file(target_file).strip().split('\n\n') if os.path.exists(target_file) else []

    contacts = read_file(file_name)
    contacts_list = contacts.strip().split('\n\n')

    new_contacts = [contact for contact in contacts_list if contact not in existing_contacts]

    if new_contacts:
        with open(target_file, 'a', encoding='utf-8') as f:
            if existing_contacts:
                f.write('\n\n')
            f.write('\n\n'.join(new_contacts))
            existing_contacts.extend(new_contacts)
        print(f'Новые контакты из {file_name} успешно добавлены в {target_file}!\n')
    else:
        print(f'Все контакты из {file_name} уже существуют в {target_file}.\n')

def copy_contact():
    print(
        'Выберите откуда хотите скопировать контакт(ы):\n'
        '1 - из полного списка контактов \n'
        '2 - найти определенный контакт \n'
        '3 - скопировать все контакты\n'
        '4 - выход'
    )
    action = input('Выберите номер действия: ')
    print()
    while action not in ('1', '2', '3', '4'):
        print('Некорректный ввод данных!')
        print()
        action = input('Выберите номер действия: ')        
        print()
    if action == '1':
        available_files = get_available_files()
        file_name = input_file_name(available_files, 'Введите номер файла для показа данных: ')
        print_data(file_name)

        nums_to_copy = input('Введите номер(а) контактов через запятую для копирования: ')
        contacts_list = [num.strip() for num in nums_to_copy.split(',')]
        contacts_to_copy_1([(num, '') for num in contacts_list], file_name=file_name)

    elif action == '2':
        available_files = get_available_files()
        file_name = input_file_name(available_files, 'Введите номер файла для поиска контакта: ')
        found_contacts = search_contact_with_numbers(file_name)

        if found_contacts:
            nums_to_copy = input('Введите номер(а) контактов через запятую для копирования: ')
            contact_nums = [int(num.strip()) for num in nums_to_copy.split(',')]
            contacts_to_copy_2(found_contacts, contact_nums, target_file='copied_contacts.txt')

    elif action == '3':
        available_files = get_available_files()
        file_name = input_file_name(available_files, 'Введите номер файла для копирования всех контактов: ')
        copy_all_contacts()

    elif action == '4':
        print('Всего доброго!')

def contacts_to_delete_1(contact_nums, file_name='phonebook.txt'):
    contacts = read_file(file_name)
    contacts_list = contacts.strip().split('\n\n')

    contacts_to_remove = []
    for num, _ in contact_nums:
        try:
            original_num = int(num)
            contact_to_remove = contacts_list[original_num - 1]
            contacts_to_remove.append(contact_to_remove)
        except (ValueError, IndexError):
            print(f'Некорректный номер контакта {num}.\n')

    for contact_to_remove in contacts_to_remove:
        contacts_list.remove(contact_to_remove)

    with open(file_name, 'a' if os.path.exists(file_name) and os.stat(file_name).st_size > 0 else 'w', encoding='utf-8') as f:
        if os.path.exists(file_name) and os.stat(file_name).st_size > 0:
            f.write('\n\n')
        f.write('\n\n'.join(contacts_list))

    print('Контакт(ы) удален(ы) успешно!\n')

def contacts_to_delete_2(found_contacts, contact_nums, target_file):
    if not found_contacts:
        print('Нет контактов для удаления.\n')
        return

    choised_contacts = []
    for num in contact_nums:
        try:
            original_num = int(num)
            contact_str = found_contacts[original_num - 1][1]
            choised_contacts.append(contact_str)
        except (ValueError, IndexError):
            print(f'Некорректный номер контакта {num}.\n')

    if choised_contacts:
        existing_contacts = read_file(target_file).strip().split('\n\n')

        contacts_to_remove = []

        for contact_str in choised_contacts:
            if contact_str in existing_contacts:
                contacts_to_remove.append(contact_str)

        remaining_contacts = [contact for contact in existing_contacts if contact not in contacts_to_remove]

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(remaining_contacts))
            print('Контакт(ы) удален(ы) успешно!\n')
    else:
        print('Контакт(ы) с такими данными не найдены в файле.\n')

def delete_contact():
    print(
        'Выберите откуда хотите удалить контакт(ы):\n'
        '1 - из полного списка контактов \n'
        '2 - найти определенный контакт \n'
        '3 - удалить все контакты \n'
        '4 - выход'
    )
    action = input('Выберите номер действия: ')
    print()
    while action not in ('1', '2', '3', '4'):
        print('Некорректный ввод данных!')
        action = input('Выберите номер действия: ')
        print()

    if action == '1':
        available_files = get_available_files()
        file_name = input_file_name(available_files, 'Введите номер файла для показа данных: ')
        print_data(file_name)

        nums_to_delete = input('Введите номер(а) контактов через запятую для удаления: ')
        contacts_list = [num.strip() for num in nums_to_delete.split(',')]
        contacts_to_delete_1([(num, '') for num in contacts_list], file_name=file_name)

    elif action == '2':
        available_files = get_available_files()
        file_name = input_file_name(available_files, 'Введите номер файла для поиска контакта: ')
        found_contacts = search_contact(file_name)

        if found_contacts:
            nums_to_delete = input('Введите номер(а) контактов через запятую для удаления: ')
            contact_nums = [int(num.strip()) for num in nums_to_delete.split(',')]
            contacts_to_delete_2(found_contacts, contact_nums, file_name)

    elif action == '3':
        available_files = get_available_files()
        file_name = input_file_name(available_files, 'Введите номер файла для удаления всех контактов: ')
        
        confirmation = input('Вы уверены, что хотите удалить все контакты? (да/нет): ')
        if confirmation.lower() == 'да':
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write('')
            print('Все контакты успешно удалены!\n')
        else:
            print('Операция отменена.\n')

    elif action == '4':
        print('Всего доброго!')

def get_available_files():
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.txt')]
    return files

def input_file_name(available_files, prompt='Введите номер файла: '):
    print('Доступные файлы:')
    for index, file_name in enumerate(available_files, 1):
        print(f'{index}. {file_name}')
    while True:
        try:
            file_index = int(input(prompt))
            if 1 <= file_index <= len(available_files):
                return available_files[file_index - 1]
            print('Некорректный номер файла. Попробуйте еще раз.')
        except ValueError:
            print('Некорректный ввод. Введите число.')

def interface():
    choice = ''
    while choice != '6':
        print(
            'Варианты действия:\n'
            '1 - ввод данных контакта \n'
            '2 - вывести данные на экран \n'
            '3 - поиск контакта \n'
            '4 - скопировать контакт(ы)\n'
            '5 - удалить контакт(ы)\n'
            '6 - выход'
        )
        print()
        choice = input('Выберите номер действия: ')
        print()
        while choice not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод данных!')
            choice = input('Выберите номер действия: ')
            print()
        match choice:
            case '1':
                data_input()
            case '2':
                available_files = get_available_files()
                file_name = input_file_name(available_files, 'Введите номер файла для показа данных: ')
                print_data(file_name)
            case '3':
                available_files = get_available_files()
                file_name = input_file_name(available_files, 'Введите номер файла для поиска контакта: ')
                search_contact(file_name)
            case '4':
                copy_contact()
            case '5':
                delete_contact()
            case '6':
                print('Всего доброго!')

if __name__ == '__main__':
    interface()






