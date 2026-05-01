import requests
import time

TOKEN = "8796123004:AAGDjAhppxlCqwqT_peny2SiTVLUFnO3aqU"
CHAT_ID = "5722800652"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    res = requests.post(url, data=data)
    print(res.text)

# हर 1 मिनट me message bhejega (test ke liye)
while True:
    send("✅ Bot running perfectly 🚀")
    time.sleep(60)
