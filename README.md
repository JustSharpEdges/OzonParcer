# *OzonParcer*
*Ozon parcer without authentication (limit of review 94)*

# Описание файлов
main.py - основной скрипт, написанный на языке python.
requirements.txt - библиотеки, необходимые для успешного запуска скрипта
yandexdriver - драйвер, необходимый для работы selenium

# Для использования скрипта необходимо:
1. Заменить путь к приложению яндекс браузер <sub> options.binary_location = '/Applications/Yandex.app/Contents/MacOS/Yandex' </sub>
2. Заменить ссылку на необходимый вам товар <sub> product_url = ('https://www.ozon.ru/product/jetgame-sistemnyy-blok-xeon-3060-intel-xeon-e5-2650v2-ram-64-gb-ssd-1024-gb-nvidia-geforce-rtx-3060-1649767704/?advert=AP8ANF2yeFT3QbyI6vzVfPV4zif_NNPUzf4tFbowzv7V2dFYhtqaJkTemq5aMLXT1Gqfa9fRvm3kCtG4eq4QudZheAXSRkhz_LNHGDEtLFZSe9ra6ekNmXpBNWqI9cMlKCrga55Tk29cMBG5udKuWtQR0HION3PwYGv3a0_1j1ATaSjrEzbQbTOYNO7fBwSWbm9H_18uwbs7jAPlxXVa_e4ZPBWAS1qhkK8fxNJ3gPcRGfROMcGmKAUb&avtc=1&avte=2&avts=1732876551' </sub>

3. Изменить название конечного excel фвйла <sub> df.to_excel('OzonReviews.xlsx', index=False, engine='openpyxl') </sub>
