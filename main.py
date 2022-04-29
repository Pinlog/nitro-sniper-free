import requests
import random
import string
import time
import keyboard
import os
import colorama
f = open("Valid Nitro.txt", "w", encoding='utf-8')
import webbrowser
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN)
print(" █████ █████  ████ █   █ █████     ████ █████ █   █ █████ ")
print("  █   █     █     █   █ █        █     █     ██  █ █      ")
print("  █   ████  █     █████ █████    █  ██ ████  █ █ █ █████  ")
print("  █   █     █     █   █     █    █   █ █     █  ██     █  ")
print("  █   █████  ████ █   █ █████     ███  █████ █   █ █████  ")
print("")

print("")
print("Press ` to start")
while True:
    if keyboard.is_pressed("`"):
        while True:
            code = ('').join(random.choices(string.ascii_letters + string.digits,
                                            k=16))
            r = requests.get(
                f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
            )   
            if r.status_code == 200:
                print(Fore.BLUE)
                print(f"[+] Valid | discord.gift/{code}")
                f.write(f"discord.gift/{code}\n")
                webbrowser.open("https://discord.gg/WdaZy28xkB")
            else:
                print(Fore.RED)
                print(f"[-] Invalid | https://discord.gift/{code}")
