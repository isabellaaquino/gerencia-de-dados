from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def get_span_first_text(span, split=True):
    if not split:
        return span.find("strong", style="color: #1F69C1;").get_text(strip=True)
    return span.find("strong", style="color: #1F69C1;").get_text(strip=True).split()[0]


def find(driver):
    element = driver.find_element(By.CLASS_NAME, "go2549335548")
    if element:
        return element
    else:
        return False


def scrape_reclame_aqui(url, company, driver_path):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    # Espera o elemento com a classe "newPerformanceCard-tab-5" aparecer (tab GERAL)
    general_tab_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "newPerformanceCard-tab-3"))
    )

    # Clica na tab GERAL
    general_tab_button.click()

    # Espera o elemento com a classe "go267425901" aparecer, com tab GERAl selecionada
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "go2549335548"))
    )

    html = driver.page_source

    driver.quit()

    # Parseador de HTML
    soup = BeautifulSoup(html, "html.parser")

    # Spans que contêm informacoes de 2023
    spans = soup.find_all("span", class_="go2549335548")

    infos = {}

    infos["empresa"] = company
    infos["reclamacoes"] = get_span_first_text(spans[0])
    infos["taxa_resposta"] = get_span_first_text(spans[1])
    infos["taxa_resolucao"] = get_span_first_text(spans[5])
    infos["tempo_resposta"] = get_span_first_text(spans[6], split=False)

    return infos
