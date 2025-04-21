from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style, init

class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    END = '\033[0m'

text = r"""
    __    _ __  __           __  
   / /_  (_) /_/ /__  ____ _/ /__
  / __ \/ / __/ / _ \/ __ `/ //_/
 / /_/ / / /_/ /  __/ /_/ / ,<   
/_.___/_/\__/_/\___/\__,_/_/|_|                                   
"""

green_text = TextColor.GREEN + text + TextColor.END
print(green_text)
print("\033[1mCreated by\033[0m AnkhCorp 1.0")

init(autoreset=True)

def main():
    torrent = input("Enter the IP address: ").strip()
    url = f"https://iknowwhatyoudownload.com/en/peer/?ip={torrent}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        table = soup.find('table', class_='table-condensed')
        
        if table:
            rows = table.find_all('tr')[1:]
            
            if not rows:
                print("No results found for this IP.")
                return
            
            for row in rows:
                cells = row.find_all('td')[1:]
                data = [cell.get_text(strip=True) for cell in cells]
                print("\n".join(data))
                print("-" * 40)
        else:
            print("Table not found. The website may have changed or the IP has no history.")
            
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
