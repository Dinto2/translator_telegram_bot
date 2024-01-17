# Import dependencies
import logging
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes
from telegram.constants import ParseMode
from telegram import Update
from deep_translator import MyMemoryTranslator
from deep_translator import GoogleTranslator

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

# Possible languages in this case
languages_to_options = {
'/zh': 'zh-CN',
'/en': 'en',
'/es': 'es',
'/de': 'de',
'/it': 'it',
'/pt': 'pt',
'/sv': 'sv',
'/ru': 'ru',
}

# Global variables
text = ''
lang_to_selected = 'es'

# Async functions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="你要什么？")
    
# What language is selected
async def to_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global lang_to
    global languages_to_options
    lang_to_selected = languages_to_options[update.message.text]

# Send the translation via GoogleTranslator
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
        txt = update.message.text
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                      text=GoogleTranslator(source='auto', 
                                      target=lang_to_selected).translate(txt))

if __name__ == '__main__':
    application = ApplicationBuilder().token(YOUR_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    zh_handler = CommandHandler('zh', lenguaje_destino)
    en_handler = CommandHandler('en', lenguaje_destino)
    es_handler = CommandHandler('es', lenguaje_destino)
    de_handler = CommandHandler('de', lenguaje_destino)
    it_handler = CommandHandler('it', lenguaje_destino)
    pt_handler = CommandHandler('pt', lenguaje_destino)
    sv_handler = CommandHandler('sv', lenguaje_destino)
    ru_handler = CommandHandler('ru', lenguaje_destino)
    unknown_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, unknown)

    application.add_handler(zh_handler)
    application.add_handler(en_handler)
    application.add_handler(es_handler)
    application.add_handler(de_handler)
    application.add_handler(it_handler)
    application.add_handler(pt_handler)
    application.add_handler(sv_handler)
    application.add_handler(ru_handler)

    application.add_handler(unknown_handler)

    application.run_polling()
