# Это telegramm бот @ShyHelpErrorbot 

Бот парсит информацию со стековерфлоу, в прочем он сам может рассказать   

Запускать его не нужно он залит на heroku и там работает на web hook   

# Для лакального запуска можно:   
Зайдите в папку куда хотите поставит проект   
Введите:   
git clone git@github.com:Drago160/BotReview.git   
cd BotReview   
git checkout dev   
Зайдите в src/config.py и поставьте туда токен вашего бота   
Введите:   
pip install -r requirements.txt   
python3 main.py   

## Для теста бота можно например прописать    
/start - она вас попреветствует   
![Image alt](https://github.com/Drago160/tmprepos/blob/main/start.png)   
Напишите /help - Она подскажет какие команды есть ![Image alt](https://github.com/Drago160/tmprepos/blob/main/help.png)   
/find - она будет ожидвать от вас запроса для поиска на сайте ![Image alt](https://github.com/Drago160/tmprepos/blob/main/question_find1.png)    
Посмотрите какие ответы она для вас нашла ![Image alt](https://github.com/Drago160/tmprepos/blob/main/answer1.png)    
/changerule - Введите если вы хотите изменить число запросов/ответов  ![Image alt](https://github.com/Drago160/tmprepos/blob/main/changes.png)   
1 - вы говорите ей что вам нужно искать ровно 1 запрос   
1 - на каждый запрос нужно смотреть только первые 1 ответа   
- Теперь она будет искать только 1 запрос и 1 ответ на него   

Попробуйте ввести   
find   
TypeError   
![Image alt](https://github.com/Drago160/tmprepos/blob/main/find2.png)   
![Image alt](https://github.com/Drago160/tmprepos/blob/main/answe2.png)   


Мой бот @ShyHelpErrorbot стоит на heroku, приведенного бота так же можно загрузить туда он умный и поймет что он на хероку и будет исправно работать там    

