# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
   SATHANIC  INSTA                                  /$$                        
                                                    | $$                        
  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
 /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$  \__/| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \__/  | $$    | $$$$$$$$| $$  \__/
| $$      | $$_____/| $$  | $$| $$  | $$| $$        | $$ /$$| $$_____/| $$      
| $$      |  $$$$$$$| $$$$$$$/|  $$$$$$/| $$        |  $$$$/|  $$$$$$$| $$      
|__/       \_______/| $$____/  \______/ |__/         \___/   \_______/|__/      
                    | $$                                                        
                    | $$                                                        
                    |__/ """

urls = [
    "GitHub - https://github.com/sathaniccc/SATHANIC-INSTA-REPORTER",
    "WhatsApp - +919778158839
    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Producer: Muneeb"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> Follow me On Instagram @muneebwanee.")
    print ("\n", "-> Special For Hackers:\n    " + choice(urls))
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
