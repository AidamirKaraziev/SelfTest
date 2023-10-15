from time import sleep
import asyncio

import requests
import speedtest

from config import MIN_DOWNLOAD, MIN_UPLOAD, SLEEP_TIME


def get_external_ip():
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


async def check_speed():
    print("START SpeedTest")
    try:
        st = speedtest.Speedtest()
        print("JOB")
        ds = st.download()
        print(ds)
        us = st.upload()
        print(us)
        if int(ds) < int(MIN_DOWNLOAD) or int(us) < int(MIN_UPLOAD):
            return f"""
На сервере: {get_external_ip()}
Загрузка должна быть: {await humansize(int(MIN_DOWNLOAD))}
Отправка должна быть: {await humansize(int(MIN_UPLOAD))}

Загрузка: {await humansize(ds)}
Отправка: {await humansize(us)}""", 0
    except Exception as ex:
        print(f"Не вышло     {ex}")
        sleep(int(SLEEP_TIME))
        return ex, -1


if __name__ == '__main__':
    asyncio.run(check_speed())
