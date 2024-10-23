from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Launch Colorama for Windows/Linux
init(autoreset=True)

def main():
    torrent = input("Digite o endereço IP: ").strip()
    url = f"https://iknowwhatyoudownload.com/en/peer/?ip={torrent}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Start the driver without specifying the path manually
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        # Waits until the table is present (30 second timeout)
        wait = WebDriverWait(driver, 30)
        table = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "table-condensed"))
        )

        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells:
                data = [cell.text for cell in cells[1:]]  # Skip the first column
                print("\n".join(data)) 

    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
