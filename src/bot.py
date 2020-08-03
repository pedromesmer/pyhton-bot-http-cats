# coding: utf-8

import json
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

base_url_cats = 'http://http.cat/'
base_url_dogs = 'http://httpstatusdogs.com/'
token_telegram = json.load(open('./credentials/token-bot-telegram.json', 'r')) # captura o token do arquivo na pasta credentials
requests_http = ["100", "200", "300", "400", "500"]

##
# CommandHandler: Manipula os comandos enviados pelo bot -> /comando
# MessageHandler: Lê as mensagens/texto/midia recebidas pelo telegram
# Filters: Filtra as mensagens do MensageHendle
# Updater: Recebe/envia as atualizações do Telegram
# ##

def start(bot, update):
    responde_mensage = 'Envie /cat ou /dog com a requisição HTTP que deseja informação.\n'
    responde_mensage += 'Exemplo: /cat 200'
    bot.send_message(
        chat_id = update.message.chat_id,
        text = responde_mensage
    )

def cats(bot, update, args):
    print('CAT')
    print(update.message.text)

    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = base_url_cats + args[0]
    )

def dogs(bot, update, args):
    bot.sendPhoto(
        chat_id = update.message.chat_id,
        photo = base_url_dogs + args[0]
    )


def textProcessing(bot, update):
    print('entrou nessa função: ' + update.message.text.lower())        
    
    bot.send_message(
        chat_id = update.message.chat_id,
        text = 'Tente enviar /iniciar'
    )


    return
    # em andamento!
    if ('cat' in update.message.text.lower() ):
        print ('cat')
        bot.sendPhoto(
            chat_id = update.chat.chat_id,
            photo = base_url_cats
        )

    if ('dog' in update.message.text.lower()):
        print('dog')
        bot.sendPhoto(
            chat_id = update.chat.chat_id,
            photo = base_url_dogs
        )


def main():
    updater = Updater(token=token_telegram['token'])
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('iniciar', start)) # ao receber /iniciar
    dispatcher.add_handler(CommandHandler('cat', cats, pass_args=True)) # ao receber /cat 404 -> envia o 404 como argumento
    dispatcher.add_handler(CommandHandler('dog', dogs, pass_args=True)) # ao receber /dog 404 -> envia o 404 como argumento
    # le toda a mensagem e envia pra função de tratamento
    dispatcher.add_handler(
        MessageHandler(Filters.text , textProcessing)
    )

    updater.start_polling() # busca as atualizações
    updater.idle() # bloqueia a aplicação até que um do sinais seja recebida e pare o updater


# configurações iniciais
if __name__ == '__main__':
    print('Token do bot: ' + token_telegram['token'])
    print('Press ctrl + C to exit program\n')
    main()