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
VIPGUEDROFAMILLY_URL = "https://t.me/+hqu05O8JCl03NzZk"

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
                    "text": "⭐ VIP GUEDROFAMILLY",
                    "url": VIPGUEDROFAMILLY_URL
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
# MINI APP
# =========================

@app.route("/app", methods=["GET"])
def mini_app():

    return """
<!DOCTYPE html>
<html lang="fr">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
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
    font-size: 24px;
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
    padding: 20px;
    margin-bottom: 15px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
}

.category:active {
    transform: scale(0.98);
}

.back {
    background: #333;
    text-align: center;
    margin-top: 20px;
}

.hidden {
    display: none;
}

/* Fiche Produit */
.product-card {
    background: #1e1e1e;
    border-radius: 16px;
    padding: 18px;
    border: 1px solid #333;
}

.media-container {
    width: 100%;
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 15px;
    background: #000;
}

.media-container img, .media-container video {
    width: 100%;
    display: block;
    max-height: 250px;
    object-fit: cover;
}

.description {
    font-size: 14px;
    color: #ccc;
    line-height: 1.5;
    margin-bottom: 20px;
}

.badge-soon {
    background: #ffaa00;
    color: #000;
    font-weight: bold;
    padding: 6px 10px;
    border-radius: 8px;
    display: inline-block;
    margin-bottom: 15px;
    font-size: 13px;
}

.price-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

.price-table th, .price-table td {
    padding: 10px 12px;
    text-align: left;
    border-bottom: 1px solid #333;
    font-size: 14px;
}

.price-table th {
    background: #2a2a2a;
    color: #ffb703;
}

.btn-order {
    display: block;
    width: 100%;
    background: #0088cc;
    color: white;
    text-align: center;
    padding: 14px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: bold;
    margin-bottom: 10px;
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

<!-- PAGE PRINCIPALE -->
<div id="page-principale">
    <div class="header">✈️ Guedrofamilly</div>
    <div class="subtitle">Bienvenue 👋</div>
    <div class="container">
        <div class="category" onclick="afficherPage('page-categorie1')">Hash🧈</div>
        <div class="category">Weed🌱</div>
        <div class="category">Wpff✅</div>
        <div class="category">Produit festif 🥳</div>
    </div>
    <div class="footer">Guedrofamilly</div>
</div>

<!-- SOUS-CATÉGORIES HASH -->
<div id="page-categorie1" class="hidden">
    <div class="header">Hash🧈</div>
    <div class="subtitle">Choisis un produit</div>
    <div class="container">
        <div class="category" onclick="afficherPage('produit-mousse')">1-) Mousse de Californie 🇺🇸✅</div>
        <div class="category" onclick="afficherPage('produit-porgiuez')">2-) Dry sift 120u Porgiuez 🇪🇸</div>
        <div class="category" onclick="afficherPage('produit-vss')">3-) Static de ferme/club (VVS) 🥇</div>
        <div class="category back" onclick="afficherPage('page-principale')">⬅️ RETOUR</div>
    </div>
</div>

<!-- PRODUIT 1: Mousse de Californie -->
<div id="produit-mousse" class="hidden">
    <div class="header">Mousse de Californie 🇺🇸✅</div>
    <div class="container">
        <div class="product-card">
            <div class="media-container">
                <img src="https://via.placeholder.com/400x250" alt="Mousse de Californie">
            </div>
            <div class="description">
                <b>Qualité :</b> TOP
            </div>
            <table class="price-table">
                <thead>
                    <tr><th>Quantité</th><th>Prix</th></tr>
                </thead>
                <tbody>
                    <tr><td>Détail</td><td>7 € / g</td></tr>
                    <tr><td>10g</td><td>6.5 € / g</td></tr>
                    <tr><td>20g</td><td>6 € / g</td></tr>
                </tbody>
            </table>
            <a href="https://t.me/+HgfeOV-dulE3ZDJk" class="btn-order">🛒 Commander</a>
        </div>
        <div class="category back" onclick="afficherPage('page-categorie1')">⬅️ RETOUR HASH</div>
    </div>
</div>

<!-- PRODUIT 2: Dry sift 120u Porgiuez -->
<div id="produit-porgiuez" class="hidden">
    <div class="header">Dry sift 120u 🇪🇸</div>
    <div class="container">
        <div class="product-card">
            <div class="media-container">
                <img src="https://via.placeholder.com/400x250" alt="Dry sift Porgiuez">
            </div>
            <div class="description">
                <b>Origine :</b> Ferme / Club Porgiuez 🇪🇸
            </div>
            <table class="price-table">
                <thead>
                    <tr><th>Quantité</th><th>Prix</th></tr>
                </thead>
                <tbody>
                    <tr><td>Détail</td><td>8 € / g</td></tr>
                    <tr><td>10g</td><td>7.5 € / g</td></tr>
                    <tr><td>50g</td><td>250 €</td></tr>
                    <tr><td>100g</td><td>480 €</td></tr>
                </tbody>
            </table>
            <a href="https://t.me/+HgfeOV-dulE3ZDJk" class="btn-order">🛒 Commander</a>
        </div>
        <div class="category back" onclick="afficherPage('page-categorie1')">⬅️ RETOUR HASH</div>
    </div>
</div>

<!-- PRODUIT 3: Static de ferme/club -->
<div id="produit-vss" class="hidden">
    <div class="header">Static de ferme/club 🥇</div>
    <div class="container">
        <div class="product-card">
            <div class="badge-soon">⏳ CE PRODUIT ARRIVE PROCHAINEMENT</div>
            <div class="media-container">
                <img src="https://via.placeholder.com/400x250" alt="Static VSS">
            </div>
            <div class="description">
                <b>Origine :</b> VVS Tanger Farm<br>
                <b>Export :</b> Espagne social club
            </div>
            <table class="price-table">
                <thead>
                    <tr><th>Quantité</th><th>Prix</th></tr>
                </thead>
                <tbody>
                    <tr><td>Détail</td><td>9 € / g</td></tr>
                    <tr><td>10g</td><td>8.5 € / g</td></tr>
                    <tr><td>20g</td><td>8 € / g</td></tr>
                </tbody>
            </table>
            <div class="description" style="margin-bottom:10px;">
                <i>Si plus, venez mp 💬</i>
            </div>
            <a href="https://t.me/+HgfeOV-dulE3ZDJk" class="btn-order">🛒 Commander / Infos MP</a>
        </div>
        <div class="category back" onclick="afficherPage('page-categorie1')">⬅️ RETOUR HASH</div>
    </div>
</div>

<script>
const tg = window.Telegram.WebApp;
tg.ready();
tg.expand();

function afficherPage(idPage) {
    const pages = [
        'page-principale',
        'page-categorie1',
        'produit-mousse',
        'produit-porgiuez',
        'produit-vss'
    ];
    
    pages.forEach(p => {
        document.getElementById(p).classList.add('hidden');
    });
    
    document.getElementById(idPage).classList.remove('hidden');
}
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
