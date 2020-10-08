from colorama import Fore, Style, init
import requests
init()
#SHUT THE FUCK UP ABOUT COLORAMA NOT WORKING, IT FUCKING WORKS OK!!!???
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
                          
""")  
#welcome to this bullshit but in python
def checkNitro(code, userToken):

    URL = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem'
    result = requests.post(URL, headers={'authorization': userToken}).text
    if 'nitro' in result:
        return True
    else: 
        return False


userToken = str(input('Enter Your fuckin Discord Token. \n >')) #for checking purposes this will not redeem

VALID_CODES_FILE   = "valid_nitro_codes.txt"
INVALID_CODES_FILE = "invalid_nitro_codes.txt"
CODES_FILE         = "nitro_codes.txt"

validTokens_file   = open(VALID_CODES_FILE, 'a+')
invalidTokens_file = open(INVALID_CODES_FILE, 'a+')

with open(CODES_FILE , 'r') as codes_file:
    content = codes_file.readlines()
    codes = list(filter(None, list(map(lambda x: str.replace(x, "\n", ""), content)))) # deletes the useless shit

    for code in codes:
        status = checkNitro(code, userToken)
        if status is True:
            print(f'{Fore.GREEN + Style.BRIGHT} {code}', Fore.WHITE + Style.NORMAL)
            validTokens_file.write(code + "\n")
        else:
            print(f'{Fore.RED + Style.BRIGHT} {code}', Fore.WHITE + Style.NORMAL)
            invalidTokens_file.write(code + "\n")
print('Done.')
input() #yeah fuck you cunts

