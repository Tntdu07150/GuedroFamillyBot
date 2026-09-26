import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# =========================
# LIENS
# =========================

# Anciens liens conservés
CONTACT_URL = "https://t.me/+HgfeOV-dulE3ZDJk"
SONDAGE_URL = "https://t.me/+jwAgNDcMINphOThk"

# Nouveaux liens
SHOP_URL = "https://t.me/+vLsDOxqSwAM1Njhk"
LOCALISATION_URL = "https://t.me/+RvPIBlR9YaczMTA0"
COLIS_URL = "https://t.me/+mSsjkyjSmVU2M2U8"

API = f"https://api.telegram.org/bot{TOKEN}"


def telegram(method, data=None):
    return requests.post(
        f"{API}/{method}",
        json=data or {},
        timeout=15
    ).json()


# =========================
# MENU PRINCIPAL
# =========================

def menu_principal(chat_id):

    clavier = {
        "inline_keyboard": [
            [
                {
                    "text": "🛒 MENU / SHOP",
                    "url": SHOP_URL
                }
            ],
            [
                {
                    "text": "📞 NOUS CONTACTER",
                    "url": CONTACT_URL
                }
            ],
            [
                {
                    "text": "📍 LOCALISATION",
                    "url": LOCALISATION_URL
                }
            ],
            [
                {
                    "text": "📦 COLIS EN LIVRAISON !",
                    "url": COLIS_URL
                }
            ],
            [
                {
                    "text": "📊 SONDAGE",
                    "url": SONDAGE_URL
                }
            ]
        ]
    }

    telegram("sendMessage", {
        "chat_id": chat_id,
        "text": (
            "✈️ *MENU PRINCIPAL*\n\n"
            "Salut à tous, sur le bot de *Guedro familly* ! 👋\n\n"
            "Vous pouvez retrouver juste en dessous tous les services de notre groupe.\n\n"
            "On tient à vous remercier de votre fidélité ✅🤝"
        ),
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# ACCUEIL
# =========================

@app.route("/", methods=["GET"])
def accueil():
    return "🤖 Guedrofamilly Bot OK"


# =========================
# RÉCEPTION TELEGRAM
# =========================

@app.route("/telegram", methods=["POST"])
def recevoir_message():

    update = request.get_json(silent=True) or {}

    message = update.get("message")

    if message:

        chat_id = message["chat"]["id"]
        texte = message.get("text", "").strip()

        if texte in ["/start", "/menu"]:
            menu_principal(chat_id)

    return "OK"


# =========================
# WEBHOOK
# =========================

@app.route("/set-webhook", methods=["GET"])
def configurer_webhook():

    webhook_url = "https://guedrofamillybot.onrender.com/telegram"

    resultat = telegram("setWebhook", {
        "url": webhook_url
    })

    return resultat


# =========================
# DÉMARRAGE
# =========================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )
