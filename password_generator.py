# Програма за генериране на пароли и запаметяването им във
# отделен файл заедно със името към сайта за който е генерирана

import string
import random
import time

characters = list(string.ascii_letters + string.digits)


def password_generate():
    length = int(input("Enter password length: "))
    site = input("Site for password: ")
    special_symbols = input("Special symbols Y/N: ").upper()
    specials = ["!", "@", "#", "$", "%", "&", "*"]
    if special_symbols == "Y":
        # "!@#$%^&*"
        characters.extend(specials)
        random.shuffle(characters)
    else:
        random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("Generating password...")
    time.sleep(1)
    print(f'Your password is: {"".join(password)}')
    print(f"The password is for {site}")
    print("Saving data in passwords.txt...")
    time.sleep(1)
    print("Saved!")

    with open("passwords.txt", "a") as file:
        file.write(f"Website: {site} --> ")
        generated_password = ""
        for i in password:
            generated_password += i
        file.write(f"Password: {generated_password}")
        file.write("\n")


password_generate()
