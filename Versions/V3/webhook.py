import requests
import json

class Webhook:
    def __init__(self, url=None, id=None, token=None):
        if url:
            self.url = url
        elif id and token:
            self.url = f"https://discord.com/api/webhooks/{id}/{token}"
        else:
            raise ValueError("Use the URL or id and token.")

    def send_embed(self, title, description, color=0x3498db, fields=None, footer=None):
        embed = {
            "title": title,
            "description": description,
            "color": color
        }
        if fields:
            embed["fields"] = [{"name": f[0], "value": f[1], "inline": f[2] if len(f) > 2 else True} for f in fields]
        if footer:
            embed["footer"] = {"text": footer}

        data = {"embeds": [embed]}

        headers = {"Content-Type": "application/json"}
        response = requests.post(self.url, data=json.dumps(data), headers=headers)

        if response.status_code != 204:
            raise Exception(f"The webhook message could not be sent: {response.status_code} - {response.text}")
        return True

    def send_message(self, title, text):
        headers = {"Content-Type": "application/json"}
        payload = {"title": title, "content": text}

        response = requests.post(self.url, json=payload, headers=headers)
        if response.status_code != 204:
            raise Exception(f"The webhook message could not be sent: {response.status_code} - {response.text}")
        return True
