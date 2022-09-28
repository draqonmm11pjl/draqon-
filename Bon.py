import requests
import telebot
import random
from telebot import types
from time import sleep 
token = input("[~] Token Bot : ")
bot = telebot.TeleBot(token)
call  = types.InlineKeyboardButton(text = "- Start Check Bin ", callback_data = 'sssk')
@bot.message_handler(commands=['start'])
def start(message):
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 1
    Keyy.add(call)
    bot.send_message(message.chat.id, text=f"*Hi Bot Checker Bins\nCheck In : Brazil ðŸ‡§ðŸ‡·\nClick Start Check Bin \nCoded By : @N_Q_G*",parse_mode="markdown",reply_markup=Keyy)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="sssk":
        BIN(call.message)       

def BIN(message):
    h = 0
    k = 0   
    mar = '0123456789'  
    while True:
        bin = str(''.join((random.choice(mar) for i in range(4))))
        req = requests.post ("https://lookup.binlist.net/37"+bin).text
        if '"scheme":"jcb"' in req:
            if '"type":"credit"' in req:
                if '"Brazil"' in req:
                    if "United States of America" in req:
                        h+=1
                        bin_true = f"""
â€¢ Hi New Available Bin âœ…
====================
â€¢ Bin : 37{bin}
â€¢ Country : Null
====================
â€¢ From : @N_Q_G"""
            bot.send_message(message.chat.id, text=bin_true)
        else:
            k+=1
                
        mees = types.InlineKeyboardMarkup(row_width=1)
        trakos = types.InlineKeyboardButton(f" Erorr : {k}",callback_data='jhi')
        buut5 = types.InlineKeyboardButton(f"At : 37{bin}",callback_data='jhi5')
        buut1 = types.InlineKeyboardButton(f"Done : {h}",callback_data='jhi1')        
            
        mees.add(trakos,buut1,buut5)
        bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Cheaker Bins**",parse_mode='markdown',reply_markup=mees)

bot.polling()
