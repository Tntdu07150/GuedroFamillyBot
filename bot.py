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
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #0a0a0c;
    color: #e0e0e0;
}

.header {
    padding: 30px 20px 10px;
    text-align: center;
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 1px;
    color: #2ec4b6;
    text-shadow: 0 0 10px rgba(46, 196, 182, 0.4);
}

.subtitle {
    text-align: center;
    color: #888;
    margin-bottom: 25px;
    font-size: 14px;
}

.container {
    padding: 0 20px 30px;
}

.category {
    background: linear-gradient(145deg, #16181d, #111215);
    border: 1px solid #2a2e39;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 15px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    transition: all 0.2s ease;
}

.category:active {
    transform: scale(0.97);
    border-color: #2ec4b6;
}

.back {
    background: #22252e;
    border-color: #333846;
    text-align: center;
    margin-top: 20px;
    color: #aaa;
}

.hidden {
    display: none;
}

/* Fiche Produit */
.product-card {
    background: linear-gradient(145deg, #14161b, #0d0e11);
    border-radius: 18px;
    padding: 20px;
    border: 1px solid #252934;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.7);
}

.media-container {
    width: 100%;
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 18px;
    background: #000;
    border: 1px solid #2a2e39;
}

.media-container img, .media-container video {
    width: 100%;
    display: block;
    max-height: 250px;
    object-fit: cover;
}

.description {
    font-size: 14px;
    color: #bbb;
    line-height: 1.6;
    margin-bottom: 20px;
    background: rgba(255, 255, 255, 0.03);
    padding: 12px;
    border-radius: 10px;
    border-left: 3px solid #ff9f1c;
}

.badge-soon {
    background: linear-gradient(90deg, #ff9f1c, #ffbf69);
    color: #000;
    font-weight: 800;
    padding: 8px 12px;
    border-radius: 8px;
    display: block;
    text-align: center;
    margin-bottom: 15px;
    font-size: 12px;
    letter-spacing: 0.5px;
}

.price-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

.price-table th, .price-table td {
    padding: 12px 14px;
    text-align: left;
    border-bottom: 1px solid #22252e;
    font-size: 14px;
}

.price-table th {
    background: #1c1f26;
    color: #2ec4b6;
    font-weight: bold;
}

.price-table td strong {
    color: #ff9f1c;
    font-size: 15px;
}

.btn-order {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #0088cc, #005580);
    color: white;
    text-align: center;
    padding: 15px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: bold;
    font-size: 16px;
    box-shadow: 0 4px 15px rgba(0, 136, 204, 0.4);
}

.btn-order:active {
    transform: scale(0.98);
}

.footer {
    text-align: center;
    color: #555;
    font-size: 12px;
    margin-top: 30px;
}
</style>
</head>

<body>

<!-- PAGE PRINCIPALE -->
<div id="page-principale">
    <div class="header">✈️ GUEDROFAMILLY</div>
    <div class="subtitle">Menu Officiel 👋</div>
    <div class="container">
        <div class="category" onclick="afficherPage('page-categorie1')">🧈 Hash</div>
        <div class="category">🌱 Weed</div>
        <div class="category">✅ Wpff</div>
        <div class="category">🥳 Produit festif</div>
    </div>
    <div class="footer">Guedrofamilly • 2026</div>
</div>

<!-- SOUS-CATÉGORIES HASH -->
<div id="page-categorie1" class="hidden">
    <div class="header">🧈 HASH</div>
    <div class="subtitle">Sélectionne ton produit</div>
    <div class="container">
        <div class="category" onclick="afficherPage('produit-mousse')">1️⃣ Mousse de Californie 🇺🇸✅</div>
        <div class="category" onclick="afficherPage('produit-porgiuez')">2️⃣ Dry sift 120u Porgiuez 🇪🇸</div>
        <div class="category" onclick="afficherPage('produit-vss')">3️⃣ Static de ferme/club (VVS) 🥇</div>
        <div class="category back" onclick="afficherPage('page-principale')">⬅️ RETOUR</div>
    </div>
</div>

<!-- PRODUIT 1: Mousse de Californie -->
<div id="produit-mousse" class="hidden">
    <div class="header">Mousse de Californie 🇺🇸</div>
    <div class="container">
        <div class="product-card">
            <div class="media-container">
                <img src="https://via.placeholder.com/400x250" alt="Mousse de Californie">
            </div>
            <div class="description">
                <b>Qualité :</b> TOP ⭐️
            </div>
            <table class="price-table">
                <thead>
                    <tr><th>Quantité</th><th>Prix Total</th></tr>
                </thead>
                <tbody>
                    <tr><td>Détail (1g)</td><td><strong>7 €</strong></td></tr>
                    <tr><td>10g</td><td><strong>65 €</strong></td></tr>
                    <tr><td>20g</td><td><strong>120 €</strong></td></tr>
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
                    <tr><th>Quantité</th><th>Prix Total</th></tr>
                </thead>
                <tbody>
                    <tr><td>Détail (1g)</td><td><strong>8 €</strong></td></tr>
                    <tr><td>10g</td><td><strong>75 €</strong></td></tr>
                    <tr><td>50g</td><td><strong>250 €</strong></td></tr>
                    <tr><td>100g</td><td><strong>480 €</strong></td></tr>
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
                    <tr><th>Quantité</th><th>Prix Total</th></tr>
                </thead>
                <tbody>
                    <tr><td>Détail (1g)</td><td><strong>9 €</strong></td></tr>
                    <tr><td>10g</td><td><strong>85 €</strong></td></tr>
                    <tr><td>20g</td><td><strong>160 €</strong></td></tr>
                </tbody>
            </table>
            <div class="description" style="border-left-color: #2ec4b6;">
                <i>Si plus, venez en MP 💬</i>
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
