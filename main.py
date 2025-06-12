from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Reemplaza 'TU_TOKEN_AQUI' por el token real de tu bot de BotFather
TOKEN = '8016766142:AAHDek2pZwegaPvzcqcj0cSaiH7_qgNzXvw'

def start(update: Update, context: CallbackContext):
    update.message.reply_text('¡Hola! Envíame la foto de tu comprobante Nequi. No acepto llamadas ni videos.')

def handle_photo(update: Update, context: CallbackContext):
    update.message.reply_text('¡Gracias! Recibí tu comprobante.')

def handle_message(update: Update, context: CallbackContext):
    if update.message.video or update.message.video_note:
        update.message.reply_text('❌ No acepto videos.')
    elif update.message.voice or update.message.audio:
        update.message.reply_text('❌ No acepto audios.')
    elif update.message.contact:
        update.message.reply_text('❌ No acepto contactos.')
    elif update.message.location:
        update.message.reply_text('❌ No acepto ubicaciones.')
    elif update.message.document:
        update.message.reply_text('❌ Solo acepto fotos de comprobantes.')
    else:
        update.message.reply_text('✅ Esperando una foto de tu comprobante.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(MessageHandler(Filters.all, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
