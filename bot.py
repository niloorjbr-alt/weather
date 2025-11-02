import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from weather import get_wetter  

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


# ---------- /start command ----------

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        ["اراک", "اردبیل", "ارومیه"],
        ["اصفهان", "اهواز", "ایلام"],
        ["بجنورد", "بندرعباس", "بوشهر"],
        ["تبریز", "تهران", "خرم‌آباد"],
        ["رشت", "زاهدان", "زنجان"],
        ["ساری", "سمنان", "سنندج"],
        ["شهرکرد", "شیراز", "قزوین"],
        ["قم", "کرج", "کرمان"],
        ["کرمانشاه", "گرگان", "مشهد"],
        ["همدان", "یاسوج", "یزد"]
    ]

    for row in buttons:
        markup.add(*[telebot.types.InlineKeyboardButton(text=city, callback_data=city) for city in row])

    bot.send_message(
        message.chat.id,
        f"سلام {message.from_user.first_name} 👋\n 🌤! لطفاً یکی از استان‌ها را انتخاب کن تا دمای هوا را ببینی",
        reply_markup=markup
    )

# 🌡 Respond to button click
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    city_name = call.data.strip()
    data = get_wetter()
    if city_name in data:
        min_temp = data[city_name]["min"]
        max_temp = data[city_name]["max"]
        bot.send_message(call.message.chat.id, f"🌤 وضعیت دمای امروز در {city_name}:\n حداکثر دما :{max_temp}\n حداقل دما : {min_temp} ")
    else:
        bot.send_message(call.message.chat.id, f"❌ نتیجه‌ای برای {city_name} یافت نشد.")
@bot.message_handler(func=lambda message :True)  
def handle_unknown_text(message):
    bot.send_message(message.chat.id , "لطفا یکی از گزینه های داده شده  را انتخاب کنید .")

# ---------- Run the robot----------
print("🤖 ربات فعال شد...")
bot.infinity_polling()