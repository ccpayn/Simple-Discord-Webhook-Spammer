# ══════════════════════════ Simple Webhook Spammer ══════════════════════════
import requests
import threading
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

defaultusername = 'Spammed By Payn'
defaultmessage = 'https://github.com/ccpayn | Spammed By Payn'

print(Fore.RED + '                         ╔═══════════════════════════════════════════════════════╗')
print(Fore.RED + '                         ║                                                       ║')
print(Fore.RED + '                         ║  ║   ╔═════════════════════════════════════════╗   ║  ║')
print(Fore.RED + '                         ║  ║   ║   »»────   ItzCutePaчn#9999   ────««    ║   ║  ║')
print(Fore.RED + '                         ║  ║   ║         Join My Discord Server          ║   ║  ║')
print(Fore.RED + '                         ║  ║   ║       https://discord.link/payn         ║   ║  ║')
print(Fore.RED + '                         ║  ║   ╚═════════════════════════════════════════╝   ║  ║')
print(Fore.RED + '                         ║                                                       ║')
print(Fore.RED + '                         ╚═══════════════════════════════════════════════════════╝')
print(Fore.YELLOW + '                                                                         ')
print(Fore.YELLOW + '                                   ██████╗  █████╗ ██╗   ██╗███╗   ██╗')
print(Fore.YELLOW + '                                   ██╔══██╗██╔══██╗╚██╗ ██╔╝████╗  ██║')
print(Fore.YELLOW + '                                   ██████╔╝███████║ ╚████╔╝ ██╔██╗ ██║')
print(Fore.YELLOW + '                                   ██╔═══╝ ██╔══██║  ╚██╔╝  ██║╚██╗██║')
print(Fore.YELLOW + '                                   ██║     ██║  ██║   ██║   ██║ ╚████║')
print(Fore.YELLOW + '                                   ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝')
print(Fore.YELLOW + '                             ═════════════════════════════════════════════')

print(Fore.WHITE + '                                                                ')
def sendtowebhook(webhook, message, username):
    data = {
        'content': message,
        'username': username
    }
    try:
        while True:
            requests.post(webhook, data=data)
    except KeyboardInterrupt:
        exit()

print(Fore.YELLOW + '                                                                ')
webhook = input('> Webhook Link?: ')
if webhook == '':
    print('You need to specify a webhook link for this to work, exiting...')
    exit()

username = input('> What would you like the username to be?: ')
if username == '': 
    username = defaultusername
    print('Using default username...')

message = input('> Your Message: ')
if message == '': 
    message = defaultmessage
    print('Using default message...')

try:
    threads = int(input('How many threads would you like to run on?: '))
    if threads < 1:  
        print('Negative or no threads, defaulting to 1...')
        threads = 1
except ValueError: 
    threads = 1
    print('Invalid amount of threads, defaulting to 1...')

print('Starting.., press CTRL+C to stop.')

for x in range(threads):
    thread = threading.Thread(
        target=sendtowebhook(webhook, message, username), args=(1,))
    thread.start()
# ══════════════════════════ Simple Webhook Spammer ══════════════════════════