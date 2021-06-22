Бот для сохранения информации от сервера mail.ru о рандомных почтовых ящиках в файл JSON

Как это работает:

	* открываем test.py и выбираем нужное количество email-адресов для запроса (n_boxes) и запускаем скрипт;
	
	* test.py забирает рандомно сформированный email-адрес у файла email_generator.py;
	
	* с помощью библиотеки для автоматизации действий веб-браузера Selenium, открываем браузер (chromedriver.exe);
	
	* отправляем на сайт почтового сервиса рандомно сформированный адрес и нажимаем кнопку введения пароля;
	
	* с помощью библиотеки request забираем информацию от сервера;
	
	* с помощью библиотеки beautiful soup достаем из полученной информации данные о почтовом ящике и сохраняем в список;
	
	* после нужного количества итераций отправляем полученный список в файл response_writer.py для сохранения данных в формате JSON
