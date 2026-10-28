import os
import telebot

TOKEN = os.getenv('BOT_TOKEN', '9211513762:AAHAxYvMzSuIUT50hT8UxKK4g1hvoea2laI')
bot = telebot.TeleBot(TOKEN)

global_messages_memory = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! You can start sending text phrases now.")

@bot.message_handler(func=lambda message: True)
def check_and_reply(message):
    user_text = message.text.strip()
    
    if user_text in global_messages_memory:
        return
    else:
        global_messages_memory.add(user_text)
        bot.reply_to(message, user_text)

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
