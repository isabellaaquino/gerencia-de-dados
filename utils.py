import requests
import json
import pandas as pd

from dotenv import load_dotenv

load_dotenv()


def generate_content(api_key, content):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": content}]}]}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        return None


def generate_content_ollama(content):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {"model": "llama3.2:3b", "prompt": content, "stream": False}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return None


def get_reclame_aqui_url(company: str):
    if company == "HURB TECHNOLOGIES S/A":
        return "https://www.reclameaqui.com.br/empresa/hotel-urbano/"
    elif company == "123 MILHAS/MAXMILHAS/HOTMILHAS":
        return "https://www.reclameaqui.com.br/empresa/123-milhas/"
    elif company == "ENEL ELETROPAULO":
        return "https://www.reclameaqui.com.br/empresa/aes-eletropaulo/"
    elif company == "BRADESCO":
        return "https://www.reclameaqui.com.br/empresa/bradesco/"
    elif company == "ITAU UNIBANCO":
        return "https://www.reclameaqui.com.br/empresa/itau/"
    elif company == "CLARO / NET / EMBRATEL / NEXTEL (AMÉRICA MÓVIL)":
        return "https://www.reclameaqui.com.br/empresa/claro/"
    elif company == "SAMSUNG ELETRONICA DA AMAZONIA LTDA":
        return "https://www.reclameaqui.com.br/empresa/samsung/"
    elif company == "IKEG":
        return "https://www.reclameaqui.com.br/empresa/ikeg/"
    elif company == "SHOPEE":
        return "https://www.reclameaqui.com.br/empresa/shopee/"
    elif company == "VIVO / TELEFÔNICA":
        return "https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv/"

    return ""


def save_to_csv(general_dict):
    data = []

    for company, details in general_dict.items():
        row = {
            "Company": company,
            "Procon CNPJ": details["procon"]["cnpj"],
            "Procon Atendidas": int(details["procon"]["atendidas"].replace(".", "")),
            "Procon Não Atendidas": int(
                details["procon"]["nao_atendidas"].replace(".", "")
            ),
            "Procon Total": int(details["procon"]["total"].replace(".", "")),
            "Procon Atendidas %": float(
                details["procon"]["atendidas_percent"].replace(",", ".").strip("%")
            ),
            "Reclame Aqui Reclamações": int(
                details["reclame_aqui"]["reclamacoes"].replace(".", "")
            ),
            "Reclame Aqui Taxa Resposta %": float(
                details["reclame_aqui"]["taxa_resposta"]
                .replace("%", "")
                .replace(",", ".")
            ),
            "Reclame Aqui Taxa Resolução %": (
                float(
                    details["reclame_aqui"]["taxa_resolucao"]
                    .replace("%", "")
                    .replace(",", ".")
                )
                if details["reclame_aqui"]["taxa_resolucao"]
                .replace("%", "")
                .replace(",", ".")
                not in ["--", "--."]
                else None
            ),
            "Reclame Aqui Tempo Resposta": details["reclame_aqui"]["tempo_resposta"],
        }
        data.append(row)

    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv("companies_analysis.csv", index=False)
    df.to_excel("companies_analysis.xlsx", index=False)
