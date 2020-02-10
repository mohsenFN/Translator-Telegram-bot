from googletrans import Translator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

start_text = open('start_text.txt', 'r', encoding='utf8').read()

def start_func(update, context):  
    update.message.reply_text("""سلام \nپیام انگلیسی یا فارسی خود را ارسال کنید.""")
    print('Start REQ from {}'.format(update.message.from_user.first_name))
    
def trans_func(update, context):
    user_text = update.message.text
    lang = Translator().detect(user_text).lang
   
    if lang == 'fa':
        transed = Translator().translate(user_text, dest='en').text
        update.message.reply_text(transed)
    elif lang == 'en':
        transed = Translator().translate(user_text, dest='fa').text
        update.message.reply_text(transed)

updater = Updater("Bot's Token", use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start_func))
updater.dispatcher.add_handler(MessageHandler(Filters.text, trans_func))
print("Running ...")
updater.start_polling()
updater.idle()        
# done  
