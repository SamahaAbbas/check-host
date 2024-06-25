import sys
import argparse
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from src.scripts.methods.iplook import iplook_part
from src.scripts.methods.ping import ping_part
from src.scripts.methods.http import http_part
from src.scripts.methods.tcp import tcp_part
from src.scripts.methods.udp import udp_part
from src.scripts.methods.dns import dns_part

# Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
ALLOWED_ID = 363719626

def start(update, context):
    if update.effective_user.id != ALLOWED_ID:
        update.message.reply_text("Sorry, you're not authorized to use this bot.")
        return
    update.message.reply_text('Welcome! Use /check <IP> to check an IP address.')

def check_ip(update, context):
    if update.effective_user.id != ALLOWED_ID:
        update.message.reply_text("Sorry, you're not authorized to use this bot.")
        return
    if not context.args:
        update.message.reply_text('Please provide an IP address. Usage: /check <IP>')
        return
    
    ip = context.args[0]
    args = argparse.Namespace(target=ip, ping=True)
    ip_address, status = ping_part(args)
    update.message.reply_text(f"IP: {ip_address}\nStatus: {status}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("check", check_ip))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
