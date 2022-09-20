import requests

#-----------------------------------------------
#               Telegram Bot
#-----------------------------------------------
'''
    1) install requests module using pip install requests
    2) enter you bot token and bot chat id
    3) call the function with your message as param
    4) boom! your message is delivered
'''
def telegram_bot_sendtext(bot_message):

   bot_token = ''
   bot_chatID = ''
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()

response = telegram_bot_sendtext("Testing Telegram bot")
print(response)
