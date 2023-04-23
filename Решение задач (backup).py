import os
import time

#1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"', 'C:\\Code']
#Заметьте, что для имен, содержащих пробелы, необходимо использовать двойные кавычки внутри строки

#2. Резервные копии должны храниться в основном каталоге резерва
target_dir = 'E:\\Backup' #Подставьте ваш путь

#3. Файлы помещаются в zip-архив
#4. Именем для zip-архива служит текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip - qr {0} {1}".format(target, ' '.join(source))

#Запускаем создание резервной копии
if os.system(zip_command) == 0:
	print('Резервная копия успешно создана в', target)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')

input("\n\nНажмите Enter, чтобы выйти.")

#Мы рассмотрели различные части языка Python, и теперь посмотрим, как все эти части работают вместе, проектируя и составляя программу, которая делает
#что-то полезное. Цель состоит в том, чтобы научиться писать сценарии на языке Python самостоятельно.

#Перед вами стоит следующая задача: составить программу, которая создаёт резервные копии всех наших важных файлов.
#Хотя задача и проста, информации явно недостаточно, чтобы приступать к ее решению. Необходим некоторый дополнительный анализ.
#Например, как вы выбирем, какие файлы необходимо копировать? Как их хранить? Где их хранить?
#После надлежащего анализа мы проектируем нашу программу. Мы создаем список, описывающий то, как наша программа должна работать. В данном случае я создал
#список того, как я себе представляю её работу. Когда вы проектируете программу, у вас может получиться другой результат, поскольку каждый человек 
#представляет себе это по-своему, так что это в порядке вещей.
#1. Файлы и каталоги, которые необходимо скопировать, собираются в список
#2. Резервные копии должны храниться в основном каталоге резерва
#3. Файлы помещаются в zip архив
#4. Именем для zip-архива служит текущая дата и время
#5. Будем использовать стандартную командру zip, имеющуюся по умолчанию в любом стандартном дистрибутиве OS. 
#Пользователи Windows могут установить её со страницы проекта GnuWin32 и добавить в "C:\Program Files\GnuWin32\bin" к системной переменной окружения PATH
#Для этого подойдёт любая команда архивации, если у неё есть интерфейс командной строки, чтобы ей можно было передавать аргументы из нашего сценария