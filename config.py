import os
from pyrogram import Client

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5008408531:AAEpMQCZiF2qnhjLTG0zB10OeS0bEcyXutc")
API_HASH = os.environ.get("API_HASH", "c23db4aa92da73ff603666812268597a")
API_ID = os.environ.get("API_ID", 2374174)
OWNER_ID = os.environ.get("OWNER_ID", "mmagneto")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001580827602"))

STRING_SESSION = os.environ.get('STRING_SESSION', '')
if len(STRING_SESSION) != 0:
    try:
        userbot = Client(
            name='Userbot',
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=STRING_SESSION,
        ) 
        userbot.start()
        me = userbot.get_me()
        userbot.send_message(OWNER_ID, f"Userbot Bașlatıldı..\n\n**Premium Durumu**: {me.is_premium}\n**Ad**: {me.first_name}\n**id**: {me.id}")
        print("Userbot Başlatıldı..")
    except Exception as e:
        print(e)
