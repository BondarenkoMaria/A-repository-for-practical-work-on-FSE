import string
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
symbols = '*#-'
password = input("Enter password: ")
has_errors = False
if len(password) != 8:
    print("Длина пароля не равна 8!")
    has_errors = True
if (password.lower() == password):
    print("В пароле отсутствуют заглавные буквы!")
    has_errors = True
if (password.upper() == password):
    print("В пароле отсутствуют строчные буквы!")
    has_errors = True
if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры!")
    has_errors = True
if not any(symbol in symbols for symbol in password):
    print("В пароле отсутствуют специальные символы!")
    has_errors = True
if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы!")
    has_errors = True 
if not has_errors:
    print("Надёжный пароль!")