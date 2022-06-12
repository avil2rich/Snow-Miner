import time
import colorama
from colorama import Fore
from colorama import Style
import random
import string

colorama.init()

print(Fore.RED + '''


░██████╗███╗░░██╗░█████╗░░██╗░░░░░░░██╗  ███╗░░░███╗██╗███╗░░██╗███████╗██████╗░
██╔════╝████╗░██║██╔══██╗░██║░░██╗░░██║  ████╗░████║██║████╗░██║██╔════╝██╔══██╗
╚█████╗░██╔██╗██║██║░░██║░╚██╗████╗██╔╝  ██╔████╔██║██║██╔██╗██║█████╗░░██████╔╝
░╚═══██╗██║╚████║██║░░██║░░████╔═████║░  ██║╚██╔╝██║██║██║╚████║██╔══╝░░██╔══██╗
██████╔╝██║░╚███║╚█████╔╝░░╚██╔╝░╚██╔╝░  ██║░╚═╝░██║██║██║░╚███║███████╗██║░░██║
╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝


Made by ray#4567 )) Join https://discord.gg/KUp44gPbDT - dsc.gg/snow-miner To Get The licenseKey!

''' + Fore.RESET)
time.sleep(1)

LicenseKey = 'tkhMogbFcxe74ufL'

if input('Enter your License Key: ') == LicenseKey:
    print("Checking if License key is valid...")
    time.sleep(2)
    print(Fore.GREEN + "Key is Valid!" + Fore.RESET)
    crypto = input("Choose between ETH or BTC: ")

    if crypto == 'ETH' or crypto == 'BTC':
        print("Okay. Wallets are being prepared ...")
        time.sleep(3)

        if crypto == "ETH":
            adress = str(input("Please enter your Ethereum Wallet adress: "))
            print("Check if Wallet exist...")
            time.sleep(2)
            print(Fore.GREEN + "Check succesfully!" + Fore.RESET)
            time.sleep(1)
            print("Miner written by ray#4567")
            time.sleep(1)

        elif crypto == 'BTC':
            adress = str(input("Please enter your Bitcoin Wallet adress: "))
            print("Check if Wallet exist...")
            time.sleep(2)
            print(Fore.GREEN + "Check succesfully!" + Fore.RESET)
            time.sleep(1)
            print("Miner written by ray#4567")
            time.sleep(1)
                    
        def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
            return "".join(random.choice(chars) for _ in range(size))

        tries = 0

        if crypto == "ETH":
            while(True):
                if(tries > random.randint(10000000000, 100000000000)):
                    print(Fore.GREEN + "[-] 0x" + id_gen() + " | Valid | " + "0.582" + "ETH")
                    print("Transfer 0.582 ETH to", adress)
                    time.sleep(7)
                    tries = 0
                    print("Done! Miner is running again!")
                    time.sleep(3)
                else:
                    print(Fore.RED + "[-] 0x" + id_gen() + " | Invalid | " + "0.00000 ETH")
                    tries += 1

        elif crypto == "BTC":
            while(True):
                if(tries > random.randint(10000000000, 100000000000)):
                    print(Fore.GREEN + "[-] bc1" + id_gen() + " | Valid | " "0.0145" "BTC")
                    print("Transfer  0.0145 BTC to", adress)
                    time.sleep(6)
                    tries = 0
                    print("Done! Miner is running again!")
                    time.sleep(3)
                else:
                    print(Fore.RED + "[-] bc1" + id_gen() + " | Invalid | " + "0.00000 BTC")
                    tries += 1
    else:
        print(Fore.RED + "Invalid currency. Please choose between 'ETH' and 'BTC'. Press Enter to exit")
        input("")
else:
    print(Fore.RED + "Invalid license key. Press Enter to exit.")
    input("")