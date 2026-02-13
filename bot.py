from telethon import TelegramClient, events
from accounts import ACC_MAIN, BOT_MAIN

# Bot client (bot_token), using your app credentials from ACC_MAIN
bot = TelegramClient(
    BOT_MAIN.session,
    ACC_MAIN.api_id,
    ACC_MAIN.api_hash
).start(bot_token=BOT_MAIN.token)


@bot.on(events.NewMessage(pattern=r'^/start$'))
async def start(event):
    await event.respond("Бот запущен. Система вкуса активна.")


if __name__ == "__main__":
    print("Bot is running...")
    bot.run_until_disconnected()
