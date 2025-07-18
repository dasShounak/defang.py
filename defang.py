#!/bin/python3
# Author: Shounak Das
# GitHub: https://github.com/dasShounak

import argparse

def Defang(mode, user_input):

    defanged_string = ""

    try:
        if mode == "url":
            replacements = { "http": "hxxp", "ftp": "fxp", "://": "[://]" }

            for old, new in replacements.items():
                user_input = user_input.replace(old, new)

            for i in user_input:
                if i == '.':
                    defanged_string += "[.]"
                else:
                    defanged_string += i

        elif mode == "email":
            user_input = user_input.replace("@", "[AT]")

            for i in user_input:
                if i == '.':
                    defanged_string += "[.]"
                else:
                    defanged_string += i

        elif mode == "ip":
            for i in user_input:
                if i == '.':
                    defanged_string += "[.]"
                else:
                    defanged_string += i
    except:
        print("Encounterd exception. Please try again. Use -h to read usage instructions.")

    print(defanged_string)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode",
                        dest = "mode",
                        help = "The type of string input. Possible options are url, email and ip.",
                        type = str,
                        required = True,
                        choices = ["url", "email", "ip"]
                        )
    parser.add_argument("input", help = "The string to be defanged.", type = str)
    args = parser.parse_args()

    Defang(args.mode, args.input)
