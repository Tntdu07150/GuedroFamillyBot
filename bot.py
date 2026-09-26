import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

CONTACT_URL = "https://t.me/+HgfeOV-dulE3ZDJk"
SONDAGE_URL = "https://t.me/+jwAgNDcMINphOThk"
MINI_APP_URL = "https://guedrofamillybot.onrender.com/app"

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
            ],
            [
                {
                    "text": "📱 MINI APP",
                    "web_app": {
                        "url": MINI_APP_URL
                    }
                }
            ]
        ]
    }

    telegram("sendMessage", {
        "chat_id": chat_id,
        "text": (
            "✈️ *MENU PRINCIPAL*\n\n"
            "Bienvenue sur *Guedrofamilly* 👋\n\n"
            "Choisis une option ci-dessous 👇"
        ),
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# SHOP
# =========================

def menu_shop(chat_id):
    clavier = {
        "inline_keyboard": [
            [
                {
                    "text": "📦 CATÉGORIE 1",
                    "callback_data": "cat1"
                }
            ],
            [
                {
                    "text": "📦 CATÉGORIE 2",
                    "callback_data": "cat2"
                }
            ],
            [
                {
                    "text": "📦 CATÉGORIE 3",
                    "callback_data": "cat3"
                }
            ],
            [
                {
                    "text": "ℹ️ INFORMATIONS",
                    "callback_data": "infos"
                }
            ],
            [
                {
                    "text": "🏠 ACCUEIL",
                    "callback_data": "home"
                }
            ]
        ]
    }

    telegram("sendMessage", {
        "chat_id": chat_id,
        "text": (
            "🛒 *SHOP*\n\n"
            "Bienvenue dans notre boutique 👋\n\n"
            "Choisis une catégorie :"
        ),
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# CATÉGORIE 1
# =========================

def categorie1(chat_id):
    clavier = {
        "inline_keyboard": [
            [
                {
                    "text": "📦 PRODUIT 1",
                    "callback_data": "prod1"
                }
            ],
            [
                {
                    "text": "📦 PRODUIT 2",
                    "callback_data": "prod2"
                }
            ],
            [
                {
                    "text": "⬅️ RETOUR",
                    "callback_data": "shop"
                }
            ]
        ]
    }

    telegram("sendMessage", {
        "chat_id": chat_id,
        "text": "📦 *CATÉGORIE 1*\n\nChoisis un produit :",
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# CATÉGORIE 2
# =========================

def categorie2(chat_id):
    clavier = {
        "inline_keyboard": [
            [
                {
                    "text": "📦 PRODUIT 3",
                    "callback_data": "prod3"
                }
            ],
            [
                {
                    "text": "📦 PRODUIT 4",
                    "callback_data": "prod4"
                }
            ],
            [
                {
                    "text": "⬅️ RETOUR",
                    "callback_data": "shop"
                }
            ]
        ]
    }

    telegram("sendMessage", {
        "chat_id": chat_id,
        "text": "📦 *CATÉGORIE 2*\n\nChoisis un produit :",
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# CATÉGORIE 3
# =========================

def categorie3(chat_id):
    clavier = {
        "inline_keyboard": [
            [
                {
                    "text": "📦 PRODUIT 5",
                    "callback_data": "prod5"
                }
            ],
            [
                {
                    "text": "📦 PRODUIT 6",
                    "callback_data": "prod6"
                }
            ],
            [
                {
                    "text": "⬅️ RETOUR",
                    "callback_data": "shop"
                }
            ]
        ]
    }

    telegram("sendMessage", {
        "chat_id": chat_id,
        "text": "📦 *CATÉGORIE 3*\n\nChoisis un produit :",
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# PRODUITS
# =========================

def produit(chat_id, numero):
    produits = {
        "prod1": (
            "PRODUIT 1",
            "Description du produit 1."
        ),
        "prod2": (
            "PRODUIT 2",
            "Description du produit 2."
        ),
        "prod3": (
            "PRODUIT 3",
            "Description du produit 3."
        ),
        "prod4": (
            "PRODUIT 4",
            "Description du produit 4."
        ),
        "prod5": (
            "PRODUIT 5",
            "Description du produit 5."
        ),
        "prod6": (
            "PRODUIT 6",
            "Description du produit 6."
        )
    }

    nom, description = produits[numero]

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
                    "text": "⬅️ RETOUR",
                    "callback_data": "shop"
                }
            ]
        ]
    }

    telegram("sendMessage", {
        "chat_id": chat_id,
        "text": (
            f"📦 *{nom}*\n\n"
            f"{description}\n\n"
            "Pour plus d'informations, contacte-nous."
        ),
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# INFORMATIONS
# =========================

def informations(chat_id):
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
                    "text": "⬅️ RETOUR AU SHOP",
                    "callback_data": "shop"
                }
            ]
        ]
    }

    telegram("sendMessage", {
        "chat_id": chat_id,
        "text": (
            "ℹ️ *INFORMATIONS*\n\n"
            "Retrouve ici les informations de la boutique.\n\n"
            "Pour toute question, utilise le bouton "
            "« NOUS CONTACTER »."
        ),
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# MINI APP
# =========================

@app.route("/app", methods=["GET"])
def mini_app():
    return """
<!DOCTYPE html>
<html lang="fr">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Guedrofamilly</title>

    <script src="https://telegram.org/js/telegram-web-app.js"></script>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #111;
            color: white;
        }

        .header {
            padding: 25px 20px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
        }

        .subtitle {
            text-align: center;
            color: #aaa;
            margin-bottom: 25px;
        }

        .container {
            padding: 0 20px 30px;
        }

        .category {
            background: #222;
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 15px;
            font-size: 18px;
            font-weight: bold;
            text-align: left;
            border: 1px solid #333;
            cursor: pointer;
        }

        .category:active {
            transform: scale(0.98);
        }

        .footer {
            text-align: center;
            color: #777;
            font-size: 13px;
            margin-top: 25px;
        }

    </style>

</head>

<body>

    <div class="header">
        ✈️ Guedrofamilly
    </div>

    <div class="subtitle">
        Bienvenue dans notre Mini App 👋
    </div>

    <div class="container">

        <div class="category">
            📦 CATÉGORIE 1
        </div>

        <div class="category">
            📦 CATÉGORIE 2
        </div>

        <div class="category">
            📦 CATÉGORIE 3
        </div>

        <div class="category">
            ℹ️ INFORMATIONS
        </div>

        <div class="footer">
            Guedrofamilly
        </div>

    </div>

    <script>

        const tg = window.Telegram.WebApp;

        tg.ready();
        tg.expand();

    </script>

</body>

</html>
"""


# =========================
# PAGE PRINCIPALE
# =========================

@app.route("/", methods=["GET"])
def accueil():
    return "🤖 Guedrofamilly Bot OK"


# =========================
# WEBHOOK TELEGRAM
# =========================

@app.route("/telegram", methods=["POST"])
def recevoir_message():

    update = request.get_json(silent=True) or {}

    # Messages classiques
    message = update.get("message")

    if message:

        chat_id = message["chat"]["id"]

        texte = message.get("text", "").strip()

        if texte in ["/start", "/menu"]:
            menu_principal(chat_id)

    # Boutons inline
    callback = update.get("callback_query")

    if callback:

        telegram("answerCallbackQuery", {
            "callback_query_id": callback["id"]
        })

        chat_id = callback["message"]["chat"]["id"]

        action = callback.get("data")

        if action == "home":
            menu_principal(chat_id)

        elif action == "shop":
            menu_shop(chat_id)

        elif action == "cat1":
            categorie1(chat_id)

        elif action == "cat2":
            categorie2(chat_id)

        elif action == "cat3":
            categorie3(chat_id)

        elif action == "infos":
            informations(chat_id)

        elif action in [
            "prod1",
            "prod2",
            "prod3",
            "prod4",
            "prod5",
            "prod6"
        ]:
            produit(chat_id, action)

    return "OK"


# =========================
# CONFIGURATION WEBHOOK
# =========================

@app.route("/set-webhook", methods=["GET"])
def configurer_webhook():

    webhook_url = "https://guedrofamillybot.onrender.com/telegram"

    resultat = telegram("setWebhook", {
        "url": webhook_url
    })

    return resultat


# =========================
# LANCEMENT
# =========================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
