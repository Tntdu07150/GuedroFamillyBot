import requests
import time

# ==============================
# CONFIGURATION
# ==============================

TOKEN = "8847632379:AAGHO2sIusFM_WNNoZlTQ74c7f7cjZZs0N8"

CONTACT_URL = "https://t.me/+HgfeOV-dulE3ZDJk"
SONDAGE_URL = "https://t.me/+jwAgNDcMINphOThk"

API = f"https://api.telegram.org/bot{TOKEN}"


# ==============================
# ENVOYER UNE REQUÊTE TELEGRAM
# ==============================

def telegram(method, data=None):
    response = requests.post(
        f"{API}/{method}",
        json=data or {},
        timeout=30
    )
    return response.json()


# ==============================
# MENU PRINCIPAL
# ==============================

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


# ==============================
# BOUCLE DU BOT
# ==============================

def lancer_bot():

    print("🤖 Guedrofamilly Bot démarré !")
    print("En attente des messages...")

    offset = None

    while True:

        try:

            result = telegram("getUpdates", {
                "offset": offset,
                "timeout": 30
            })

            if not result.get("ok"):
                print("Erreur Telegram :", result)
                time.sleep(5)
                continue

            for update in result.get("result", []):

                offset = update["update_id"] + 1

                # Message reçu
                message = update.get("message")

                if message:

                    chat_id = message["chat"]["id"]
                    texte = message.get("text", "").strip()

                    if texte in ["/start", "/menu"]:
                        afficher_menu(chat_id)

                # Bouton SHOP
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

        except Exception as e:

            print("Erreur :", e)
            time.sleep(5)


# ==============================
# DÉMARRAGE
# ==============================

if __name__ == "__main__":
    lancer_bot()
