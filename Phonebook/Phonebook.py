phone_book = {}
password1 = ""
pwd1 = "password.txt"
def over_write():
  file = open ("password.txt", "w")
  file.close
  while True:
    quiz = input("to set new password type yes or none for no password: ").lower()
    if quiz == "yes":
      set_lock(1)
      break
    elif quiz == "none":
      menu()
      break
    else:
      print("invalid option")
  
def set_lock(value=0):
  with open ("password.txt", "r") as f:
    file = f.readlines()
    if value == 1:
      pwd4 = input("Enter new password")
      s2 = "Password reset successfully"
      store_lock(pwd4, s2)
    elif len(file) == 0:
      pin = input("Enter the pin to set lock: ")
      s2 = "Password set successfuly"
      store_lock(pin, s2)
      
    else:
      print("already have a password")
      pass2 = input("To reset password type yes: ").lower()
      if pass2 == "yes":
        over_write()
      else:
        menu()
    f.close
    

def user_unlock():
  with open ("password.txt", "r") as file:
    f = file.read().strip()
    if len(f) == 0:
      print("No password found set using setlock")
      menu()
    else:
      while True:
        pwd = input("Enter password To unlock: ")
        if pwd == f:
          print("successfully unlocked")
          break
        else:
          print("wrong password try again")
    file.close()
    menu()
def add_contact():
  global phone_book
  while True:
    option = input("To add contact type yes/menu: ")
    if option == "menu":
      menu()
      break
    elif option == "yes":
      key = input("Enter the contact name: ")
      if key in phone_book:
        print(f"contact {key} is already available")
      num = input("Enter the contact number: ")
      phone_book[key] = num
      print("contact added successfully")
def phonebook():
  global phone_book
  while True:
    search_cont = input("To search enter contact name or type menu: ")
    if search_cont == "menu":
      menu()
      break
    elif search_cont in phone_book:
      print(phone_book[search_cont])
    else:
      print(f"No contact name {search_cont}")
      
def store_lock(passwd, msg):
  with open ("password.txt", "a") as f:
    f.write(passwd)
    print(msg)
    f.close
    menu()


def menu():
  while True:
    user_input = input("Enter the following options (exit/search/addcontact/setlock/lock): ").lower()
    if user_input == "exit":
      break
    elif user_input == "setlock":
      set_lock()
      break
    elif user_input == "lock":
      user_unlock()
      break
    elif user_input == "addcontact":
      add_contact()
      break
    elif user_input == "search":
      phonebook()
      break
    else:
      print("invalid option ")
menu()