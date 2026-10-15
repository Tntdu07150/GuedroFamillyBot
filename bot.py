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

MINI_APP_URL = "https://guedrofamillybot.onrender.com/app?v=10"

API = f"https://api.telegram.org/bot{TOKEN}"


def telegram(method, data=None):
    return requests.post(
        f"{API}/{method}",
        json=data or {},
        timeout=15
    ).json()


# =========================
# MENU PRINCIPAL (TELEGRAM)
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
            "Choisis une option ci-dessous 👇\n\n"
            "Fais /start pour actualiser l’application menu 📱🤳"
        ),
        "parse_mode": "Markdown",
        "reply_markup": clavier
    })


# =========================
# MINI APP (APPLICATION MENU MODERN GRID)
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
<link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Inter', sans-serif;
    background: #0d0f12;
    color: #ffffff;
    padding-bottom: 90px;
    min-height: 100vh;
}

/* En-tête */
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 15px 20px;
    background: rgba(13, 15, 18, 0.95);
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
    z-index: 100;
    border-bottom: 1px solid rgba(255, 0, 60, 0.2);
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-img {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 2px solid #ff003c;
    object-fit: cover;
    box-shadow: 0 0 10px rgba(255, 0, 60, 0.4);
}

.brand-title {
    font-family: 'Permanent Marker', cursive;
    font-size: 20px;
    color: #ff003c;
    text-shadow: 0 0 8px rgba(255, 0, 60, 0.6);
}

.badge-count {
    background: rgba(255, 0, 60, 0.15);
    border: 1px solid #ff003c;
    color: #ff003c;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
}

/* Barre de filtres catégories */
.filter-bar {
    display: flex;
    gap: 8px;
    padding: 15px 20px;
    overflow-x: auto;
    scrollbar-width: none;
}
.filter-bar::-webkit-scrollbar {
    display: none;
}

.filter-btn {
    background: #161922;
    border: 1px solid #282c37;
    color: #a0a5b5;
    padding: 10px 18px;
    border-radius: 12px;
    font-size: 13px;
    font-weight: 600;
    white-space: nowrap;
    cursor: pointer;
    transition: all 0.2s ease;
}

.filter-btn.active {
    background: linear-gradient(135deg, #ff003c, #b3002d);
    border-color: #ff003c;
    color: #ffffff;
    box-shadow: 0 0 12px rgba(255, 0, 60, 0.4);
}

/* Grille 2 colonnes pour les produits */
.products-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 14px;
    padding: 0 20px;
}

/* Carte Produit */
.card {
    background: #141720;
    border: 1px solid #222634;
    border-radius: 18px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    cursor: pointer;
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.card:active {
    transform: scale(0.97);
    border-color: #ff003c;
}

.card-image-wrap {
    width: 100%;
    height: 160px;
    position: relative;
    background: #000;
}

.card-image-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.tag-badge {
    position: absolute;
    bottom: 8px;
    left: 8px;
    background: rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #fff;
    font-size: 10px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
    text-transform: uppercase;
}

.card-content {
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    flex-grow: 1;
}

.card-title {
    font-size: 14px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.3;
}

.card-sub {
    font-size: 11px;
    color: #8a8f9d;
}

.card-price {
    font-size: 14px;
    font-weight: 800;
    color: #ff003c;
    margin-top: auto;
    padding-top: 6px;
}

/* Modal Vue Détail Produit */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.85);
    backdrop-filter: blur(8px);
    z-index: 200;
    display: none;
    align-items: flex-end;
}

.modal-content {
    background: #141720;
    border-top: 2px solid #ff003c;
    border-radius: 24px 24px 0 0;
    width: 100%;
    max-height: 85vh;
    overflow-y: auto;
    padding: 24px;
    position: relative;
}

.close-btn {
    position: absolute;
    top: 16px;
    right: 16px;
    background: #222634;
    border: none;
    color: #fff;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    font-weight: bold;
    cursor: pointer;
}

