# Програма за генериране на пароли и запаметяването им във
# отделен файл заедно със името към сайта за който е генерирана

import string
import random
import time


def special_symbol(symbol):
    if symbol == "Y":
        # "!@#$%^&*"
        characters.extend(specials)
        random.shuffle(characters)
    else:
        random.shuffle(characters)


def generated_password(len, chars, pwd):
    for i in range(len):
        pwd.append(random.choice(chars))
    random.shuffle(pwd)


def user_message(pwd, site):
    print("Generating password...")
    time.sleep(1)
    print(f'Your password is: {"".join(pwd)}')
    print(f"The password is for {site}")
    print("Saving data in passwords.txt...")
    time.sleep(1)
    print("Saved!")


def write_to_file(pwd, site):
    with open("passwords.txt", "a") as file:
        file.write(f"Website: {site} --> ")
        generated_password = ""
        for i in pwd:
            generated_password += i
        file.write(f"Password: {generated_password}")
        file.write("\n")


characters = list(string.ascii_letters + string.digits)

length = int(input("Enter password length: "))
site = input("Site for password: ")
special_symbols = input("Special symbols Y/N: ").upper()
specials = ["!", "@", "#", "$", "%", "&", "*"]
password = []

special_symbol(special_symbols)
generated_password(length, characters, password)
user_message(password, site)
write_to_file(password, site)
