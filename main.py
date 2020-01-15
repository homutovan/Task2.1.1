documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }

messages = ['\nДобро пожаловать в систему электронного документооборота ООО "Рога и Копыта"\n', 'Чтобы посмотреть перечень зарегистрированных документов, нажмите [l]', 'Чтобы посмотреть документы, хранящиеся на полках, введите [sp]', 'Чтобы вывести информацию о документе, введите [p]', 'Чтобы найти документ на полке, введите [s]', 'Чтобы добавить новый документ, введите [a]', 'Чтобы удалить документ, введите [d]', 'Чтобы переместить документ, введите [m]', 'Чтобы добавить новую полку, введите [as]', 'Для выхода из системы введите [q]']

def request_number():
  doc_number = input('Введите номер документа: ')
  return doc_number

def request_shelf():
  while True:
    shelf_number = input('Введите номер полки: ')
    if is_int(shelf_number) == True:
      break
    else:
      print('Номер полки должен быть целым числом')
  return shelf_number

def is_int(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

def find_doc(doc_number, print_stat = True):
  for doc in documents:
    if doc['number'] == doc_number:
      break
    else:
      doc = None
  if doc == None and print_stat == True:
    print(f'Документ № {doc_number} не найден в учетной системе')
  return doc

def find_shelf(doc_number):
  for shelf in directories.items():
    if doc_number in shelf[1]:
      break
  else:
    print(f'Документ № {doc_number} не найден в учетной системе')
    shelf = None
  return shelf

def print_shelf(doc_number = None):
  while doc_number == None:
    doc_number = request_number()
    if find_shelf(doc_number) == None:
      doc_number = None
  shelf = find_shelf(doc_number)
  if shelf != None:
    print(f'Документ № {doc_number} находится на полке № {shelf[0]} позиция {shelf[1].index(doc_number)}')
  return None

def print_people(doc_number = None):
  if doc_number == None:
    doc_number = request_number()
  doc = find_doc(doc_number)
  if doc != None:
    print(f'Документ № {doc_number} принадлежит пользователю {doc["name"]}')
  return None

def print_list():
  print('Перечень зарегистрированных документов\n')
  for doc in documents:
    print(' '.join([i for i in doc.values()]))
  return None

def add_docs(): 

  doc = dict.fromkeys(documents[0].keys())
  
  while True:
    for key in doc.keys():
      doc[key] = input(f'Введите аттрибут документа {key}:')
      print(doc['name'])

      #print('Мудаки вы')
    if find_doc(doc['number'], False) != None:
      print(f'Документ с указанным номером уже храниться в системе:')
    else:
      break

  documents.append(doc)
  add_doc_shelf(doc)
  return None
  
def add_doc_shelf(doc):
  while True:
    shelf_number = request_shelf()
    if shelf_number not in directories.keys():
      print(f'Полка № {shelf_number} отсутствует, хотите создать новую полку № {shelf_number}?')
      if input('y/n?:') == 'y':
        add_shelf()
    else:
      break 
  directories[shelf_number].append(doc['number'])
  print(f'Документ № {doc["number"]} добавлен spна полку {shelf_number} позиция {directories[shelf_number].index(doc["number"])}')
  return None

def del_doc_shelf(doc_number):
  #Дописать модуль подтверждения удаления
  shelf = find_shelf(doc_number)
  print(f'Документ № {doc_number} удален c полки {shelf[0]} позиция {shelf[1].index(doc_number)}')
  directories[shelf[0]].remove(doc_number)
  return None

def del_doc(doc_number = None):
  while doc_number == None:
    doc_number = request_number()
    if find_doc(doc_number) == None:
      doc_number = None
  documents.remove(find_doc(doc_number))
  del_doc_shelf(doc_number)
  return None

def move_doc_shelf(doc_number = None):
  while doc_number == None:
    doc_number = request_number()
    if find_doc(doc_number) == None:
      doc_number = None
  del_doc_shelf(doc_number)
  add_doc_shelf(find_doc(doc_number))
  
  return None

def add_shelf():
  while True:
    shelf_number = request_shelf()
    if shelf_number in directories.keys():
      print('Указанная полка уже существует')
    else:
      directories[shelf_number] = []
      print(f'Полка № {shelf_number} добавлена')
      break
  return None

def print_dir():
  print('Документы, хранящиеся на полках')
  for key in directories:
    print(key, directories[key])
  return None

def main_menu():
  while True:
    print("\n".join([msg for msg in messages]))
    command = input('\nВведите команду:')
    if command not in commands.keys():
      print('Незарегистрированная команда, повторите ввод')
      continue
    if command == 'q':
      break
    else:
      commands[command]()
  return None

commands = {'l': print_list, 'sp': print_dir, 'p': print_people, 's': print_shelf, 'a': add_docs, 'd': del_doc, 'm': move_doc_shelf, 'as': add_shelf, 'q': None}


def main():
  main_menu()
  return None

main()