.modal-img {
    width: 100%;
    max-height: 220px;
    object-fit: cover;
    border-radius: 16px;
    margin-bottom: 16px;
    border: 1px solid #222634;
}

.modal-title {
    font-size: 20px;
    font-weight: 800;
    color: #fff;
    margin-bottom: 6px;
}

.modal-desc {
    font-size: 13px;
    color: #c0c4d0;
    line-height: 1.5;
    background: #1b1f2b;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 16px;
}

.modal-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

.modal-table th, .modal-table td {
    padding: 10px;
    text-align: left;
    font-size: 13px;
    border-bottom: 1px solid #222634;
}

.modal-table th {
    color: #ff003c;
    font-weight: 700;
}

.btn-order {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #ff003c, #990024);
    color: white;
    text-align: center;
    padding: 14px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 800;
    font-size: 15px;
    box-shadow: 0 0 15px rgba(255, 0, 60, 0.4);
}

/* Barre de Navigation Fixe en Bas */
.navbar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: rgba(13, 15, 18, 0.95);
    backdrop-filter: blur(12px);
    border-top: 1px solid #222634;
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
    z-index: 150;
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    color: #717685;
    font-size: 10px;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
}

.nav-item.active {
    color: #ff003c;
}

.nav-icon {
    font-size: 18px;
}

.hidden {
    display: none !important;
}
</style>
</head>

<body>

<!-- EN-TÊTE -->
<div class="header">
    <div class="brand">
        <img class="logo-img" src="https://raw.githubusercontent.com/Tntdu07150/GuedroFamillyBot/main/4584E461-74CC-44BF-A7C6-28600C22F000.png" alt="Logo">
        <div class="brand-title">Guedrofamilly</div>
    </div>
    <div class="badge-count">2 Produits</div>
</div>

<!-- FILTRES DE CATÉGORIES -->
<div class="filter-bar">
    <button class="filter-btn active" onclick="filtrer('tous', this)">🔥 Tous</button>
    <button class="filter-btn" onclick="filtrer('hash', this)">🧈 Hash</button>
    <button class="filter-btn" onclick="filtrer('weed', this)">🌱 Weed</button>
    <button class="filter-btn" onclick="filtrer('wpff', this)">✅ Wpff</button>
    <button class="filter-btn" onclick="filtrer('festif', this)">🥳 Festif</button>
</div>

<!-- GRILLE DES PRODUITS -->
<div class="products-grid">

    <!-- PRODUIT 1 -->
    <div class="card prod-item hash" onclick="ouvrirModal('modal-porgiuez')">
        <div class="card-image-wrap">
            <img src="https://raw.githubusercontent.com/Tntdu07150/GuedroFamillyBot/main/IMG_2982.jpeg" alt="Dry sift 120u">
            <span class="tag-badge">🏷️ DRY SIFT 120U</span>
        </div>
        <div class="card-content">
            <div class="card-title">Dry sift 120u Porgiuez 🇪🇸</div>
            <div class="card-sub">Ferme / Club Porgiuez</div>
            <div class="card-price">À partir de 8 €</div>
        </div>
    </div>

    <!-- PRODUIT 2 -->
    <div class="card prod-item hash" onclick="ouvrirModal('modal-plasma')">
        <div class="card-image-wrap">
            <img src="https://raw.githubusercontent.com/Tntdu07150/GuedroFamillyBot/main/IMG_3199.jpeg" alt="Plasma Static">
            <span class="tag-badge">⚡ PLASMA STATIC</span>
        </div>
        <div class="card-content">
            <div class="card-title">Plasma Genetic Ferm 👨‍🌾🥇</div>
            <div class="card-sub">Élite Plasma Genetic</div>
            <div class="card-price">À partir de 12 €</div>
        </div>
    </div>

</div>

