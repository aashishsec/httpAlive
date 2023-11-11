import requests

import sys

import colorama

import random

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

red = Fore.RED

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

colors = [green,magenta,cyan,mixed,red,blue,yellow, white]

random_color = random.choice(colors)

bold = Style.BRIGHT

def banner():
    print(f'''{bold}{random_color}
      

██╗░░██╗████████╗████████╗██████╗░░░░░░░░█████╗░██╗░░░░░██╗██╗░░░██╗███████╗
██║░░██║╚══██╔══╝╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░░░░██║██║░░░██║██╔════╝
███████║░░░██║░░░░░░██║░░░██████╔╝█████╗███████║██║░░░░░██║╚██╗░██╔╝█████╗░░
██╔══██║░░░██║░░░░░░██║░░░██╔═══╝░╚════╝██╔══██║██║░░░░░██║░╚████╔╝░██╔══╝░░
██║░░██║░░░██║░░░░░░██║░░░██║░░░░░░░░░░░██║░░██║███████╗██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝
      
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashish36
          
        HttpAlive is a tool designed to efficiently probe for alive subdomains and Urls from a provided list.
        
      ''')
    
def help():
        banner()
        print(f'''{bold}{random_color}
    Usage: python httpAlive.py file-paths-url

    Options:
    -h --> help
    -u --> List of Subdomains or URLs
        ''')

def httpAlive(urlfile):
  
  banner()
  attempts=0
  
  with open(urlfile,"r") as subdomains:

    for subdomain in subdomains:

        try:

            subdomain = subdomain.strip("\n")

            if subdomain[0:5]=="https" or subdomain[0:7]=="http://":
                  
                  url=subdomain

            else:
                  
                  url="https://{}".format(subdomain)

            request=requests.get(url)

            statusCode=request.status_code

            if statusCode== 200:
               
               content_length = request.headers.get('Content-Length')

               if content_length is not None:
                   
                   print(f"{bold}{green}(Status: {statusCode}) --[Size: {content_length}]---> {subdomain}")

               else:
                   
                   print(f"{bold}{green}(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}")

            else:
               
                print(f"{bold}{random_color}(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}")
                      
               
        except:

            pass

        attempts +=1


def main():
    
    if len(sys.argv)!=2 or sys.argv[1]=="-h":
        
        help()
    else:
        httpAlive(sys.argv[1])   
     


if __name__ == "__main__":
    
    main()

