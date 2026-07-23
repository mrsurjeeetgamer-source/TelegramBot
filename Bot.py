import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

# GitHub Secret se token lega
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return

    if update.message.new_chat_members:
        group_name = update.effective_chat.title

        for member in update.message.new_chat_members:
            welcome_text = f"""
🌸 {member.mention_html()} 🌸

𝐀αנασ 𝐀ρкα 𝐒ωαgαт 𝐇αι 🦋

𝐇αмαяι 🍂 <b>{group_name}</b>

𝐆𝐫𝐨𝐮𝐩 𝐌𝐞𝐢𝐧 𝐀αנ 𝐒𝐞 𝐀αρ

🍂 <b>{group_name}</b>

𝐊α 𝐇ιѕѕα 𝐇αι 🦋
"""

            await update.message.reply_html(welcome_text)


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN GitHub Secret me set nahi hai.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
    )

    print("✅ Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
