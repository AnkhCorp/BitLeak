from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init

# Inicializa colorama para Windows/Linux
init(autoreset=True)

def main():
    torrent = input("Digite o endereço IP: ").strip()
    url = f"https://iknowwhatyoudownload.com/en/peer/?ip={torrent}"

    # Configura o navegador em modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Inicia o driver sem especificar caminho manualmente
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Acessa a URL
        driver.get(url)

        # Aguarda até que a tabela esteja presente (timeout de 10 segundos)
        wait = WebDriverWait(driver, 10)
        table = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "table-condensed"))
        )

        # Exibe o texto da tabela se encontrada
        print(table.text if table else "Tabela não encontrada.")
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()