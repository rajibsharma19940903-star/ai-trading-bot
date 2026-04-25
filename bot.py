import requests

TOKEN = "8796123004:AAGDjAhppxlCqwqT_peny2SiTVLUFnO3aqU
CHAT_ID = "5722800652"

def send(msg):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg})

send("✅ Bot successfully running on Cloud 🚀")
