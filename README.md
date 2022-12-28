# DSListener

**ENGLISH**
*!! This is self-bot and you have risk to be banned !!*
*!! It's your own risk !!*

This code uses modules: colorama, pyfiglet, discord.py-self
  Installing modules (open cmd and write this commands):
    pip install colorama
    pip install pyfiglet
    pip install discord.py-self
    
Config (dslistener_res/config.ini)
  Token: write here your own token
  Serv: write here server id which you want 'listen', if you want listen all write 0

Features:
  prints message date: [YEAR-MONTH-DAY HOUR:MINUTE:SECOND]
  prints guild name with chat and chat id (if listening all guilds): [GUILD_NAME(#CHANNEL_NAME(CHANNEL_ID))]
  prints chat and chat id (if listening one guild): [#CHANNEL_NAME(CHANNEL_ID)]
  prints user nick with tag and user id: [USERNAME#USERTAG(USERID)]
  prints message id: MESSAGE_ID, or edited message id in brackets: (MESSAGE_ID)
  prints message content: MESSAGE_CONTENT
  prints message attachments list: ([...]), or: ([]), if empty
  prints (on_ready): logo, account token, name with tag, id

[RUSSIAN]
*!! Это селф-бот и у тебя есть риск быть забаненным !!*
*!! Это только твой риск !!*

Для работы этого скрипта нужны модули: colorama, pyfiglet, discord.py-self
  Установка модулей (открой CMD и пиши эти команды):
    pip install colorama
    pip install pyfiglet
    pip install discord.py-self
    
Конфиг (находится по пути dslistener_res/config.ini):
  Token: введи сюда свой токен
  Serv: введи сюда айди сервера, с которого ты хочешь получать сообщения, а если хочешь со всех, то пиши 0
  
Возможности:
  вывод даты сообщения: [ГОД-МЕСЯЦ-ДЕНЬ ЧАС:МИНУТА:СЕКУНДА]
  вывод названия сервера с названием чата и айди чата (если прослушиваются все сервера): [НАЗВАНИЕ_СЕРВЕРА(#НАЗВАНИЕ_КАНАЛА(АЙДИ_КАНАЛА))]
  вывод названия чата и его айди (если прослушивается один сервер): [#НАЗВАНИЕ_КАНАЛА(АЙДИ_КАНАЛА)]
  вывод никнейма и тэга автора и его айди: [НИК#ТЭГ(АЙДИ)]
  вывод айди сообщения: АЙДИ_СООБЩЕНИЯ, а если сообщение изменено, то в скобках: (АЙДИ_СООБЩЕНИЯ)
  вывод содержания сообщения: СОДЕРЖАНИЕ
  вывод списка вложений: ([...]) или ([]) если их нету
  вывод на запуске бота (on_ready): лого, токен аккаунта, имя с тэгом аккаунта и его айди
  
*You can send pull-request and i will check it*
*Ты можешь отправить пулл реквест и я посмотрю его*
