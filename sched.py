import time
import schedule
from main import pin_markup, bot
from telebot.util import async_dec
# chat_id = -452045393
chat_id = 779917069

# Понедельник
@async_dec()
def monday(data):
    text = f"""🕕Понедельник {data}

Доброе утро 🤗❤️
⭕️  1. <b>(08:30-9:50)</b> <code>Лаб. роботи з фiзики</code> 3-31

⭕️  2. <b>(10:10-11:30)</b> <code>Диф. рiвняння</code> 10-5

⭕️  3. <b>(12:00-13:20)</b> <code>Основи радіоел-ки</code> 10-2
    """
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=pin_markup)
    # print(text)

# Вторник
@async_dec()
def tuesday(data):
    text = f"""🕕Вторник {data}

Доброе утро 🤗❤️
⭕️  1. <b>(08:30-9:50)</b> <code>Фізика</code>

⭕️  2. <b>(10:10-11:30)</b> <code>Диференціальні рівняння</code> https://zoom.us/j/6658815517?pwd=VzlrVEhDQ1drU0FYclBKbUI3SWRpUT09&fbclid=IwAR2T5oTJ0il_uBPudhOkk8mAjj8x3pzZhT5P-hkr1SaNvLD2QZJ3gOIHVt4

⭕️  3. <b>(12:00-13:20)</b> <code>Основи радіоел-ки</code> https://zoom.us/j/96032637094?pwd=UnhEOUNsNFgyMUUzLzhsT0NlR041QT09

⭕️  4. <b>(13:40-15:00)</b> <code>Англійська мова</code> https://us04web.zoom.us/j/5209187779?pwd=djNMMDhjbzNLTXdlcU16ajkzK2dtQT09
    """
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=pin_markup)
    # print(text)

# Среда
@async_dec()
def wednesday(data, week):
    if week == 1:
        text = f"""🕕Среда {data}

Доброе утро 🤗❤️
⭕️  1. <b>(08:30-9:50)</b> <code>Мет.математичної фізики</code> 10-5

⭕️  2. <b>(10:10-11:30)</b> <code>Фiзика</code>

⭕️  3. <b>(12:00-13:20)</b> <code>Тривим. комп. графіка</code> 10-2
        """
    else:
        text = f"""🕕Среда {data}

Доброе утро 🤗❤️
⭕️  2. <b>(10:10-11:30)</b> <code>Фiзика</code>

⭕️  3. <b>(12:00-13:20)</b> <code>Тривим. комп. графіка</code> 10-2
        """
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=pin_markup)
    # print(text)

# Четверг
@async_dec()
def thursday(data, week):
    if week == 1:
        text = f"""🕕Четверг {data}

Доброе утро 🤗❤️
⭕️  1. <b>(08:30-9:50)</b> <code>Основи адміністрування UNIX систем</code>

⭕️  2. <b>(10:10-11:30)</b> <code>Основи радіоелектроніки</code> https://zoom.us/j/91723646230?pwd=Z3Nkd1hlbjdBT3k2OVhydHdrTVEyZz09

⭕️  3. <b>(12:00-13:20)</b> <code>Основи радіоелектроніки</code> https://zoom.us/j/91723646230?pwd=Z3Nkd1hlbjdBT3k2OVhydHdrTVEyZz09

⭕️  4. <b>(13:40-15:00)</b> <code>Методи математичної фізики</code> https://us04web.zoom.us/j/4768912509?pwd=OHpDMi9WYk1QSmo1K280NnFYYTM3QT09
        """
    else:
        text = f"""🕕Четверг {data}

Доброе утро 🤗❤️
⭕️  1. <b>(08:30-9:50)</b> <code>Основи адміністрування UNIX систем</code>

⭕️  2. <b>(10:10-11:30)</b> <code>Основи радіоелектроніки</code> https://zoom.us/j/91723646230?pwd=Z3Nkd1hlbjdBT3k2OVhydHdrTVEyZz09

⭕️  3. <b>(12:00-13:20)</b> <code>Основи радіоелектроніки</code> https://zoom.us/j/91723646230?pwd=Z3Nkd1hlbjdBT3k2OVhydHdrTVEyZz09

⭕️  4. <b>(13:40-15:00)</b> <code>Тривимірна комп'ютерна графіка</code> https://zoom.us/j/94293232790?pwd=bjFTOEFiOHZISUFFandpNFROamVuQT09
        """
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=pin_markup)
    # print(text)

# Пятница
@async_dec()
def friday(data, week):
    if week == 1:
        text = f"""🕕Пятница {data}

Доброе утро 🤗❤️
⭕️  3. <b>(12:00-13:20)</b> <code>Міжфакультетська вибіркова дисципліна №1</code>
        """
    else:
        text = f"""🕕Пятница {data}

Доброе утро 🤗❤️
⭕️  2. <b>(10:10-11:30)</b> <code>Основи адміністрування UNIX систем</code> 10-2

⭕️  3. <b>(12:00-13:20)</b> <code>Міжфакультетська вибіркова дисципліна №1</code>
        """
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=pin_markup)
    # print(text)
    write_week()


def get_week():
    with open("week.txt","r") as file:
        return int(file.read())

def write_week():
    week = get_week()
    with open("week.txt","w") as file:
        if week == 1:
            file.write("2")
        else:
            file.write("1")

schedule.every().monday.at("06:00").do(monday, time.strftime("%d.%m.20%y"))
schedule.every().tuesday.at("11:55").do(tuesday,time.strftime("%d.%m.20%y"))
schedule.every().wednesday.at("06:00").do(wednesday,time.strftime("%d.%m.20%y"), get_week())
schedule.every().thursday.at("06:00").do(thursday,time.strftime("%d.%m.20%y"), get_week())
schedule.every().friday.at("06:00").do(friday,time.strftime("%d.%m.20%y"), get_week())

@async_dec()
def start_loop():
    while  True:
        time.sleep(1)
        schedule.run_pending()