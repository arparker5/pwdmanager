from hashlib import sha256
from os import system


def printlogo():
    print("******************************************************************************")
    print("*                      _                                                     *")
    print("* _ __  __      __  __| |  _ __ ___    __ _  _ __    __ _   __ _   ___  _ __ *")
    print("*| '_ \ \ \ /\ / / / _` | | '_ ` _ \  / _` || '_ \  / _` | / _` | / _ \| '__|*")
    print("*| |_) | \ V  V / | (_| | | | | | | || (_| || | | || (_| || (_| ||  __/| |   *")
    print("*| .__/   \_/\_/   \__,_| |_| |_| |_| \__,_||_| |_| \__,_| \__, | \___||_|   *")
    print("*|_|                                                       |___/             *")
    print("*                                                                            *")
    print("******************************************************************************")

def enterpwd():
    system('cls')
    printlogo()
    print("Enter your password, or type exit to quit")
    pwd = input("--> ")
    if pwd == 'exit':
        system('cls')
        exit()

    return pwd

def accesspwd(pwd):
    system('cls')
    printlogo()
    while True:
        print("Enter the service, or:")
        print("Type \'pwd\' to reenter your password")
        print("Type \'exit\' to quit")
        service = input("--> ")
        if service == 'exit':
            system('cls')
            exit()
        if service == 'pwd':
            pwd = enterpwd()
            system('cls')
            printlogo()
            continue

        hashedpass = get_hash(pwd, service)

        newpwd = ""
        octlist = []

        for i in range(8):                              # Makes list of octets
            octlist.append(hashedpass[8*i: 8*(i+1)])

        listsorted = octlist.copy()
        listsorted.sort()
        numspot = listsorted[0]                         # octet that will generate a number
        specialspot = listsorted[1]                     # octet that will generate a special char

        for i in range(8):                              # Loop generates each character
            hex_int = int(octlist[i], 16)
            if octlist[i] == numspot:
                newpwd += num[hex_int % 10]
            elif octlist[i] == specialspot:
                newpwd += special[hex_int % 7]
            else:
                newpwd += cap[hex_int % 52]

        system('cls')
        printlogo()

        print("********")
        print(newpwd)
        print("********")


def get_hash(pwd, site):
    return sha256((pwd + site).encode('utf-8')).hexdigest()


cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
num = '0123456789'
special = '!@#$%&*'

password = enterpwd()
accesspwd(password)
