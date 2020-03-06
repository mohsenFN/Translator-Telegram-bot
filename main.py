from googletrans import Translator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start_func(update, context):  
    update.message.reply_text("""سلام \nپیام انگلیسی یا فارسی خود را ارسال کنید.\n/about""")
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
    else:
        transed = Translator().translate(user_text, dest='fa').text
        update.message.reply_text(transed)
def about_func(update, context):
	update.message.reply_text("coder @six_6_six\nchannel @freezed_cash\ngithub github.com/mohsenfn")

updater = Updater("1022302291:AAGeLKKLbWueJEybGF1nzAaQpdegGNnxqdk", use_context=True)
updater.dispatcher.add_handler(CommandHandler("about", about_func))
updater.dispatcher.add_handler(CommandHandler("start", start_func))
updater.dispatcher.add_handler(MessageHandler(Filters.text, trans_func))
print("Running ...")
updater.start_polling()
updater.idle()        
# done  
