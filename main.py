import telebot
import time
import schedule
import asyncio
from telebot import types
from telebot.util import async_dec

pin_markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Закрепить", callback_data="pin"))

bot = telebot.TeleBot("1186453090:AAHzJtaYruWypR2Wwgg9WUzInvgcDv6y_bY")

@async_dec()
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "pin":
                bot.pin_chat_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,reply_markup=None)

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Закреплено👌")

    except Exception as e:
        print(repr(e))


print('start')

@async_dec()
def main():
	import sched
	sched.start_loop()
	bot.polling()
if __name__ == "__main__":
	main()



