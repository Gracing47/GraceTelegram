from pyrogram import Client, filters
import os
from dotenv import load_dotenv

# Laden der Umgebungsvariablen
load_dotenv()

print(os.getenv("API_ID"))
print(os.getenv("API_HASH"))
print(os.getenv("BOT_TOKEN"))


# Initialisiere den Pyrogram-Client
app = Client(
    "airdrop_bot",
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Willkommen zum Celo Airdrop-Bot! Bitte geben Sie Ihre Celo Wallet-Adresse oder Telefonnummer ein, um fortzufahren.")

if __name__ == "__main__":
    app.run()
