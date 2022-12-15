#!/usr/bin/env python3
import requests
from tqdm import tqdm

def print_banner():
    banner = '''
  _   _ _______ ______ _____  __ ___  
 ####### ######     #     #####   #####  #     # 
    #    #     #   # #   #     # #     # #     # 
    #    #     #  #   #  #       #       #     # 
    #    ######  #     #  #####  #       ####### 
    #    #   #   #######       # #       #     # 
    #    #    #  #     # #     # #     # #     # 
    #    #     # #     #  #####   #####  #     # 
                                                
 
    '''
    print(banner)
    print('Please enter the website you want to scan without "https:// and www"')
    print('                                                                                             trasch.com')
print_banner()

def subf(domain_name, subd):
    print('Started scanning.')

    # Use tqdm to create a progress bar with automatic max_value calculation
    for subdomain in tqdm(subd):
        url = f'https://{subdomain}.{domain_name}'
        try:
            response = requests.get(url, timeout=5)
            # Check if the status code is 200, indicating that the subdomain exists
            if response.status_code == 200:
                print(f'[+] {url} found.')
        except:
            # Handle any exceptions that occur during the request
            pass

    print('\nThanks for using my program.')

if __name__ == '__main__':
    domain_name = input('Enter the domain you want to scan: ')
    print('\n')

    # Read the list of subdomains from the URL
    response = requests.get('https://raw.githubusercontent.com/theMiddleBlue/DNSenum/master/wordlist/subdomains-top1mil-20000.txt')
    subd = response.text.splitlines()

    subf(domain_name, subd)
