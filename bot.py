import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

CONTACT_URL = "https://t.me/+HgfeOV-dulE3ZDJk"
SONDAGE_URL = "https://t.me/+jwAgNDcMINphOThk"

API = f"https://api.telegram.org/bot{TOKEN}"


def telegram(method, data=None):
    return requests.post(
        f"{API}/{method}",
        json=data or {},
        timeout=15
    ).json()


def afficher_menu(chat_id):

    clavier = {
        "inline_keyboard": [
            [
                {
                    "text": "📞 NOUS CONTACTER",
                    "url": CONTACT_URL
                }
            ],
            [
                {
                    "text": "🛒 MENU / SHOP",
                    "callback_data": "shop"
                },
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
            "Bienvenue sur *Guedrofamilly* 👋"
        ),
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


@app.route("/", methods=["GET"])
def accueil():
    return "🤖 Guedrofamilly Bot OK"


@app.route("/telegram", methods=["POST"])
def recevoir_message():

    update = request.get_json(silent=True) or {}

    message = update.get("message")

    if message:
        chat_id = message["chat"]["id"]
        texte = message.get("text", "").strip()

        if texte in ["/start", "/menu"]:
            afficher_menu(chat_id)

    callback = update.get("callback_query")

    if callback:

        telegram("answerCallbackQuery", {
            "callback_query_id": callback["id"]
        })

        if callback.get("data") == "shop":

            chat_id = callback["message"]["chat"]["id"]

            telegram("sendMessage", {
                "chat_id": chat_id,
                "text": (
                    "🛒 *MENU / SHOP*\n\n"
                    "Bientôt disponible 👀"
                ),
                "parse_mode": "Markdown"
            })

    return "OK"


@app.route("/set-webhook", methods=["GET"])
def configurer_webhook():

    webhook_url = "https://guedrofamillybot.onrender.com/telegram"

    resultat = telegram("setWebhook", {
        "url": webhook_url
    })

    return resultat


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
