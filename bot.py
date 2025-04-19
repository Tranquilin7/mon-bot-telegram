from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

# === Dictionnaire des contenus ===
contents = {
    "main_menu": [
        ["💻 Assistance informatique", "assist_info"],
        ["🛡️ Cybersécurité", "cybersec"],
        ["❓ FAQ", "faq"],
        ["💸 Faire un don", "don"],
    ],
    "assist_info": [
        ["📄 Créer un document Word pro", "word_doc"],
        ["📊 Faire une présentation PowerPoint", "ppt"],
        ["🔧 PC lent – solutions", "pc_lent"],
        ["🔥 PC chauffe – que faire ?", "pc_chauffe"],
        ["🔙 Retour au menu", "main_menu"]
    ],
    "cybersec": [
        ["🔐 Astuces pour sécuriser ses données", "secure_data"],
        ["🛑 Reconnaitre arnaques et virus", "detect_virus"],
        ["🔎 Outils d’analyse système", "analyse_sys"],
        ["🔑 Gérer ses mots de passe", "mdp"],
        ["🧠 Bonnes pratiques internet", "bonnes_pratiques"],
        ["🔙 Retour au menu", "main_menu"]
    ],
    "faq": [
        ["💾 Installer un logiciel", "faq_soft"],
        ["🖨️ Problème imprimante", "faq_print"],
        ["⚙️ PC lent, que faire ?", "faq_pc_lent"],
        ["🌡️ Pourquoi mon PC chauffe ?", "faq_pc_chauffe"],
        ["🧼 Libérer de l’espace disque", "faq_disque"],
        ["🖥️ Booster son PC sans matériel", "faq_boost"],
        ["🛡️ Savoir si on a un virus", "faq_virus"],
        ["💽 HDD vs SSD ?", "faq_ssd"],
        ["🔙 Retour au menu", "main_menu"]
    ],
    "don": [
        ["💖 Pourquoi faire un don ?", "don_pourquoi"],
        ["💳 Effectuer un don", "don_lien"],
        ["🤝 Contact partenariat", "don_contact"],
        ["🔙 Retour au menu", "main_menu"]
    ]
}

# === Dictionnaire des réponses ===
responses = {
    "start": "👋 Bienvenue sur le bot d’assistance informatique & cybersécurité !\nChoisis une option ci-dessous :",
    "word_doc": "📝 Pour créer un beau document Word :\n- Utilise les styles\n- Mets des titres clairs\n- Utilise une page de garde\n- N’abuse pas des couleurs\n- Utilise des tableaux pour structurer",
    "ppt": "📊 Pour faire une présentation efficace :\n- Sois simple et visuel\n- Une idée par slide\n- Utilise des icônes et images\n- Sois lisible même à distance",
    "pc_lent": "🐢 Si ton PC est lent :\n1. Nettoie les fichiers inutiles\n2. Désactive les logiciels au démarrage\n3. Utilise CCleaner ou BleachBit\n4. Pense à ajouter un SSD !",
    "pc_chauffe": "🌡️ Ton PC chauffe ?\n- Nettoie la poussière\n- Ne bloque pas les ventilateurs\n- Évite de le poser sur un lit\n- Utilise une base ventilée",
    "secure_data": "🔐 Sécurise tes données :\n- Utilise des mots de passe\n- Chiffre ton disque (BitLocker, VeraCrypt)\n- Fais des sauvegardes régulières",
    "detect_virus": "🛑 Reconnaitre un virus :\n- Popups, lenteur, pubs bizarres\n- Fichiers qui disparaissent\n- Antivirus désactivé seul\n=> Analyse avec Malwarebytes ou Defender",
    "analyse_sys": "🔍 Outils recommandés :\n- Windows Defender\n- Malwarebytes\n- Process Explorer\n- VirusTotal.com",
    "mdp": "🔑 Gestion des mots de passe :\n- Utilise Bitwarden ou KeePassXC\n- Un mot de passe différent par site\n- Active la double authentification (2FA)",
    "bonnes_pratiques": "🧠 Bonnes pratiques internet :\n- Navigateur à jour\n- Extension uBlock Origin\n- Ne partage pas tes infos persos\n- Utilise un VPN sur Wi-Fi public",
    "faq_soft": "💾 Installer un logiciel :\n1. Télécharge depuis le site officiel\n2. Lance le fichier\n3. Suis les étapes\n⚠️ Évite les sites louches",
    "faq_print": "🖨️ Problème imprimante :\n- Vérifie le câble / Wi-Fi\n- Mets à jour le pilote\n- Définis comme imprimante par défaut",
    "faq_pc_lent": "⚙️ Un PC lent ?\n- Nettoyage\n- Supprimer logiciels inutiles\n- Gérer démarrage (msconfig)",
    "faq_pc_chauffe": "🌡️ Surchauffe = poussière + mauvaise ventilation\n=> Nettoie, change la pâte thermique, base ventilée",
    "faq_disque": "🧼 Libérer de l’espace :\n- Supprime gros fichiers\n- Vide la corbeille\n- Utilise WinDirStat ou le nettoyage disque",
    "faq_boost": "🚀 Astuces sans matos :\n- Ferme les apps inutiles\n- Mode performance\n- Supprime animations\n- Nettoyage système",
    "faq_virus": "🛡️ Symptômes d’infection :\n- Lenteurs anormales\n- Programmes bizarres\n- Analyse avec antivirus !",
    "faq_ssd": "💽 HDD = lent / SSD = rapide\n=> Mets un SSD pour booster ton PC !",
    "don_pourquoi": "💖 Ce projet est gratuit, mais les dons aident à :\n- Améliorer le bot\n- Héberger les services\n- Créer plus de contenu",
    "don_lien": "💳 Faire un don :\n- MOMO : +229 0191915091\n- WAVE : +229 0197582070",
    "don_contact": "🤝 Contact pour partenariat : @Tranquilinlebon"
}

def build_menu(key):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text, callback_data=callback)] for text, callback in contents[key]]
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(responses["start"], reply_markup=build_menu("main_menu"))

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data
    if key in contents:
        await query.edit_message_text("Voici les options 👇", reply_markup=build_menu(key))
    elif key in responses:
        await query.edit_message_text(responses[key], reply_markup=build_menu("main_menu"))
    else:
        await query.edit_message_text("Contenu non disponible.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    print("✅ Bot lancé !")
    app.run_polling()
