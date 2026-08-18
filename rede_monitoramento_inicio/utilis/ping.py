import subprocess


def testar_ping(ip):
    comando = ["ping", "-n", "1", "-w", "200", ip]


    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True
    )

    return resultado.returncode == 0