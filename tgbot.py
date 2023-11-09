import random
import telebot
bot = telebot.TeleBot("6432346117:AAE9K8xlEqf_rhrpn7mdar0OyfEIIpLtk30")

player_ammo = 10
player_health = 100
enemy_ammo = 10
enemy_health = 100
is_player_turn = True

@bot.message_handler(commands=["start"])
def start(message):
    global player_health, enemy_health, is_player_turn
    player_health = 100
    enemy_health = 100
    is_player_turn = True
    bot.send_message(message.chat.id, 'привет это топовый шутер 2023 года, при проигрыше все деньги с карточки списываются, введи /play')

@bot.message_handler(commands=["play"])
def play(message):
    global is_player_turn
    is_player_turn = True
    bot.send_message(message.chat.id, 'начинаем')
    bot.send_message(message.chat.id, "1. атаковать")
    bot.send_message(message.chat.id, "2. защищаться")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global player_health, enemy_health, player_ammo, enemy_ammo, is_player_turn
    if message.text == "1":
        if is_player_turn:
            if player_ammo > 0:
                damage = random.randint(10, 20)
                enemy_health -=damage
                player_ammo -= 1
                bot.send_message(message.chat.id, f"вы атаковали противника и нанесли ему {damage} урона")
                bot.send_message(message.chat.id, f"здоровье противника: {enemy_health} здоровье игрока: {player_health}")
                is_player_turn = False
                check_game_status(message.chat.id)
            else:
                bot.send_message(message.chat.id, "у вас патроны кончились")
        else:
            bot.send_message(message.chat.id, "сейчас не твоя очередь")
    elif message.text == "2":
        if is_player_turn:
            dodge_chance == random.randint(5, 15)
            if dodge_chance == 1:
                bot.send_message(message.chat.id, "ты уклонился")
            else:
                damage = random.randint(5, 15)
                player_health -= damage
                enemy_ammo -= 1
                bot.send_message(message.chat.id, f"противник атаковал вас и нанес {damage} урона")
                bot.send_message(message.chat.id, f"здоровье игрока {player_health}, здоровье противника {enemy_health}")
                is_player_turn = True
                check_game_status(message.chat.id)
        else:
            bot.send_message(message.chat.id, "сейчас не твоя очередь")
    else:
         bot.send_message(message.chat.id, "неверный выбор.")
def check_game_status(chat_id):
    global player_health, enemy_health
    if player_health <= 0 or enemy_health <= 0:
        if player_health > enemy_health:
            bot.send_message(chat_id, "победа, проверь сбербанк милиард там")
        else:
            bot.send_message(chat_id, "-rep ты проиграл и денег тоже на карте нету")

bot.polling()