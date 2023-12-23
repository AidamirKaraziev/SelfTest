from time import sleep
import asyncio

import requests
import speedtest

from config import SLEEP_TIME, PERFECT_DOWNLOAD, PERFECT_UPLOAD


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


async def check_speed():
    sum_ds = 0
    sum_us = 0
    norm_download = int(PERFECT_DOWNLOAD) * 0.5
    norm_upload = int(PERFECT_UPLOAD) * 0.5

    print("START SpeedTest")
    try:
        """
        5 раз замерить
        если 1 раз получаем хорошую скорость - то заканчиваем тест.
        если нет - то отправка среднеарифметической скорости.
        """
        n = 5
        for i in range(n):
            st = speedtest.Speedtest(secure=True)  # локально secure - не работает. онлайн надо использовать
            # st = speedtest.Speedtest()
            print("JOB")
            ds = st.download()
            # print("fact ds:", await humansize(int(ds)))
            # print("norm ds:", await humansize(int(norm_download)))
            us = st.upload()
            if ds >= norm_download and us >= norm_upload:
                return None, 1
            else:
                sum_ds += ds
                sum_us += us
                pass
        average_ds = sum_ds / n
        average_us = sum_us / n
        if average_ds < norm_download or average_us < norm_upload:
            return f"""
На сервере: {await get_external_ip()}
DS: {await humansize(average_ds)}
US: {await humansize(average_us)}
Normal DS: {await humansize(int(norm_download))}
Normal US: {await humansize(int(norm_upload))}
""", 0
        else:
            return None, 1
    except Exception as ex:
        print(f"Не вышло     {ex}")
        sleep(int(SLEEP_TIME))
        return ex, -1
