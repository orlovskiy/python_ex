#!/usr/bin/python3
#encoding:utf-8

__author__ = 'Daniil Orlovskiy'

import os
import re
import sys
import urllib

""" Logpuzzle
На сервере лежит 9 изображений, являющихся частями одного изображения 
(фото дикой природы).

Дан лог файл веб-сервера, в котором среди прочих запросов содеражатся запросы
к этим изображениям. Нужно вытащить из файла url всех изображений и скачать их.
Затем создать файл index.html и собрать с его помощью все изображения в одну
картинку.

Вот что из себя представляет строка лога:
101.237.66.11 - - [05/Jun/2013:10:44:02 +0400] "GET /images/animals_07.jpg HTTP/1.1" 200 13632 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

Замечание: для создания html файла можно использовать самую простую разметку:
<html>
<body>
<img src="img0.jpg"><img src="img1.jpg">...
</body>
</html>

Подсказка: скачать файлы можно двумя способами:

1. Воспользоваться функцией, сохраняющей url по заданному пути file_name:
urllib.request.urlretrieve(url, file_name)

2. Скачать url и сохранить в файле:
import urllib.request
import shutil
...
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

"""


def read_urls(filename):
    """ 
    Возвращает список url изображений из данного лог файла,
    извлекая имя хоста из имени файла (apple-cat.ru_access.log). Вычищает
    дубликаты и возвращает список url, отсортированный по названию изображения.
    """
    log = open(filename,'r')
    log  = log.read()
    img_finder = re.compile(ur'(/images/.*?\.jpg\s)')
    result = img_finder.findall(log)
    img_urls = sorted(set(result))
    img_urls = map(lambda i: "http://apple-cat.ru" + i, img_urls)
    for i in img_urls:
       print i
    return img_urls

def download_images(img_urls, dest_dir):
    """
    Получает уже отсортированный спискок url, скачивает каждое изображение
    в директорию dest_dir. Переименовывает изображения в img0.jpg, img1.jpg и тд.
    Создает файл index.html в заданной директории с тегами img, чтобы 
    отобразить картинку в сборе. Создает директорию, если это необходимо.
    """

    # +++ваш код+++
    os.mkdir(dest_dir)
    img_name_shifter = 0
    for i in img_urls:
        img_name = dest_dir + '/img' + str(img_name_shifter) + '.jpg'
        urllib.urlretrieve(i, os.path.join(os.getcwd(), img_name))
        img_name_shifter += 1
    html = open(dest_dir + '/test.html','w')
    html.write('''<html>
        <body>
        <div>
        ''')
    img_name_shifter = 0
    for i in range(len(img_urls)-2):
        img = '<img src = "' + dest_dir + '/img' + str(img_name_shifter) + '.jpg">'
        html.write(img)
        img_name_shifter += 1
    html.write('''</div>
        </body>
        </html>
        ''')
    
def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()
