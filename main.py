import asyncio
from aiogram import Bot, types
from config import API_TOKEN, CHANNEL_ID
from self_testing import check_speed


bot = Bot(token=API_TOKEN)


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


async def main():
    while True:
        text, code = await check_speed()
        if code == 0:
            await send_message(CHANNEL_ID, text)
            # break
        if code == 1:
            print("скорость отличная!", text)
            # break

if __name__ == '__main__':
    asyncio.run(main())
