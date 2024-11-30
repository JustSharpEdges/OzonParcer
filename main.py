import time
import pandas as pd
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.binary_location = '/Applications/Yandex.app/Contents/MacOS/Yandex'

driver = webdriver.Chrome(service=Service(executable_path='./yandexdriver'), options=options)

# URL товара на Ozon
product_url = ('https://www.ozon.ru/product/jetgame-sistemnyy-blok-xeon-3060-intel-xeon-e5-2650v2-ram-64-gb-ssd-1024-gb-nvidia-geforce-rtx-3060-1649767704/?advert=AP8ANF2yeFT3QbyI6vzVfPV4zif_NNPUzf4tFbowzv7V2dFYhtqaJkTemq5aMLXT1Gqfa9fRvm3kCtG4eq4QudZheAXSRkhz_LNHGDEtLFZSe9ra6ekNmXpBNWqI9cMlKCrga55Tk29cMBG5udKuWtQR0HION3PwYGv3a0_1j1ATaSjrEzbQbTOYNO7fBwSWbm9H_18uwbs7jAPlxXVa_e4ZPBWAS1qhkK8fxNJ3gPcRGfROMcGmKAUb&avtc=1&avte=2&avts=1732876551')
driver.get(product_url)

print("Ожидаем загрузки страницы...")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
print("Страница загружена!")

# Функция для прокрутки страницы на 500 пикселей
def scroll_page(k):
    driver.execute_script(f"window.scrollTo(0, {k * 500});")


reviews = []
loaded_reviews_count = 0
max_scroll_steps = 560
k = 0  # Счётчик шагов прокрутки

# Флаг для выхода из цикла
stop_script = False

# Выход по кнопке
def listen_for_exit():
    global stop_script
    while not stop_script:
        input_text = input("Введите 'q' для завершения или нажмите Enter, чтобы продолжить: ")
        if input_text.lower() == 'q':  # Если введен 'q', останавливаем скрипт
            stop_script = True
            print("Выход по запросу пользователя.")

# Запуск отслеживания ввода в отдельном потоке
threading.Thread(target=listen_for_exit, daemon=True).start()

# Основной цикл для прокрутки и сбора отзывов
while len(reviews) < 200 and k < max_scroll_steps and not stop_script:
    k += 1
    print(f"Шаг прокрутки {k}... Загружено отзывов: {len(reviews)}")

    scroll_page(k)


    review_blocks = driver.find_elements(By.CSS_SELECTOR, '.rr4_30')  # Поиск блока отзыва

    for review in review_blocks[loaded_reviews_count:]:
        try:
            user_name = review.find_element(By.CSS_SELECTOR, '.wq7_30').text.strip()  # Имя пользователя
        except:
            user_name = 'Без имени'

        try:
            review_date = review.find_element(By.CSS_SELECTOR, '.qz5_30').text.strip()  # Дата отзыва
        except:
            review_date = 'Без даты'

        try:
            rating = len(review.find_elements(By.CSS_SELECTOR, '.a5d23-a0 svg'))  # Количество звёзд
            if rating == 0:
                rating = 'Без рейтинга'
        except:
            rating = 'Без рейтинга'

        try:
            review_text = review.find_element(By.CSS_SELECTOR, '.zq6_30').text.strip()  # Текст отзыва
        except:
            review_text = 'Без текста'


        reviews.append([user_name, review_date, rating, review_text])


    loaded_reviews_count = len(reviews)

    time.sleep(1)


if reviews:
    df = pd.DataFrame(reviews, columns=['User', 'Date', 'Rating', 'Review'])
    df.to_excel('OzonReviews.xlsx', index=False, engine='openpyxl')
    print("Отзывы сохранены в файл OzonReviews.xlsx")
else:
    print("Отзывы не были найдены.")

# Закрытие браузера
driver.quit()

print("Скрипт завершён.")
