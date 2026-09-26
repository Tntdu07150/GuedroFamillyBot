import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# =========================
# LIENS
# =========================

SHOP_URL = "https://t.me/+vLsDOxqSwAM1Njhk"
CONTACT_URL = "https://t.me/+HgfeOV-dulE3ZDJk"
LOCALISATION_URL = "https://t.me/+RvPIBlR9YaczMTA0"
COLIS_URL = "https://t.me/+mSsjkyjSmVU2M2U8"
SONDAGE_URL = "https://t.me/+jwAgNDcMINphOThk"

# Mini App
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
                    "text": "📦 COLIS EN LIVRAISON",
                    "url": COLIS_URL
                }
            ],

            [
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
<!-- ========================= -->

<!-- CATÉGORIE 1 -->

<!-- ========================= -->

<div id="page-categorie1" class="hidden">

    <div class="header">

        📦 CATÉGORIE 1

    </div>

    <div class="subtitle">

        Choisis une sous-catégorie

    </div>

    <div class="container">

        <div class="category">

            📦 SOUS-CATÉGORIE 1

        </div>

        <div class="category">

            📦 SOUS-CATÉGORIE 2

        </div>

        <div class="category">

            📦 SOUS-CATÉGORIE 3

        </div>

        <div class="category">

            📦 SOUS-CATÉGORIE 4

        </div>

        <div

            class="category back"

            onclick="retourAccueil()"

        >

            ⬅️ RETOUR

        </div>

    </div>

</div>

<script>

const tg = window.Telegram.WebApp;

tg.ready();

tg.expand();

function ouvrirCategorie1() {

    document.getElementById(

        "page-principale"

    ).classList.add("hidden");

    document.getElementById(

        "page-categorie1"

    ).classList.remove("hidden");

}

function retourAccueil() {

    document.getElementById(

        "page-categorie1"

    ).classList.add("hidden");

    document.getElementById(

        "page-principale"

    ).classList.remove("hidden");

}

</script>

</body>

</html>

"""

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
    padding: 28px 20px 10px;
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
    border: 1px solid #333;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 15px;
    font-size: 18px;
    font-weight: bold;
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
    Bienvenue 👋
</div>

<div class="container">

    <div class="category">
        🛒 MENU / SHOP
    </div>

    <div class="category">
        Hash🧈
    </div>

    <div class="category">
        Weed🌱
    </div>

    <div class="category">
        Wpff✅
    </div>

    <div class="category">
        Produit festif🎉
    </div>

</div>

<div class="footer">
    Guedrofamilly
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
# PAGE TEST
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

    message = update.get("message")

    if message:

        chat_id = message["chat"]["id"]

        texte = message.get("text", "").strip()

        if texte in ["/start", "/menu"]:

            menu_principal(chat_id)

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
