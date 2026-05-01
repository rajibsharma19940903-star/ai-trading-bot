import requests
import time

TOKEN = "8796123004:AAGDjAhppxlCqwqT_peny2SiTVLUFn03aqU"
CHAT_ID = "5722800652"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

# Start message
send("✅ Bot successfully running 🚀")

# Keep bot alive (VERY IMPORTANT)
while True:
    time.sleep(60)
