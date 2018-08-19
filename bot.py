#PYTHON SOURCE CODE v-4 By VrozAnims
#----------------------------------------------------------------------- 
#
#Please install python-telegram-bot modules first!
#htps://github.com/python-telegram-bot/python-telegram-bot
#
#-----------------------------------------------------------------------
#Script Bot v1:
#-First Release!
#-added response function for example
#-added polling system
#-added logging for handle error
#-added dispatcher for handle message
#
#Script Bot v2:
#-remake syntax code for good looking to read
#-added some explain about how-it-work?
#-added started bot message
#-added checking tokenbot
#-added checking module for handle import error
#
#Script Bot v3:
#-Added Debug Mode! For helping testing bot in polling
#-remake started bot message
#-added Bot Name for identity
#-added import run_async for handle multiple request from users (If we don't use this, will be big BUG!)
#-added webhook syntax for Heroku (Another Web Hosting Coming Soon!)
#
#Sript Bot v4:
#-Debug mode removed
#-redesign syntax
#####################################################################################################################

#Importing Modules
try:
	import telegram, logging, os
	from telegram.ext import Updater, CommandHandler
	from telegram.ext.dispatcher import run_async
except ImportError as e:
	print("Problem: ",e)
	exit()

#Bot Data (Please insert bot token here!)
namebot = 'CHALEE'
verbot  = 'v4' #<== You can change this version with your real bot version
tokenbot= '581681521:AAF6yOAMQg_QigP77XkxjT4ugzCUElDfzX8' #<-- Put your bot token here!

#polling setup

updater= Updater(tokenbot)


#webhook setup
#
#Webhook(Heroku):
#-------------------------------

#handling command
dispatcher = updater.dispatcher

#logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#tambahan

vip_access = [297620679, 340639887]

#####################################################################################################################
#COMMAND
#####################################################################################################################

@run_async
def start(bot, update):
	msg= "Halo, kakak.. ada apa? ^_^"
	bot.send_message(chat_id=update.message.chat_id, text=msg)
	if update.message.chat_id > 0 :
		msg+= "["+update.effective_user.username+": "+str(update.message.chat_id)+"]"
		for i in (0, len(vip_access)-1):
			bot.send_message(chat_id=vip_access[i], text=msg)
		return
	elif update.message.chat_id < 0:
		msg+= "["+str(update.message.chat_id)+"]"
		for i in (0, len(vip_access)-1):
			bot.send_message(chat_id=vip_access[i], text=msg)
		return

@run_async
def grup_id(bot, update):
	msg = "*GRUP CHAT ID*\n"
	msg+= "--------------------\n"
	msg+= "chat id: "+str(update.message.chat_id)
	for i in vip_access:
		bot.send_message(chat_id=vip_access[i], text=msg, parse_mode=telegram.ParseMode.MARKDOWN)

@run_async
def kirim_pesan(bot, update, args):
	if update.message.chat_id not in vip_access:
		return
	chati = int(args[0])
	pesan = ' '.join(args[1:])
	bot.send_message(chat_id=chati, text=pesan)


#####################################################################################################################

#configure command
start_handler = CommandHandler('start', start)
kirim_handler = CommandHandler('kirim', kirim_pesan, pass_args=True)
grup_handler  = CommandHandler('grupid', grup_id)

#####################################################################################################################

#set command

dispatcher.add_handler(start_handler)
dispatcher.add_handler(kirim_handler)
dispatcher.add_handler(grup_handler)

#####################################################################################################################

#start polling
#print(namebot,' ',verbot,' : Start!')
#updater.start_polling()
PORT = int(os.environ.get('PORT', '5000'))
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=tokenbot)
#
updater.bot.set_webhook("https://agile-sands-57113.herokuapp.com/" + tokenbot)
#--------------------------------
updater.idle() #untuk menjalankan heroku webhook

#####################################################################################################################
#FOR MORE INFORMATION, CHECK htps://github.com/python-telegram-bot/python-telegram-bot
