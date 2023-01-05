import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta
import json
import requests


FONT_SIZE = 50
TEXT_Y_POSITION = 1
TEXT_X_POSITION = 1
Tashkent_UTC = 5 #укажите ваш часовой пояс

def convert_time_to_string(dt):
    dt += timedelta(hours=Tashkent_UTC)
    return f"{dt.hour}:{dt.minute:02}"

def change_img():
    start_time = datetime.utcnow()
    text = convert_time_to_string(start_time)
    row = Image.new('RGBA', (180, 180), "White")# Цвет фона black,white тд
    parsed = ImageDraw.Draw(row)
    font = ImageFont.truetype("HEADPLANE.ttf", FONT_SIZE)#стиль шрифта
    font2 = ImageFont.truetype("HEADPLANE.ttf", 15)
    parsed.text((int(row.size[0]*0.23), int(row.size[1]*0.31)), f'{text}',
                 align="center", font=font, fill=(0, 0, 0))
    parsed.text((45, 110),' Tashkent', # подтекст
                 align="center", font=font2, fill=(0, 0, 0))
    response = json.loads(requests.get("http://cbu.uz/ru/arkhiv-kursov-valyut/json/").content)
    rates_by_code = {}
    for rate in response:
        rates_by_code[rate['Ccy']] = float(rate['Rate'])
    parsed.text((45, 130),f" ${rates_by_code['USD']}", # подтекст
                 align="center", font=font2, fill=(0, 0, 0))

    row.save(f'time.png', "PNG")



if __name__ == '__main__':
    change_img()
