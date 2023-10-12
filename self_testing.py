from time import sleep
import asyncio
import socket

import speedtest
from config import MIN_DOWNLOAD, MIN_UPLOAD


async def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    return local_ip


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
        if ds < MIN_DOWNLOAD or us < MIN_UPLOAD:
            return f"""На сервере: {await get_local_ip()}
Загрузка должна быть: {await humansize(MIN_DOWNLOAD)}
Отправка должна быть: {await humansize(MIN_UPLOAD)}

Загрузка: {await humansize(ds)}
Отправка: {await humansize(us)}""", 0
    except Exception as ex:
        print(f"Не вышло     {ex}")
        sleep(10)
        return None, -1
        # raise f"{ex}"
    # if ds < MIN_DOWNLOAD and us < MIN_UPLOAD:
    #     return f"На сервере: {await get_local_ip()} - недостаточная скорость загрузки {await humansize(ds)}" \
    #            f" и отправки {await humansize(us)}"
    # elif ds < MIN_DOWNLOAD:
    #     return f"На сервере: {await get_local_ip()} - недостаточная скорость загрузки {await humansize(ds)}"
    # elif us < MIN_UPLOAD:
    #     return f"На сервере: {await get_local_ip()} - недостаточная скорость отправки {await humansize(us)}"
    # else:


if __name__ == '__main__':
    asyncio.run(check_speed())
