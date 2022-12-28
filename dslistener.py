import asyncio
import configparser
import time
import os
import datetime

try:
	import discord
	import pyfiglet
	from colorama import Fore, init; init()
	from discord.ext import commands

except ImportError:
	print("[!] Не удаётся импортировать модули! Попробуй их установить:\n\npip install discord\npip install pyfiglet\npip install colorama")
	time.sleep(8)
	exit()

bot = commands.Bot(command_prefix="!", help_command=None)

try:
	cfg = configparser.RawConfigParser()
	cfg.read("dslistener_res/config.ini")

	cfg_p = dict(cfg.items("MAIN"))

	token = cfg_p["token"]
	serv = cfg_p["serv"]

except:
	print(Fore.RED + "[!] Не удаётся найти конфиг. Следовательно, данные не могут быть загружены")
	time.sleep(3)
	exit()

@bot.event
async def on_ready():
	print(Fore.CYAN, end="")
	pyfiglet.print_figlet("D S  L i s t e n e r")
	print(f"{Fore.YELLOW}Аккаунт: {Fore.GREEN}{str(bot.user)}\n{Fore.YELLOW}Айди: {Fore.GREEN}{str(bot.user.id)}\n{Fore.YELLOW}Токен: {Fore.GREEN}{str(token)}\n{Fore.RESET}")
	os.system(f"title {str(bot.user)} активен")

@bot.event
async def on_message(message):
	if str(serv) == "0":
		print(f"{Fore.LIGHTGREEN_EX}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]{Fore.LIGHTRED_EX}[{message.guild}(#{message.channel}({message.channel.id}))]{Fore.LIGHTCYAN_EX}[{message.author}({message.author.id})]{Fore.LIGHTMAGENTA_EX}{message.id}:\n {Fore.YELLOW}{message.content} {Fore.CYAN}({message.attachments})\n")

	else:
		if message.guild.id == int(serv):
			print(f"{Fore.LIGHTGREEN_EX}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]{Fore.LIGHTRED_EX}[#{message.channel}({message.channel.id})]{Fore.LIGHTCYAN_EX}[{message.author}({message.author.id})]{Fore.LIGHTMAGENTA_EX}{message.id}:\n {Fore.YELLOW}{message.content} {Fore.CYAN}({message.attachments})\n")

@bot.event
async def on_message_edit(msg, message):
	if str(serv) == "0":
		print(f"{Fore.LIGHTGREEN_EX}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]{Fore.LIGHTRED_EX}[{message.guild}(#{message.channel}({message.channel.id}))]{Fore.LIGHTCYAN_EX}[{message.author}({message.author.id})]{Fore.LIGHTMAGENTA_EX}({message.id}):\n {Fore.YELLOW}{message.content} {Fore.CYAN}({message.attachments})\n")

	else:
		if message.guild.id == int(serv):
			print(f"{Fore.LIGHTGREEN_EX}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]{Fore.LIGHTRED_EX}[#{message.channel}({message.channel.id})]{Fore.LIGHTCYAN_EX}[{message.author}({message.author.id})]{Fore.LIGHTMAGENTA_EX}({message.id}):\n {Fore.YELLOW}{message.content} {Fore.CYAN}({message.attachments})\n")

def main_entry():
	try:
		bot.run(token)

	except Exception as e:
		print(e)
		print(Fore.RED + "[!] Ошибка! Возможно введён неверный токен")
		time.sleep(3)
		exit()

main_entry()

