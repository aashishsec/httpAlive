#!/usr/bin/python3

import requests

import colorama

import random

import argparse

import concurrent.futures

import httpx

from datetime import datetime

from colorama import Fore, Style

colorama.init(autoreset=True)

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

red = Fore.RED

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [magenta,cyan,mixed,red,blue,yellow, white]

random_color = random.choice(colors)

USER_AGENT  = [
        
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",

    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/99.0.1150.36",

    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",

     ]
     

random_user_agent = random.choice(USER_AGENT)

parser=argparse.ArgumentParser(description=f"{bold}{random_color}httpAlive is a tool designed to efficiently probe for alive subdomains and Urls from a provided list.")

parser.add_argument('-l','--DomainList',metavar='list',type=str,required=True,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of Subdomains or URLs.")

parser.add_argument('-o','--output',metavar='output',type=str,default="httpAlive_output.txt",required=False,help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")

parser.add_argument("-c", "--concurrency", help=f"[{bold}{random_color}INFO{random_color}]: {bold}{random_color}Concurrency level to make fast process.", type=int, default=5)

parser.add_argument("-t", "--threads", help=f"[{bold}INFO{random_color}]: {random_color}{random_color}Threading level to make fast process.", type=int, default=5)

args=parser.parse_args()

DominList=args.DomainList

output=args.output

concurrency=args.concurrency

threads=args.threads

global_output=[]

global_urls=[]
        

def banner():

    print(f'''{bold}{random_color}

██╗░░██╗████████╗████████╗██████╗░░░░░░░░█████╗░██╗░░░░░██╗██╗░░░██╗███████╗
██║░░██║╚══██╔══╝╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░░░░██║██║░░░██║██╔════╝
███████║░░░██║░░░░░░██║░░░██████╔╝█████╗███████║██║░░░░░██║╚██╗░██╔╝█████╗░░
██╔══██║░░░██║░░░░░░██║░░░██╔═══╝░╚════╝██╔══██║██║░░░░░██║░╚████╔╝░██╔══╝░░
██║░░██║░░░██║░░░░░░██║░░░██║░░░░░░░░░░░██║░░██║███████╗██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝
      
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashishsec
          
        httpAlive is a tool designed to efficiently probe for alive subdomains and Urls from a provided list.
          
      ''')
    print("-" * 80)

    checking_vesion()

    print(f"{bold}{random_color}httpAlive starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    print("-" * 80)
   
    print(f"{bold}{random_color}[*] Threads".ljust(20, " "), ":", threads)

    print(f"{bold}{random_color}[*] Concurrency".ljust(20, " "), ":",concurrency)

def checking_vesion():

    version = "v1.0.2"
    
    url = f"https://api.github.com/repos/aashishsec/httpAlive/releases/latest"
    
    try:
            
         response =  requests.get(url, timeout=10)
          
         if response.status_code == 200:
            
            data = response.json()
                
            latest = data.get('name')
            
            if latest == version:
                
                    message = "latest"
                
                    print(f"[{blue}Version{reset}]: {bold}{white}httpAlive current version {version} ({green}{message}{reset})")
                
                    t.sleep(1)
                
            else:
                
                    message ="outdated"
                
                    print(f"[{blue}Version{reset}]: {bold}{white}httpAlive current version {version} ({red}{message}{reset})")

            
    except KeyboardInterrupt as e:
        
            print(f"[{blue}INFO{random_color}]: httpAlive says BYE!")
        
            exit()
                
    except Exception as e:

           pass


def httpAlive(subdomain):

    global global_output

    if subdomain[0:5]=="https" or subdomain[0:7]=="http://":
                  
            url=subdomain

    else:
                  
            url="https://{}".format(subdomain)
    
    header={"User-Agent": random_user_agent}

    try:
            with httpx.Client(verify=False,timeout=10,follow_redirects=True,headers=header) as client:

                  request=client.get(url)

            statusCode=request.status_code

            content_length = request.headers.get('Content-Length')

            if statusCode== 200:

               if content_length is not None:
                   
                   print(f"{green}(Status: {statusCode}) --[Size: {content_length}]---> {subdomain}")

                   global_output.append(f"(Status: {statusCode}) --[Size: {content_length}]---> {subdomain}\n")

               else:
                   
                   print(f"{green}(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}")

                   global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}\n")

            else:
               
                print(f"{random_color}(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}")

                global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}\n")
                
    except KeyboardInterrupt as e:
        
            print(f"[{blue}INFO{random_color}]: httpAlive says BYE!")
        
            exit()
                
    except Exception as e:
        
           pass

def saveOutput(output):

    with open(output, 'w') as file:
        
        file.writelines(global_output)


def threading(urls):
    
    try:

        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency*threads) as executor:
            
           futures = [executor.submit(httpAlive, url) for url in urls]
           
        concurrent.futures.wait(futures)
           
    except KeyboardInterrupt as e:
        
        print(f"[{bold}INFO{random_color}]: httpAlive says BYE!")
        
        exit()

    except Exception as e:
        
        pass 


def main():

    banner()

    global global_urls
    
    try:
        
        with open(DominList,"r") as subdomains:
       
           subdomain=subdomains.read().splitlines()
        
           for url in subdomain:
          
               global_urls.append(url)

        print(f"{bold}{random_color}[*] No.of Words".ljust(20, " "), ":", len(global_urls))

        print("-" * 80)

        threading(global_urls)

        saveOutput(output) 
           
    except KeyboardInterrupt as e:
        
        print(f"[{blue}INFO{random_color}]: httpAlive says BYE!")
        
        exit()

    except Exception as e:
        
        pass 

if __name__ == "__main__":

    main()
