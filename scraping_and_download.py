import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

image_number = 0        #счетчик для картинок с сайта
storage_number = 1      #счетчик для страниц сайта
url = 'https://zastavok.net/'       #адресс сайта с картинками

for storage in range(1):        #цикл по страницам сайта
    responce = requests.get(f'{url}/{storage_number}', headers = header).text       #отправка запроса на сайт
    soup = BeautifulSoup(responce, 'lxml')      #получение html кода
    block = soup.find('div', class_ = 'block-photo')        #находим блок со всеми фото на сайте
    all_image = block.find_all('div', class_ = 'short_full')        #получаем блок фотографий на сайте

    for image in all_image:         #циклом бежим по блоку кода картинок
        image_link = image.find('a').get('href')        #получаем ссылку картинки
        download_storage = requests.get(f'{url}{image_link}').text    #отправляем запрос на сайт и добавляем ссылку картинки
        download_soup = BeautifulSoup(download_storage, 'lxml')     #получаем код загрузки картинки
        download_block = download_soup.find('div', class_ = 'image_data').find('div', class_ ='block_down')     #ищем в коде ссылку  на скачивание
        result_link = download_block.find('a').get('href')      #получаем ссылку скачать

        #download image
        image_bytes = requests.get(f'{url}{result_link}').content       #отправляем запрос на сайт с добавлением ссылки на скачку изо и получаем содержимое

        with open(f'C:\\Users\\admin\\Desktop\\image\\{image_number}.jpg', 'wb') as file:     #открываем папку на пк
            file.write(image_bytes)         #записываем картинку в папку

        image_number += 1       #итерируем счетчик картинок
        print(f'изображение {image_number}.jpg успешно скачано')

    storage_number += 1     #итерируем счетчик страниц сайта

