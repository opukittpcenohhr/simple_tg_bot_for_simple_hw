import asyncio
import logging
import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType

# bot_token = os.environ["bot_token"]
bot_token = "5862274410:AAGpEeQLWgt3gKGkyc-qKE-dqb0PMWHKWWk"

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Welcome to gang, man! I can: /help, /send_228, /send_1337, /send_kek, /send_lol, /spy")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Coolest bot evet, man!")

@dp.message_handler(commands=['send_1337'])
async def process_1337(message: types.Message):
    await message.reply("1337 4eva")

@dp.message_handler(commands=['send_228'])
async def process_228(message: types.Message):
    await message.reply("228 4eva")

@dp.message_handler(commands=['send_kek'])
async def process_kek(message: types.Message):
    await message.reply("Keking all day, dude")

@dp.message_handler(commands=['send_lol'])
async def process_lol(message: types.Message):
    await message.reply("LolIpop it, man")

@dp.message_handler(commands=['spy'])
async def process_spy(message: types.Message):
    await message.reply(f"I am looking for you, {message.from_user.full_name}")

@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    await msg.reply("What a fuck, man?")

if __name__ == '__main__':
    executor.start_polling(dp)
