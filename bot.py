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

MINI_APP_URL = "https://guedrofamillybot.onrender.com/app?v=15"

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
# MINI APP (APPLICATION MENU MODERN GRID WITH DROPDOWN)
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

/* Zone Filtres avec Menu Déroulant (Volet Dépliant) */
.filter-dropdown-container {
    padding: 15px 20px;
    display: flex;
    gap: 10px;
}

.custom-select-wrap {
    position: relative;
    width: 100%;
}

.category-select {
    width: 100%;
    background: #161922;
    border: 1px solid #282c37;
    color: #ffffff;
    padding: 12px 16px;
    border-radius: 14px;
    font-size: 14px;
    font-weight: 700;
    appearance: none;
    -webkit-appearance: none;
    outline: none;
    cursor: pointer;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    transition: all 0.2s ease;
}

.category-select:focus {
    border-color: #ff003c;
    box-shadow: 0 0 12px rgba(255, 0, 60, 0.4);
}

.select-arrow {
    position: absolute;
    right: 16px;
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none;
    color: #ff003c;
    font-size: 12px;
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
    margin-bottom: 10px;
    border: 1px solid #222634;
}

/* Galerie photos multiples dans le modal */
.modal-gallery {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    margin-bottom: 16px;
    padding-bottom: 4px;
}

.modal-gallery img {
    width: 70px;
    height: 70px;
    object-fit: cover;
    border-radius: 10px;
    border: 1px solid #222634;
    cursor: pointer;
    flex-shrink: 0;
}

