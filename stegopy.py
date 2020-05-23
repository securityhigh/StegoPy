#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
StegoPy Offical
github.com/eBind/StegoPy
"""

import sys
import os

from PIL import Image, ImageDraw
from cryptography.fernet import Fernet
from colorama import Fore, Style

DATA = dict()


def main():
    """
    Main method
    :return:
    """
    try:
        DATA["action"] = sys.argv[1]
        DATA["image"] = sys.argv[2]

        if DATA["action"] == '-e':
            DATA["data"] = sys.argv[3]

            if not os.path.exists(DATA["data"]):
                raise FileExistsError

        if not os.path.exists(DATA["image"]):
            raise FileExistsError

    except IndexError:
        print(Style.BRIGHT + Fore.WHITE + '     Encrypt: stegopy.py -e path_to_image path_to_data')
        print("     Decrypt: stegopy.py -d path_to_image")
        sys.exit()

    except FileExistsError:
        print(Style.BRIGHT + Fore.YELLOW + '     Image not found.')
        sys.exit()

    print(Style.RESET_ALL + Fore.CYAN)
    print("    ███████╗████████╗███████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗")
    print("    ██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██╔══██╗╚██╗ ██╔╝")
    print("    ███████╗   ██║   █████╗  ██║  ███╗██║   ██║██████╔╝ ╚████╔╝ ")
    print("    ╚════██║   ██║   ██╔══╝  ██║   ██║██║   ██║██╔═══╝   ╚██╔╝  ")
    print("    ███████║   ██║   ███████╗╚██████╔╝╚██████╔╝██║        ██║   ")
    print("    ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝        ╚═╝   ")
    print("")

    if DATA["action"] == '-e':
        balance = int(input(Style.BRIGHT + Fore.RED + "     Balance (1 to 4) > "))
        if balance < 1 or balance > 4:
            balance = 2

        file = open(DATA["data"], 'r')
        text = file.read()
        file.close()

        encrypt(DATA["image"], text.strip(), Fernet.generate_key().decode(), balance)

    elif DATA["action"] == '-d':
        key = input(Style.BRIGHT + Fore.RED + "     Key: ")

        try:
            decrypt(DATA["image"], key)

        except IndexError:
            print(Style.BRIGHT + Fore.YELLOW + "     Invalid key")

        except ValueError:
            print(Style.BRIGHT + Fore.YELLOW + "     Invalid key")

    print('')


def encrypt(path_to_image, text, key, balance):
    """
    Encrypt in image
    :param balance: 1 to 4
    :param path_to_image: path
    :param text: text from data file
    :param key: generated key
    :return:
    """
    img = dict()
    size = dict()
    coord = dict()

    img["image"] = Image.open(path_to_image)
    img["draw"] = ImageDraw.Draw(img["image"])
    img["pix"] = img["image"].load()

    size["width"] = img["image"].size[0]
    size["height"] = img["image"].size[1]

    text = des_encrypt(text, key)
    binary_text = text_to_binary(text)
    list_two = split_count(''.join(binary_text), balance)

    coord["x"] = 0
    coord["y"] = 0
    count = 0

    for i in list_two:
        blue = last_replace(bin(img["pix"][coord["x"], coord["y"]][2]), i)

        img["draw"].point((coord["x"], coord["y"]),
                          (img["pix"][coord["x"], coord["y"]][0],
                           img["pix"][coord["x"], coord["y"]][1],
                           int(blue, 2)))

        if coord["x"] < (size["width"] - 1):
            coord["x"] += 1
        elif coord["y"] < (size["height"] - 1):
            coord["y"] += 1
            coord["x"] = 0
        else:
            print(Style.BRIGHT + Fore.YELLOW + "     Message too long for this image")
            sys.exit()

        count += 1

    img["image"].save("out.png", "PNG")
    print(Style.BRIGHT + Fore.GREEN + "     Image saved in out.png")

    file = open("key.dat", "w")
    file.write(str(balance) + '$' + str(count) + '$' + key)
    file.close()
    print(Style.BRIGHT + Fore.GREEN + "     Key saved in key.dat")


def decrypt(path_to_image, key):
    """

    :param path_to_image:
    :param key:
    :return:
    """
    balance = int(key.split('$')[0])
    count = int(key.split('$')[1])
    end_key = key.split('$')[2]

    img = dict()
    coord = dict()

    img["image"] = Image.open(path_to_image)
    img["width"] = img["image"].size[0]
    img["height"] = img["image"].size[1]
    img["pix"] = img["image"].load()

    coord["x"] = 0
    coord["y"] = 0
    code = ''

    i = 0
    while i < count:
        pixel = str(bin(img["pix"][coord["x"], coord["y"]][2]))

        if balance == 4:
            code += pixel[-4] + pixel[-3] + pixel[-2] + pixel[-1]

        elif balance == 3:
            code += pixel[-3] + pixel[-2] + pixel[-1]

        elif balance == 2:
            code += pixel[-2] + pixel[-1]

        else:
            code += pixel[-1]

        if coord["x"] < (img["width"] - 1):
            coord["x"] += 1
        else:
            coord["y"] += 1
            coord["x"] = 0

        i += 1

    outed = binary_to_text(split_count(code, 8))

    file = open("out.txt", "w")
    file.write(des_decrypt(''.join(outed), end_key))
    file.close()
    print(Style.BRIGHT + Fore.GREEN + "     Data saved in out.txt")


def des_encrypt(text, key):
    """
    DES Encrypting
    :param text:
    :param key:
    :return: encrypt data
    """
    cipher = Fernet(key.encode())
    result = cipher.encrypt(text.encode())

    return result.decode()


def des_decrypt(text, key):
    """
    DES Decrypting
    :param text:
    :param key:
    :return:
    """
    cipher = Fernet(key.encode())
    result = cipher.decrypt(text.encode())

    return result.decode()


def split_count(text, count):
    """
    Splitting every count
    :param text:
    :param count:
    :return:
    """
    result = list()
    txt = ''
    var = 0

    for i in text:
        if var == count:
            result.append(txt)
            txt = ''
            var = 0

        txt += i
        var += 1

    result.append(txt)

    return result


def last_replace(main_string, last_symbols):
    """

    :param main_string: пиздец
    :param last_symbols: бля
    :return: пизбля
    """
    return main_string[:-len(last_symbols)] + last_symbols


def text_to_binary(event):
    """
    Text convert to binary code
    :param event: text
    :return: binary code(str)
    """
    return ['0' * (8 - len(format(ord(elem), 'b'))) + format(ord(elem), 'b') for elem in event]


def binary_to_text(event):
    """
    Binary code convert to text
    :param event: binary code(str)
    :return: text
    """
    return [chr(int(str(elem), 2)) for elem in event]


if __name__ == "__main__":
    main()
