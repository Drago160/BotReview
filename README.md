# Это telegramm бот @ShyHelpErrorbot 

# Бот парсит информацию со стековерфлоу, в прочем он сам может рассказать   

# Запускать его не нужно он залит на heroku и там работает на web hook   
# Для лакального запуска можно:   
### Зайдите в папку куда хотите поставит проект   
### Введите:   
#### git clone git@github.com:Drago160/BotReview.git   
#### cd BotReview
#### git checkout dev
### Зайдите в src/config.py и поставьте туда токен вашего бота    
### Введите:   
#### python3 main.py   

## Для теста бота можно например прописать   
### /start - она вас попреветствует(Скажет Hello, (Ваше имя в telegramm))   
### Напишите /help - Она подскажет какие команды есть   
### /find - она будет ожидвать от вас запроса для поиска на сайте   
### Введите для примера: TypeError, тогда она найдет для вас информацию на stackoverflow про TypeError   
### /changerule - Введите если вы хотите изменить число запросов/ответов    
### 2 - вы говорите ей что вам нужно искать ровно 2 запроса   
### 2 - на каждый запрос нужно смотреть только первые 2 ответа   
### - Теперь она будет искать только 2 запроса и по 2 ответа на каждый   

## Мой бот @ShyHelpErrorbot стоит на heroku приведенного бота так же можно загрузить туда он умный и поймет что он на хероку и будет исправно работать там    

