import logging
import requests
import json
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from aiogram.utils.markdown import hlink

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
    await message.answer('Напиши мне название песни')


@dp.message_handler(commands = ['help'])
async def start(message: types.Message):
    await message.answer('мне тоже нужна помощь')

@dp.message_handler()
async def getapi(message: types.Message):
    query = 'http://172.19.0.45:8080/get_recommendations?search='+message.text
    ans = requests.get(query)
    res = json.loads(ans.text)
    answer = 'Попробуй послушать вот эти треки:'
    for i in range(9):
        artist = res['tracks'][i]['artists'][0]['name']
        name = res['tracks'][i]['name']
        url = res['tracks'][i]['external_urls']['spotify']
        answer = answer + '\n' + hlink(artist + ' - ' + name, url)
    await message.answer(answer, parse_mode = 'HTML', disable_web_page_preview = True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)