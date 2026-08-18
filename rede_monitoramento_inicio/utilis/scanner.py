from utilis.ping import testar_ping
from concurrent.futures import ThreadPoolExecutor

def verificar_ip(ip):

    if testar_ping(ip):

        return {
            "ip": ip,
            "mac": "Desconhecido",
            "tipo": "Ativo",
            "status": "🟢 Online"
               }                  

    return None


def escanear_rede(rede):

    dispositivos = []

    with ThreadPoolExecutor(max_workers=50) as executor:

        ips = [f"{rede}.{i}" for i in range(1, 255)]

        resultados = executor.map(verificar_ip, ips)

        for resultado in resultados:

          if resultado:
              dispositivos.append(resultado)
              
    return dispositivos          