<!-- MODAL DÉTAILS PRODUIT 1 -->
<div id="modal-porgiuez" class="modal-overlay" onclick="fermerModalSurFond(event, 'modal-porgiuez')">
    <div class="modal-content">
        <button class="close-btn" onclick="fermerModal('modal-porgiuez')">✕</button>
        <img class="modal-img" src="https://raw.githubusercontent.com/Tntdu07150/GuedroFamillyBot/main/IMG_2982.jpeg" alt="Dry sift Porgiuez">
        <div class="modal-title">Dry sift 120u Porgiuez 🇪🇸</div>
        <div class="modal-desc">
            <b>Origine :</b> Ferme / Club Porgiuez<br><br>
            🍊 <b>Terpènes :</b> Goût fruité et sucré très prononcé, note boisée/épicée.<br><br>
            ✨ <b>Texture :</b> Mousseuse, grasse et crémeuse. S'effrite très facilement.
        </div>
        <table class="modal-table">
            <thead>
                <tr><th>Quantité</th><th>Prix Total</th></tr>
            </thead>
            <tbody>
                <tr><td>1g (Détail)</td><td>8 €</td></tr>
                <tr><td>10g</td><td>75 €</td></tr>
                <tr><td>50g</td><td>250 €</td></tr>
                <tr><td>100g</td><td>480 €</td></tr>
            </tbody>
        </table>
        <a href="https://t.me/+HgfeOV-dulE3ZDJk" class="btn-order">🛒 Commander / Contact MP</a>
    </div>
</div>

<!-- MODAL DÉTAILS PRODUIT 2 -->
<div id="modal-plasma" class="modal-overlay" onclick="fermerModalSurFond(event, 'modal-plasma')">
    <div class="modal-content">
        <button class="close-btn" onclick="fermerModal('modal-plasma')">✕</button>
        <img class="modal-img" src="https://raw.githubusercontent.com/Tntdu07150/GuedroFamillyBot/main/IMG_3199.jpeg" alt="Plasma Static">
        <div class="modal-title">Plasma Genetic Ferm 👨‍🌾🥇✅</div>
        <div class="modal-desc">
            <b>Origine :</b> Élite Plasma Genetic Ferm "epg"<br><br>
            👑 <b>Gamme :</b> Ultra Premium réservée aux connaisseurs.<br><br>
            ⚡ <b>Terpènes :</b> Bonbon Zkittlez fruité avec des sous-notes gazeuses.
        </div>
        <table class="modal-table">
            <thead>
                <tr><th>Quantité</th><th>Prix Total</th></tr>
            </thead>
            <tbody>
                <tr><td>1g (Détail)</td><td>12 €</td></tr>
                <tr><td>10g</td><td>120 €</td></tr>
            </tbody>
        </table>
        <a href="https://t.me/+HgfeOV-dulE3ZDJk" class="btn-order">🛒 Commander / Contact MP</a>
    </div>
</div>

<!-- BARRE DE NAVIGATION FIXE EN BAS -->
<div class="navbar">
    <div class="nav-item active">
        <span class="nav-icon">🏠</span>
        <span>Accueil</span>
    </div>
    <a class="nav-item" href="https://t.me/+HgfeOV-dulE3ZDJk">
        <span class="nav-icon">📞</span>
        <span>Contact</span>
    </a>
    <a class="nav-item" href="https://t.me/+mSsjkyjSmVU2M2U8">
        <span class="nav-icon">📦</span>
        <span>Colis</span>
    </a>
    <a class="nav-item" href="https://t.me/+hqu05O8JCl03NzZk">
        <span class="nav-icon">⭐</span>
        <span>VIP</span>
    </a>
</div>

<script>
const tg = window.Telegram.WebApp;
tg.ready();
tg.expand();

function filtrer(cat, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const items = document.querySelectorAll('.prod-item');
    items.forEach(item => {
        if (cat === 'tous' || item.classList.contains(cat)) {
            item.classList.remove('hidden');
        } else {
            item.classList.add('hidden');
        }
    });
}

function ouvrirModal(id) {
    document.getElementById(id).style.display = 'flex';
}

function fermerModal(id) {
    document.getElementById(id).style.display = 'none';
}

function fermerModalSurFond(event, id) {
    if (event.target.classList.contains('modal-overlay')) {
        fermerModal(id);
    }
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
