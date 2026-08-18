from flask import Flask, render_template, request, redirect
import socket 


from utilis.scanner import escanear_rede
from utilis.omada import obter_dispositivos
app = Flask(__name__)

@app.route("/", methods=["GET" , "POST"])
def login():
    
 if request.method =="POST":
        
     usuario = request.form["usuario"]
     senha = request.form["senha"]
     
     print("Usuário:" , usuario)
     print("Senha:" , senha)
    
     return redirect("/dashboard")
    
 return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    
    gateway = "10.0.0.1"
    mac = "98-2a-0a-8a-dc-c1"
    
    usuarios = 1
    equipamentos = 10
    alertas = 2
    intelbras = "Online"
    
    arp = ""
    dispositivos_ping = escanear_rede("10.0.0")

    dispositivos_omada = obter_dispositivos()

    dispositivos = dispositivos_ping + dispositivos_omada
    
    
    return render_template(
        "dashboard.html",
        nome=hostname,
        ip=ip,
        gateway=gateway,
        mac=mac,
        usuarios=usuarios,
        equipamentos = equipamentos,
        alertas = alertas,
        intelbras = intelbras,
        dispositivos = dispositivos,
        arp=arp
        )
    


if __name__ == "__main__":
    app.run(debug=True)
    
    