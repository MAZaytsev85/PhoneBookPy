

def read_all(data_file):
    with open(data_file, 'r', encoding="UTF-8") as phone_base:
        for line in phone_base:
            print(line.strip())

def write_new_contact(data_file):
    new_sname = input("Введите фамилию ")
    new_name = input("Введите имя ")
    new_mname = input("Введите отчество ")
    new_phone = input("Введите телефон ")
    contact = "\n" + new_sname + "," + new_name + "," + new_mname + "," + new_phone
    with open(data_file, 'a', encoding="UTF-8") as phone_base:
        phone_base.write(contact)

def find_contact(data_file):
    request_data = input("Введите данные контакта для поиска ")
    with open(data_file, 'r', encoding="UTF-8") as phone_base:
        for value in phone_base:
            if request_data.lower() in value.lower():
                print(value.strip())

def sort_contact(data_file):
    new_list = []
    with open(data_file, 'r', encoding="UTF-8") as phone_base:
        for value in phone_base:
            new_list.append(value)
        new_list.sort()
    with open(data_file, 'w', encoding="UTF-8") as phone_base:
        for value in new_list:
            phone_base.write(value)

def edit_contact(data_file):
    with open(data_file, 'r', encoding="UTF-8") as phone_base:
        data_for_edit = phone_base.read()
        new_data = data_for_edit.replace(input("Старая данные "), input("Новые данные "))
    with open(data_file, 'w', encoding="UTF-8") as phone_base:
       phone_base.write(new_data)

edit_contact("PhoneBase.txt")





