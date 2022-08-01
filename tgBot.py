from aiogram import Bot, Dispatcher, executor, types
import sys
import markup as navigation
import mediaControl
from settings import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ah shit, here we go again', reply_markup=navigation.playbackControl)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '⏮️':
        await bot.send_message(message.from_user.id, 'Мотаю назад...')
        mediaControl.Previous()
    elif message.text == '⏯️':
        await bot.send_message(message.from_user.id, 'Play/Pause')
        mediaControl.playPause()
    elif message.text == '⏭️':
        await bot.send_message(message.from_user.id, 'Мотаю вперед...')
        mediaControl.Next()
    elif message.text == '🔈':
        await bot.send_message(message.from_user.id, 'Убавил')
        mediaControl.VolumeDown()
    elif message.text == '🔊':
        await bot.send_message(message.from_user.id, 'Прибавил')
        mediaControl.VolumeUp()
    elif message.text == '↗️':
        await bot.send_message(message.from_user.id, 'Полное погружение')
        mediaControl.Fullscreen()
    elif message.text == 'Suspend':
        await bot.send_message(message.from_user.id, 'Пажожда, не надо...')
        await bot.send_message(message.from_user.id, '🥺')
        sys.exit()
    else:
        await message.reply('Всё')

    

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
