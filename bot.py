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
                    "text": "📱 APPLICATION MENU",
                    "web_app": {
                        "url": MINI_APP_URL
                    }
                }
            ],
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
# MINI APP (APPLICATION MENU)
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
<link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: radial-gradient(circle, #1a1c23 0%, #08090b 100%);
    color: #ffffff;
    min-height: 100vh;
}

/* En-tête avec Logo et Titre */
.brand-header {
    text-align: center;
    padding: 20px 10px 10px;
}

.logo-img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 2px solid #ffffff;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
    object-fit: cover;
}

.header-title {
    font-family: 'Permanent Marker', cursive;
    font-size: 34px;
    color: #ff003c;
    text-shadow: 0 0 10px #ff003c, 0 0 20px #ff003c;
    margin-top: 10px;
    letter-spacing: 2px;
}

/* Sous-titre en Rouge */
.subtitle {
    text-align: center;
    color: #ff003c;
    text-shadow: 0 0 8px rgba(255, 0, 60, 0.6);
    margin-bottom: 25px;
    font-weight: bold;
    font-size: 15px;
}

.container {
    padding: 0 20px 30px;
}

/* Boutons / Catégories (Contours en Blanc) */
.category {
    background: linear-gradient(135deg, #1f232d, #14161d);
    border: 2px solid #ffffff;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 15px;
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    cursor: pointer;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.15);
    transition: all 0.2s ease;
}

.category:active {
    transform: scale(0.97);
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.4);
}

.back {
    background: linear-gradient(135deg, #2e1419, #1a0b0d);
    border-color: #ff003c;
    color: #ff003c;
    text-shadow: 0 0 8px rgba(255, 0, 60, 0.5);
    box-shadow: 0 0 15px rgba(255, 0, 60, 0.2);
    text-align: center;
    margin-top: 20px;
}

.hidden {
    display: none;
}

/* Fiches Produits */
.product-card {
    background: linear-gradient(145deg, #1a1d26, #101218);
    border-radius: 18px;
    padding: 20px;
    border: 2px solid #ffffff;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
}

.media-container {
    width: 100%;
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 18px;
    background: #000;
    border: 1px solid #ffffff;
}

.media-container img, .media-container video {
    width: 100%;
    display: block;
    max-height: 250px;
    object-fit: cover;
}

.description {
    font-size: 14px;
    color: #e0e0e0;
    line-height: 1.6;
    margin-bottom: 20px;
    background: rgba(255, 255, 255, 0.05);
    padding: 12px;
    border-radius: 10px;
    border-left: 4px solid #ffffff;
}

.badge-soon {
    background: linear-gradient(90deg, #ff003c, #ff5e00);
    color: #ffffff;
    font-weight: 800;
    padding: 8px 12px;
    border-radius: 8px;
    display: block;
    text-align: center;
    margin-bottom: 15px;
    font-size: 13px;
    letter-spacing: 0.5px;
    box-shadow: 0 0 10px rgba(255, 0, 60, 0.5);
}

/* Tableau des Prix */
.price-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

.price-table th, .price-table td {
    padding: 12px 14px;
    text-align: left;
    border-bottom: 1px solid #2a2e3d;
    font-size: 14px;
}

/* En-têtes du tableau en ROUGE */
.price-table th {
    background: #12141a;
    color: #ff003c;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(255, 0, 60, 0.5);
}

/* Prix des produits en BLANC */
.price-table td strong {
    color: #ffffff;
    font-size: 16px;
}

.btn-order {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #ff003c, #990024);
    color: white;
    text-align: center;
    padding: 15px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: bold;
    font-size: 16px;
    box-shadow: 0 0 15px rgba(255, 0, 60, 0.5);
}

.btn-order:active {
    transform: scale(0.98);
}

.footer {
    text-align: center;
    color: #666;
    font-size: 12px;
    margin-top: 30px;
}
</style>
</head>

<body>

<!-- LOGO & TITRE PERMANENTS -->
<div class="brand-header">
    <img class="logo-img" src="https://i.ibb.co/L5m4S39/guedro-logo.jpg" alt="Guedrofamilly Logo" onerror="this.src='https://via.placeholder.com/120/000000/ffffff?text=GF'">
    <div class="header-title">Guedrofamilly</div>
</div>

<!-- PAGE PRINCIPALE -->
<div id="page-principale">
    <div class="subtitle">Bienvenue sur le Menu 👋</div>
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
    <div class="subtitle">Sélectionne ton produit 👇</div>
    <div class="container">
        <div class="category" onclick="afficherPage('produit-porgiuez')">1️⃣ Dry sift 120u Porgiuez 🇪🇸</div>
        <div class="category" onclick="afficherPage('produit-vss')">2️⃣ Static de ferme/club (VVS) 🥇</div>
        <div class="category back" onclick="afficherPage('page-principale')">⬅️ RETOUR</div>
    </div>
</div>

<!-- PRODUIT 1: Dry sift 120u Porgiuez -->
<div id="produit-porgiuez" class="hidden">
    <div class="container">
        <div class="product-card">
            <div class="media-container">
                <img src="https://via.placeholder.com/400x250" alt="Dry sift Porgiuez">
            </div>
            <div class="description">
                <b>Produit :</b> Dry sift 120u 🇪🇸<br>
                <b>Origine :</b> Ferme / Club Porgiuez
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
            <div class="description">
                <i>Si plus, venez en MP 💬</i>
            </div>
            <a href="https://t.me/+HgfeOV-dulE3ZDJk" class="btn-order">🛒 Commander / Infos MP</a>
        </div>
        <div class="category back" onclick="afficherPage('page-categorie1')">⬅️ RETOUR HASH</div>
    </div>
</div>

<!-- PRODUIT 2: Static de ferme/club -->
<div id="produit-vss" class="hidden">
    <div class="container">
        <div class="product-card">
            <div class="badge-soon">⏳ CE PRODUIT ARRIVE PROCHAINEMENT</div>
            <div class="media-container">
                <img src="https://via.placeholder.com/400x250" alt="Static VSS">
            </div>
            <div class="description">
                <b>Produit :</b> Static de ferme/club 🥇<br>
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
            <div class="description">
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
