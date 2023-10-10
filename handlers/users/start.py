from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start_no_state(message: Message):
    await message.answer('hello!')


@dp.message_handler(content_types=["document"])
async def sticker_file_id(message: Message):
    if message.document.file_name.endswith('.txt'):
        a = await message.document.download()
        await message.answer(f"Документ успешно скачан. Начинаю парсинг")
        new_lines_count = await document_parsing(a.name)
        await message.answer(f'Допарсил, новы строк: {new_lines_count}')
    else:
        await message.answer("Неверный формат файла. Пожалуйста, отправьте документ в формате .txt")


async def document_parsing(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    new_lines = 0
    for line in lines:
        with open('result.txt', 'a') as res:
            r = open('result.txt').readlines()
            if line not in r:
                print(line)
                res.write(line)
                new_lines += 1
    return new_lines

@dp.message_handler(commands=['document'])
async def send_document(message: Message):
    with open('result.txt', 'rb') as document:
        await message.answer_document(document=document)
