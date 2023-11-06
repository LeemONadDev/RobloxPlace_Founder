import requests #импортируем модуль requests для отправки запросов
import simple_file_db as sfdb #импортируем модуль для работы с бд

sfdb.make_db_dir("db")       #создаем папку с названием db

counter = 100000 #создаем переменную counter. это наша стартовая точка, откуда мы начинаем сканирование плейсов (рекомендованное значение: 1000)
request_url = "https://roblox.com/games/" #переменная, в которой мы храним url плейсов

while 1:
    temp = request_url + str(counter) #создаем переменную temp в которой соединяем значение counter (счетчика) и request_url
    r = requests.get(temp)      #отправляем запрос

    if r.status_code == 200:                                    #проверяем статус запроса. если статус запроса (ответ) имеет код 200, значит плейс найден!
        print("id:",counter,"place founded")                    #выводим id плейса в консоль
        sfdb.write_string_to_db("places.txt",temp,end=" ")      #записываем url в наш файл. все ссылки разделяются пробелами (чтобы потом через split запихнуть их в массив)
    else:
        pass                                                    #плейс не найден, ничего не делаем
        
    counter += 1                                                #увеличиваем счетчик на +1