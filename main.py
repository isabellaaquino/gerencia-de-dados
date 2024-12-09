from scrapers.procon_sp import scrape_powerbi_data
from scrapers.reclame_aqui import scrape_reclame_aqui
from utils import get_reclame_aqui_url, save_to_csv
from analyze import analyze
import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def main():
    driver_path = os.getenv("CHROME_DRIVER_PATH")

    general_dict = {}
    # Primeiro, pegamos as informações das top 10 empresas no Procon SP
    procon_dict = scrape_powerbi_data(10, driver_path)

    for company, procon_infos in procon_dict.items():
        url = get_reclame_aqui_url(company)

        # Agora, pegamos as informações do Reclame Aqui
        reclame_aqui_info = scrape_reclame_aqui(url, company, driver_path)

        # Unindo as informações
        general_dict[company] = {
            "procon": procon_infos,
            "reclame_aqui": reclame_aqui_info,
        }

    save_to_csv(general_dict)

    analyze()


# main()
analyze()
