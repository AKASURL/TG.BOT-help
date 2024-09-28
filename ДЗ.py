import telebot

TOKEN = ('7607860872:AAFrjGp7xnkZONY2Q-uleEd9qCbBJnArbA8'
         '')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот введите /help, чтоб узнать, что я умею.')

@bot.message_handler(commands=['help'])
def help_commands(message):
    help_text = ('Список доступных команд: \n'
                 '/start - Приветствие\n'
                 '/help - справка по командам \n\n'
                 'Я могу выполнять различные действие такие как: \n'
                 '- Приветсвие пользователя \n'
                 '- Вывод справочную информацию \n'
                 'В будущем я смогу работать с валютой и новостями!')
    bot.send_message(message.chat.id, help_text)
if __name__=='__main__':
    bot.polling(none_stop=True)