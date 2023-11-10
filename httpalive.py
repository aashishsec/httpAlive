import requests
import sys

def banner():
    print('''
      

██╗░░██╗████████╗████████╗██████╗░░░░░░░░█████╗░██╗░░░░░██╗██╗░░░██╗███████╗
██║░░██║╚══██╔══╝╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░░░░██║██║░░░██║██╔════╝
███████║░░░██║░░░░░░██║░░░██████╔╝█████╗███████║██║░░░░░██║╚██╗░██╔╝█████╗░░
██╔══██║░░░██║░░░░░░██║░░░██╔═══╝░╚════╝██╔══██║██║░░░░░██║░╚████╔╝░██╔══╝░░
██║░░██║░░░██║░░░░░░██║░░░██║░░░░░░░░░░░██║░░██║███████╗██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝
      
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashish36
        
      ''')
    
def help():
        banner()
        print(
            
        '''
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
                   
                   print("(Status: {}) --[Size: {}]---> {}".format(statusCode,content_length,subdomain))

               else:
                   
                   print("(Status: {}) --[Size: {}]---> {}".format(statusCode,len(request.content),subdomain))

            else:
               
               print("(Status: {}) --[Size: {}]---> {}".format(statusCode,len(request.content),subdomain))
                      
               
        except:

            pass

        attempts +=1



if sys.argv !=2:
    help()
    
if sys.argv[1] =="-h":
    help()
else:
    httpAlive(sys.argv[1])
