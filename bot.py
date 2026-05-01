import requests
import time

TOKEN = "YOUR_TELEGRAM_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

def strategy():
    # yaha market logic ayega
    price = 100  # dummy

    if price > 95:
        send("BUY SIGNAL 🚀")
    else:
        send("SELL SIGNAL 🔻")

while True:
    strategy()
    time.sleep(60)import requests
import time

TOKEN = "https://api.telegram.org/bot123456:ABCxyz/sendMessage?chat_id=123456789&text=hello"
CHAT_ID = "5722800652"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

def strategy():
    # yaha market logic ayega
    price = 100  # dummy

    if price > 95:
        send("BUY SIGNAL 🚀")
    else:
        send("SELL SIGNAL 🔻")

while True:
    strategy()
    time.sleep(60)
