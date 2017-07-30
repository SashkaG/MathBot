import telebot
from sympy import sympify
from datetime import datetime
from  telebot import types

# имя бота MathOlBot
bot = telebot.TeleBot('367865312:AAGp7K5J-GyQOc44KdWHAlD_H23H_ev3ASU')


@bot.inline_handler(func=lambda query: True)
def query_text(query):
     try:
          temp = str(query.query).replace("×", "*").replace("÷", "/")
          temp.replace('/math', "")
          expr = sympify(temp)
          otv = expr.evalf()
          otv = str(otv).rstrip("0").rstrip(".")
          r_sum = types.InlineQueryResultArticle(id='1', title="Expression",description="Result: {!s}".format(otv),input_message_content=types.InputTextMessageContent( message_text=temp+" = "+otv))
          bot.answer_inline_query(query.id, [r_sum])
     except:
          pass

@bot.message_handler(content_types=["text"], func=lambda message: True)
def default_test(message):
     try:
          temp = str(message.text).replace("×", "*").replace("÷", "/")
          if not str(message.text).startswith("/math"):
               return
          temp = temp.replace('/math ',"")
          expr = sympify(temp)
          otv = expr.evalf()
          otv = str(otv).rstrip("0").rstrip(".")
          bot.send_message(message.chat.id,temp+" = "+otv)
     except:
          print("err")


if __name__ == '__main__':
    bot.polling(none_stop=True)
