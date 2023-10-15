from time import sleep
import asyncio

import requests
import speedtest

from config import MIN_DOWNLOAD, MIN_UPLOAD, SLEEP_TIME


async def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        data = response.json()
        external_ip = data['ip']
        return external_ip
    except Exception:
        return None


async def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


# TODO сделать вывод в процентном соотношении
async def check_speed():
    print("START SpeedTest")
    try:
        st = speedtest.Speedtest(secure=True)  # локально secure - не работает. онлайн надо использовать
        # st = speedtest.Speedtest()
        print("JOB")
        ds = st.download()
        us = st.upload()
        if int(ds) < int(MIN_DOWNLOAD) or int(us) < int(MIN_UPLOAD):
            return f"""
На сервере: {await get_external_ip()}
Загрузка должна быть: {await humansize(int(MIN_DOWNLOAD))}
Отправка должна быть: {await humansize(int(MIN_UPLOAD))}

Загрузка: {await humansize(ds)}
Отправка: {await humansize(us)}""", 0
        else:
            return None, 1
    except Exception as ex:
        print(f"Не вышло     {ex}")
        sleep(int(SLEEP_TIME))
        return ex, -1
