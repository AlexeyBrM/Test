from uuid import uuid4
from datetime import datetime 
import json



# TODO: убрать database, в функцию передавать название файла базы данных
def add_user(name: str, phone_number, json_object):

  with open(f"{json_object}", "r") as file:
    json_object = json.load(file)

  id = str(uuid4())
  date_of_creation = datetime.timestamp(datetime.now())
  a = str(phone_number)
  try:
    name not in json_object['id']['name']
  except:
    print(" Таке імя вже існує")
  else:    
    if len(a) != 10:
      
      print('Маленький номер. Введіть ще раз')
    else:
      json_object[id] = {
      "name": name,
      "phone_number": phone_number,
      "date_of_creation": date_of_creation
      }
      
      # TODO: добавить проверку на налачие файла с указанным именем через try
      json_object = json.dumps(json_object, indent=4)
      print( f'Запись {id} успешно создана!')
      with open("base.json", "w") as outfile:
        outfile.write(json_object)
        print(json_object)
  

  return json_object


add_user(name="Vasiiliy", phone_number=1234567891, json_object="base.json")
# print(database)




# TODO: добавить 2 новые функции для чтения базы данных: 

def show_user(id, json_object):
  # Выводит конкретного пользователя по его id
  with open(f"{'base.json'}", "r") as file:
    json_object = json.load(file)
  
  try:
     id in json_object
  except:
     print('No user found with id specified')
  else:
    print(json_object[id])
  return json_object


# show_user('300cc148-de5f-49e1-9dc4-347f6d72274e', json_object='base.json')


# "3d537369-52d6-4f11-8cd4-65f22526ac05": {
#         "name": "David",
#         "surname": "Jones",
#         "phone_number": "9992104390",
#         "date_of_creation": 1689954079.582785
#     }

# No user found with id specified

def list_users(json_object):
    # Выводит всю базу данных
  with open(f"{'base.json'}", "r") as file:
    json_object = json.load(file)
    print(json_object)
    return

# list_users(json_object="base.json")