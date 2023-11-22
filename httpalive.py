import requests,colorama,random,argparse,concurrent.futures

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

reset = Style.RESET_ALL

colors = [magenta,cyan,mixed,red,blue,yellow, white]

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
          
        httpAlive is a tool designed to efficiently probe for alive subdomains and Urls from a provided list.
          
      ''')


parser=argparse.ArgumentParser(description=f"{bold}{random_color}httpAlive is a tool designed to efficiently probe for alive subdomains and Urls from a provided list.")

parser.add_argument('-l','--DomainList',metavar='list',type=str,required=True,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of Subdomains or URLs.")

parser.add_argument('-o','--output',metavar='output',type=str,default="httpAlive_output.txt",required=False,help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")

parser.add_argument("-c", "--concurrency", help=f"[{bold}{random_color}INFO{random_color}]: {bold}{random_color}Concurrency level to make fast process", type=int, default=10)

parser.add_argument("-t", "--threads", help=f"[{bold}INFO{random_color}]: {random_color}{random_color}Threading level to make fast process", type=int, default=4)

args=parser.parse_args()

DominList=args.DomainList

output=args.output

concurrency=args.concurrency

threads=args.threads

global_output=[]


def httpAlive(subdomain):

    global global_output

    try:

            if subdomain[0:5]=="https" or subdomain[0:7]=="http://":
                  
                  url=subdomain

            else:
                  
                  url="https://{}".format(subdomain)

            request=requests.get(url,timeout=10)

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


def main(DominList):
        
    banner()

    urls=[]
    
    try:
        with open(DominList,"r") as subdomains:
       
           subdomain=subdomains.read().splitlines()
        
           for url in subdomain:
          
               urls.append(url)

        threading(urls)

        saveOutput(output) 
           
    except KeyboardInterrupt as e:
        
        print(f"[{blue}INFO{random_color}]: httpAlive says BYE!")
        
        exit()

    except Exception as e:
        
        pass 

if __name__ == "__main__":

    main(DominList)
