# httpAlive

- HttpAlive is a  tool designed to efficiently probe for alive subdomains and Urls  from a provided list along with statuscode and content length.

- This httpAlive tool also had threading which will speed up the process.
  
-  Works in all platforms.

## Installation

- Clone the repository to your local machine.
  
- Install the required dependencies using pip


```bash
git clone https://github.com/aashish36/httpAlive.git

cd httpAlive

pip install -r requirements.txt

```

## Usage

- Create a file containing that contains list of URLs or subdoamins or both and give to httpAlive. The output contains status codes and content length.

- This python code will save the results of the analysis to a file named 'output.txt'.

- Run the script using the following command: 

``` bash

usage: httpalive-Mark9.py [-h] -l list [-o output] [-c CONCURRENCY] [-t THREADS]

httpAlive is a tool designed to efficiently probe for alive subdomains and Urls from a provided list.

options:

  -h, --help            show this help message and exit.

  -l list, --DomainList list
                        [INFO]: List of Subdomains or URLs.

  -o output, --output output
                        [INFO]: File to save our output.

  -c CONCURRENCY, --concurrency CONCURRENCY
                        [INFO]: Concurrency level to make fast process.

  -t THREADS, --threads THREADS
                        [INFO]: Threading level to make fast process.

```
## Tool Output

![Screenshot 2023-11-28 173900](https://github.com/aashishsec/httpAlive/assets/65489287/bfaff3d7-b434-416e-87b3-b38b5954c1a7)

## Contributing

- Contributions are welcome!
  
- If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


![image](https://github.com/aashish36/JSScanner/assets/65489287/70f7e3a8-e95f-429b-9433-89087daad721)

