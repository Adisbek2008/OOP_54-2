import requests
# отправляет HTTP-запросы, тем самым упрощаяет взаимодействие с веб-сайтом

url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    image_url = data['message']
    print("Случайная собака:", image_url)
else:
    print("Ошибка при запросе:", response.status_code)

# Моя программа отправляет Post-запрос, а также получает и выводит JSON-ответ, где мы можем видеть, что сервер получил отправленные данные