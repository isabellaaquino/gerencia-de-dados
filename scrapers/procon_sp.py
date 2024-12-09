from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROCON_URL = "https://app.powerbi.com/view?r=eyJrIjoiNTZmOTliMjAtNzk5Zi00NTZkLWEwNGYtZjZhODA4ZmM0MDgwIiwidCI6IjNhNzhiMGNkLTdjOGUtNDkyOS04M2Q1LTE5MGE2Y2MwMTM2NSJ9"


def scrape_powerbi_data(num_rows, driver_path) -> dict:
    """
    Scrape data from a Power BI report page.

    :param num_rows: Number of rows to scrape from the report.
    :param driver_path: Path to the ChromeDriver executable.
    """

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(PROCON_URL)

        # Div que contém a tabela de dados é pivotTableCellWrap, logo precisamos esperar ela carregar

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pivotTableCellWrap"))
        )

        html_content = driver.page_source

        # Parseador de HTML
        soup = BeautifulSoup(html_content, "html.parser")

        rows = soup.find_all("div", class_="pivotTableCellWrap")

        infos = {}
        counter = 0
        current_company = None

        # Para essa tabela do procon, existem 6 linhas por empresa
        # As 6 primeiras linhas são do cabeçalho
        # num_rows é o número de empresas que queremos extrair de forma parametrizada

        for row in rows[6 : (num_rows + 1) * 6]:
            if counter == 0:
                current_company = row.text.strip()
                infos[current_company] = {}

            elif counter == 1:
                infos[current_company]["cnpj"] = row.text.strip()

            elif counter == 2:
                infos[current_company]["atendidas"] = row.text.strip()

            elif counter == 3:
                infos[current_company]["nao_atendidas"] = row.text.strip()

            elif counter == 4:
                infos[current_company]["total"] = row.text.strip()

            elif counter == 5:
                infos[current_company]["atendidas_percent"] = row.text.strip()
                counter = 0
                continue

            counter += 1

    finally:
        driver.quit()

    return infos
