import requests
import os



class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

os.system('clear')
Logo = f'''
{Colors.YELLOW}
       _               _        _             
__      _____| |__        ___| |_ __ _| |_ _   _ ___ 
\ \ /\ / / _ \ '_ \ _____/ __| __/ _` | __| | | / __|
 \ V  V /  __/ |_) |_____\__ \ || (_| | |_| |_| \__ \\
  \_/\_/ \___|_.__/      |___/\__\__,_|\__|\__,_|___/
                                                     {Colors.RESET}\n
'''
print(Logo)
print(f"{Colors.RED}Created by computer_boy also known as huntinghackers : insta: computer_boy5{Colors.RESET}\n")
filename = input("Enter the file where you saved the sub-domains or domains: ")



with open(filename, 'r') as file:
    domains = file.readlines()

for domain in domains:
    domain = domain.strip() 
    if domain: 
        try:
            response = requests.get(f"http://{domain}")  
            print(f"Processing {domain}...")
            status_code = response.status_code
            
            if status_code == 200:
                print(f"{Colors.GREEN}Status Code: {status_code} - Valid!!!{Colors.RESET}")
            elif status_code == 301:
                print(f"{Colors.YELLOW}Status Code: {status_code} - Redirection detected!!!{Colors.RESET}")
            elif status_code == 403:
                print(f"{Colors.YELLOW}Status Code: {status_code} - Not available!!!{Colors.RESET}")
            elif status_code == 500:
                print(f"{Colors.RED}Status Code: {status_code} - Server error{Colors.RESET}")
            else:
                print(f"Status Code: {status_code} - Other status code")

        except requests.ConnectionError:
            print(f"{Colors.RED}Connection error for {domain}. The URL might not exist or there might be a network issue.{Colors.RESET}")
        except requests.HTTPError as http_err:
            print(f"{Colors.RED}HTTP error occurred for {domain}: {http_err}{Colors.RESET}")
        except requests.Timeout:
            print(f"{Colors.RED}Timeout occurred for {domain}. The request took too long to complete.{Colors.RESET}")
        except requests.TooManyRedirects:
            print(f"{Colors.RED}Too many redirects occurred for {domain}. Check the URL for potential issues.{Colors.RESET}")
        except requests.RequestException as e:
            print(f"{Colors.RED}An error occurred for {domain}: {e}{Colors.RESET}")
print("Digg more!!!!!!{Colors.RESET}")
