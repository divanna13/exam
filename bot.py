import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш todo-бот. Введите команду /help для получения списка доступных команд.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Доступные команды:\n/start - Запустить бота\n/add - Добавить задачу\n/list - Список задач\n")

@bot.message_handler(commands=['add'])
def add_task(message):
    bot.reply_to(message, "Введите название задачи:")
    bot.register_next_step_handler(message, process_add_task)

def process_add_task(message):
    title = message.text
    bot.reply_to(message, "Введите описание задачи:")
    bot.register_next_step_handler(message, process_add_task_description, title=title)

def process_add_task_description(message, title):
    description = message.text
    bot.reply_to(message, "Введите дедлайн задачи в формате YYYY-MM-DD HH:MM:")
    bot.register_next_step_handler(message, process_add_task_deadline, title=title, description=description)

def process_add_task_deadline(message, title, description):
    deadline = message.text
    task = Task.objects.create(title=title, description=description, deadline=deadline)
    bot.reply_to(message, f"Задача '{task.title}' добавлена.")
    send_notification(task)

def send_notification(task):
    bot.send_message(TELEGRAM_CHAT_ID, f"Новая задача: {task.title}\nОписание: {task.description}\nДедлайн: {task.deadline}")

@bot.message_handler(commands=['list'])
def list_tasks(message):
    tasks = Task.objects.all()
    if tasks:
        response = "Список задач:\n"
        for task in tasks:
            response += f"ID: {task.id}, Заголовок: {task.title}, Описание: {task.description}, Статус: {task.status}, Дедлайн: {task.deadline}\n"
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Нет задач в списке.")

if __name__ == '__main__':
    TELEGRAM_CHAT_ID = 'MY_TELEGRAM_CHAT_ID'
    bot.polling()