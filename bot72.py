import telebot
from telebot import types
from telegram import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot('7852929978:AAGxVvbG4ykN_w6760I-m_79ppW5rucWLgg')
DISC = {
    '1': 'Иллюстрация влюблённые мышки на льду была придумана как рождественская картинка для детей',
    '2': 'Рисунок ночи символизирует гармонию между быстротечностью времени и безграничным спокойствием',
}
@bot.message_handler(content_types=['text']) 
def get_text_messages(message):

    if message.text == "Привет":

        bot.send_message(message.chat.id, "Привет, это персональный чат-бот художницы Ольги Ромуальдовны Ионайтис, который поможет вам познакомиться с её творчеством. Вы можете подписаться на социальные сети, купить книги с её иллюстрациями или написать её что-нибудь.")
        web_app = WebAppInfo(url="https://peredreynastya-ui.github.io/Lablnterface2/")
        keyboard = types.InlineKeyboardMarkup()
        # Создаём клавиатуру с Web App кнопкой
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        web_app_button = KeyboardButton(text="Иллюстрации", web_app=web_app)
        keyboard.add(web_app_button)
 # По очереди готовим текст и обработчик для каждого знака зодиака
        button_about = types.InlineKeyboardButton(text='Немного обо мне', callback_data='about_me')
 # И добавляем кнопку на экран
        button_social = types.InlineKeyboardButton(text='Соц сети', callback_data='social_media')
        button_books = types.InlineKeyboardButton(text='Книги с иллюстрациями О.Ионайтис', callback_data='books')
        keyboard.add(button_about, button_social, button_books)
 # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.chat.id, text='Выбери один из вариантов', reply_markup=keyboard)


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
 if call.data == "about_me":
    bot.send_message(call.message.chat.id, "Здравствуйте! Меня зовут Ольга Ионайтис, и я — художник-иллюстратор. Мой мир — это мир сказок, волшебства и детства, воплощенный в красках и линиях." \
    "Я верю, что каждая книга, особенно детская, - это маленькое чудо, и моя задача – помочь этому чуду раскрыться в полной мере. Мне нравится представлять себя той самой маленькой девочкой, которая впервые открывает книгу, затаив дыхание, и погружается в сказочный мир.")
 elif call.data == "social_media":
    bot.send_message(call.message.chat.id, "https://vk.com/id798628944")
 elif call.data == "books":
    bot.send_message(call.message.chat.id, "Ветер в ивах, Таинственный сад, Маленький лорд Фаунтлерой")
# Обработчик для Web App данных
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data
    if data in DISC:
        bot.send_message(message.chat.id, DISC[data])


bot.polling(none_stop=True, interval=0)