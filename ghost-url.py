import requests
import argparse
import json
from colorama import Fore, Style
parser = argparse.ArgumentParser(description="This use to extrect url info" )
parser.add_argument("-d", "--domain", help="The target domain")
parser.add_argument("-all", "--allurls", help="to get the all url")
parser.add_argument("-o", "--output", help="Output file name .json extension)")
args = parser.parse_args()
if not any(vars(args).values()):
    print("to see the option usage: urlscan.py [-h] ")

tar_domain = args.domain
print(Fore.RED,"""
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗      ██╗   ██╗██████╗ ██╗     
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝      ██║   ██║██╔══██╗██║     
██║  ███╗███████║██║   ██║███████╗   ██║   █████╗██║   ██║██████╔╝██║     
██║   ██║██╔══██║██║   ██║╚════██║   ██║   ╚════╝██║   ██║██╔══██╗██║     
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║         ╚██████╔╝██║  ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝          ╚═════╝ ╚═╝  ╚═╝╚══════╝
 @sudo-xzero
 """, Style.RESET_ALL)
url = f'https://urlscan.io/api/v1/search/?q={tar_domain}'

response = requests.get(url)


if response.status_code == 200:
    data = response.json()  
    
    
    specific_page = None
    for result in data.get('results', []):
        page_url = result.get('page', {}).get('url')
        if page_url in [f'https://{tar_domain}/', f'https://www.{tar_domain}/']:
            specific_page = result['page']
            break
    
 
    if specific_page:
        print(specific_page)
else:
    print(f"Error: {response.status_code}")
if args.allurls:
    TAR_domain = args.allurls
    response = requests.get(f'https://urlscan.io/api/v1/search/?q={TAR_domain}')
    
    if response.status_code == 200:
        print(response.json())


if args.output:
            with open(args.output, 'w') as outfile:
                if args.output.endswith('.json'):
                    json.dump(data, outfile, indent=4)
                else:
                    outfile.write(str(data))
            print(f"Data saved to {args.output}")





