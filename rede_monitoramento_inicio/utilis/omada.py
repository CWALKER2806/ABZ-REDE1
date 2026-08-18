import requests
from config import OMADA_URL, CLIENT_ID, CLIENT_SECRET, SITE_ID


def autenticar():

    if not OMADA_URL:
        print("API da Omada ainda não configurada.")
        return None

    print("Conectando à Omada...")

    # Aqui faremos o login quando a API existir
    return None

def obter_dispositivos():

    token = autenticar()

    if token is None:
        return []

    return []