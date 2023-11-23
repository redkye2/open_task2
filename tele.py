"""import telegram

token="6864686536:AAF4eZtm7LUkgKAQkz-BI1uKtxt-R_Ntkh8"
bot = telegram.Bot(token=token)
updates=bot.get_updates()
for u in updates:
    print(u.message['chat']['id'])
"""

#텍스트받기

""" 
import telegram
token="6864686536:AAF4eZtm7LUkgKAQkz-BI1uKtxt-R_Ntkh8"
bot = telegram.Bot(token=token)
chat_id="6531722704"
text='수업이 너무 어려워요'
bot.sendMessage(chat_id=chat_id,text=text)
"""    
    
"""import telegram
token="6864686536:AAF4eZtm7LUkgKAQkz-BI1uKtxt-R_Ntkh8"    
bot = telegram.Bot(token=token)
public_chat_name='@Lee201911977'
id_channel=bot.sendMessage(chat_id=public_chat_name, text="alarm").chat_id
print(id_channel)"""

"""import telegram

token = '6864686536:AAF4eZtm7LUkgKAQkz-BI1uKtxt-R_Ntkh8'
bot = telegram.Bot(token = token)
public_chat_name = '@Lee201911977'
id_channel = bot.sendMessage(chat_id=public_chat_name, text="hi!").chat_id
print(id_channel)"""


#알람 _telegram 버전 13.12

import schedule
import time
import pytz
import datetime
import telegram


def msg():
    token ='telegram-token'
    bot =telegram.Bot(token=token)
    public_chat_name='@Lee201911977'
    id_channel=bot.sendMessage(chat_id=public_chat_name, text="mwssage").chat_id

def job():
    now=datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >=23 or now.hour <=6:
        return
    else:
        msg()
msg()       
schedule.every(30).minutes.do(job)
print("start")
while True:
    schedule.run_pending()
    time.sleep(1)
    
"""
import telegram

print(telegram.__version__)
#텔레그램 python-telegram-bot=20.0a0


import telegram

print(telegram.__version__)
"""
