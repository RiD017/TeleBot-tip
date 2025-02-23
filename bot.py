import telebot
import time 
BOT_TOKEN=('7554453508:AAFUnJeUcUsMDSWrJe66bFAFpiFBUFIgrwY')
bottele = telebot.TeleBot(BOT_TOKEN)

from telebot import types
      
@bottele.message_handler(commands=['/start' , '/help'])
def startBot(message):
  first_mess = (f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, Hi \n Do you want play in the 'number' game?")
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
  markup.add(button_yes)
  bottele.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@bottele.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Greate! \n Тогда,я расскажу правила нашей игры:Я-Бот,загадываю число,а ты должен при этом,-отгадать загаданное мною число! \n Чтобы тебе не было тяжело буду помогать тебе и говорить о расположение загаданного числа,прям как в игре 'Горячё/Холодно/Тепло'"
        markup = types.InlineKeyboardMarkup()
        #markup.add(types.InlineKeyboardButton("Перейти на сайт", url=""))
        bottele.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        bottele.answer_callback_query(function_call.id)

name = ''
age = 0
@bottele.message_handler(content_types=['text','audio'])
def start(message):
   if message.text == '/reg':
      bottele.send_message(message.from_user.id, "Можешь представиться:")
      bottele.register_next_step_handler(message,get_name)
   else:   
      bottele.send_message(message.from_user.id, "Click /reg")

def get_name(message):
   global name
   name = message.text
   bottele.send_message(message.from_user.id, "Enter your name,please,for start game:")
   bottele.register_next_step_handler(message,get_name)

def get_age(message):
   global age
   while age == 0:
    try:
        age = int(message.next)#проверяем корректность возраста
    except Exception:
       bottele.send_message(message.from_user.id, "Цифрами,please:")
       keyboard = types.InlineKeyboardMarkup() #наша клавиатура
       key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
       keyboard.add(key_yes) #добавляем кнопку в клавиатуру
       key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
       keyboard.add(key_no)
       bottele.send_message(message.from_user.id, reply_markup=keyboard)

#@bottele

@bottele.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        # ...... код сохранения данных, или их обработки
        bottele.send_message(call.message.chat.id, 'Молодец,справился с задачей!: )')   
    elif call.data == "no":
        bottele.send_message(call.message.chat.id, 'Соу сорри, ты не справился с задачей')
        # ...... переспрос
   #bottele.send_message(message.from_user.id)
bottele.infinity_polling() ##необходимо добавить последнюю строчку, которая отвечает за непрерывное продолжение работы бота:
   
      
      





      




                       









