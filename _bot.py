
import telebot, wikipedia, re


bot = telebot.TeleBot ('5836730004:AAFnPkKi78JRFxxsiOg3ckI4wJ4OxbeTQFc')

wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)

        wikitext=ny.content[:500]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break

        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'Википедия такого не знает'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Напиши любое слово, и я поищу его в Wikipedia')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


bot.polling(none_stop=True)

