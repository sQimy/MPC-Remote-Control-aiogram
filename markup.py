from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnPrevtrack = KeyboardButton('⏮️')
btnPlay = KeyboardButton('⏯️')
btnNexttrack = KeyboardButton('⏭️')
btnVolumeDown = KeyboardButton('🔈')
btnVolumeUp = KeyboardButton('🔊')
btnFullscreen = KeyboardButton('↗️')
btnSuspend = KeyboardButton('Suspend')

playbackControl = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPrevtrack, btnPlay, btnNexttrack, btnVolumeDown, btnVolumeUp, btnFullscreen, btnSuspend)