from colorama import Fore, Back, Style

def log_direct(name):
    return print(f'{Fore.BLUE}{name}/{Fore.RESET}')

def log_file(name, format):
    return print(f'{Fore.GREEN}{name}{Fore.RESET}.{Fore.YELLOW}{format}{Fore.RESET}')