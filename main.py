from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '8016766142:AAHDek2pZwegaPvzcqcj0cSaiH7_qgNzXvw'

def start(update, context):
    update.message.reply_text('Hola, envíame la foto del comprobante de Nequi. No acepto videos ni llamadas.')

def recibir_foto(update, context):
    if update.message.photo:
        update.message.reply_text('Gracias, recibí tu comprobante.')
    else:
        update.message.reply_text('Por favor, envía solo fotos.')

def bloquear_todo(update, context):
    update.message.reply_text('Solo se aceptan fotos de comprobantes. No se permiten videos, audios o llamadas.')

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.photo, recibir_foto))
dp.add_handler(MessageHandler(Filters.video | Filters.voice | Filters.audio | Filters.document | Filters.contact | Filters.location, bloquear_todo))

updater.start_polling()
updater.idle()
