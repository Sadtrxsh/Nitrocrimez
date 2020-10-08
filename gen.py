import random
import string
import time
import sys
from colorama import Fore, Style, init
init()
f = open('nitro_codes.txt', 'a')
print(Fore.RED + Style.BRIGHT, """ 
░██████╗░█████╗░██████╗░  ███╗░░██╗██╗████████╗██████╗░░█████╗░
██╔════╝██╔══██╗██╔══██╗  ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗
╚█████╗░███████║██║░░██║  ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║
░╚═══██╗██╔══██║██║░░██║  ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║
██████╔╝██║░░██║██████╔╝  ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝
            ================================
             	Made by SADTRASH#1337
             https://github.com/sadtrxsh
            ================================
                          
""", Fore.WHITE + Style.NORMAL)
#YES I IS SMART FUCK YOU I DID THIS SHIT FACED            
print ('')
time.sleep(1)
print('How Many codes make for the nitro crimes?')
print ('')
time.sleep(1)
amount = int(input(">"))
print ('')
time.sleep(1)
print ('Generating')
print ('YOUR FUCKING NITRO CRIME IS BEING PLANNED')
time.sleep(2)
print ('')

fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    discord_url = "https://discord.gift/"
    f.write( code + '\n')
    discord_code = discord_url + code
    print('Code: ' + discord_code)
    fix += 1
time.sleep(2)
print ('')
print ('Now use check.py to complete le nitro crimes...')
