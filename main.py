def getToken():
    file=open('TOKEN.txt', 'r')
    TOKEN = file.read()
    print(TOKEN)
    return TOKEN

import os
from turtle import right
import easyocr

import vgamepad as vg

gamepad = vg.VX360Gamepad()

def text_recognition(file_path, text_file_name="result.txt"):
    try:
        reader = easyocr.Reader(["ru", "en"])
        result = reader.readtext(file_path, detail=0, paragraph=True)

        with open(text_file_name, "w") as file:
            for line in result:
                file.write(f"{line}\n\n")

        File = open(text_file_name, 'r')
        content = File.read()

        return content
    except:
        return 'Похоже что произошла ошибка!'


from email import message
from time import sleep
import pyautogui

class Kombat():

    def ShildAnf():
        import random
        for i in range(25):
            r = random.randint(1, 3)
            
            pyautogui.mouseDown(button='right')
            sleep(r)
            pyautogui.mouseUp(button='right')
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')                    

class Elitra():

    def gas():
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right') 

    def eGas():
        f = open('srt.txt', 'r')
        cont = f.read()
        Long = cont.split('|')[0]
        bac = cont.split('|')[1]
        rezult = int(Long) / 100
        if rezult > int(bac):
            return('Топливо мало для такого перелёта')

        else:
            for x in range(int(rezult)):
                sleep(3.46)
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right')                



    def gas_hard():
        for x in range(500):
            sleep(1.5)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')       

    def gas_medium():
        for x in range(500):
            sleep(3.81)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')       

    def gas_eco():
        while True:
            sleep(5.5)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')

def maus_left():
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

def maus_left_loop():
    for x in range(1_000):
        pyautogui.mouseDown(button='left')
        sleep(5)
        pyautogui.mouseUp(button='left')

def maus_right():
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')

def maus_right_sleep():
    pyautogui.mouseDown(button='right')
    sleep(2.5)
    pyautogui.mouseUp(button='right')

def write(content):
    pyautogui.write(content)

def Gas():
    gas = 10_000
    while gas > 0 :
        pyautogui.press('w')
        gas = gas - 1

def get_keyboard_cfg1():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="gas-hard", callback_data="key_hard"),
        types.KeyboardButton(text="gas-medium", callback_data="key_medium"),
        types.KeyboardButton(text="gas-soft", callback_data="ket_soft"),
        types.KeyboardButton(text="gas-eGas", callback_data="ket_egas"),
        types.KeyboardButton(text="gas", callback_data="ket_gas"),
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard_cfg2():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="/gamemode survival", callback_data="key_gm0"),
        types.KeyboardButton(text="/gamemode creative", callback_data="key_gm1"),
        types.KeyboardButton(text="/gamemode spectator", callback_data="key_gm2"),
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard_cfg3():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="boor", callback_data="key_boring"),
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard_cfg4():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="kombat", callback_data="key_shild"),

    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard_cfg5():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="ctrl-a", callback_data="key_ctrl-a"),
        types.KeyboardButton(text="ctrl-c", callback_data="key_ctrl-c"),
        types.KeyboardButton(text="ctrl-v", callback_data="key_ctrl-v"),
        types.KeyboardButton(text="ctrl-x", callback_data="key_ctrl-x"),
        types.KeyboardButton(text="ctrl-z", callback_data="key_ctrl-z"),
        types.KeyboardButton(text="win-r", callback_data="key_win-r"),
        types.KeyboardButton(text="win-tab", callback_data="key_win-tab"),
        types.KeyboardButton(text="win-space", callback_data="key_win-space"),
        types.KeyboardButton(text="left", callback_data="key_left"),
        types.KeyboardButton(text="right", callback_data="key_right"),
        types.KeyboardButton(text="up", callback_data="key_up"),
        types.KeyboardButton(text="down", callback_data="key_down"),
        types.KeyboardButton(text="enter", callback_data="key_enter"),
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard_cfg6():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="q", callback_data="key_q"),
        types.KeyboardButton(text="w", callback_data="key_w"),
        types.KeyboardButton(text="e", callback_data="key_e"),
        types.KeyboardButton(text="r", callback_data="key_r"),
        types.KeyboardButton(text="t", callback_data="key_t"),
        types.KeyboardButton(text="y", callback_data="key_y"),
        types.KeyboardButton(text="u", callback_data="key_u"),
        types.KeyboardButton(text="i", callback_data="key_i"),
        types.KeyboardButton(text="o", callback_data="key_o"),
        types.KeyboardButton(text="p", callback_data="key_p"),

        types.KeyboardButton(text="a", callback_data="key_a"),
        types.KeyboardButton(text="s", callback_data="key_s"),
        types.KeyboardButton(text="d", callback_data="key_d"),
        types.KeyboardButton(text="f", callback_data="key_f"),
        types.KeyboardButton(text="g", callback_data="key_g"),
        types.KeyboardButton(text="h", callback_data="key_h"),
        types.KeyboardButton(text="j", callback_data="key_j"),
        types.KeyboardButton(text="k", callback_data="key_k"),
        types.KeyboardButton(text="l", callback_data="key_l"),
        types.KeyboardButton(text=";", callback_data="key_;"),

        types.KeyboardButton(text="z", callback_data="key_z"),
        types.KeyboardButton(text="x", callback_data="key_x"),
        types.KeyboardButton(text="c", callback_data="key_c"),
        types.KeyboardButton(text="v", callback_data="key_v"),
        types.KeyboardButton(text="b", callback_data="key_b"),
        types.KeyboardButton(text="n", callback_data="key_n"),
        types.KeyboardButton(text="m", callback_data="key_m"),
        types.KeyboardButton(text=",", callback_data="key_,"),
        types.KeyboardButton(text=".", callback_data="key_."),
        types.KeyboardButton(text="/", callback_data="key_/"),
        types.KeyboardButton(text="⌫", callback_data="key_⌫"),
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=8)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard_cfg8_Up():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="Up↕", callback_data="key_UpGamepad"),
            ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard

def get_keyboard_cfg8():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="◄Left", callback_data="key_L-Gamepad"),
        types.KeyboardButton(text="Up↕", callback_data="key_Up-Gamepad"),
        types.KeyboardButton(text="Right►", callback_data="key_R-Gamepad"),
        types.KeyboardButton(text="Down↕", callback_data="key_Down-Gamepad"),
            ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard

def get_keyboard_cfg8_Down():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="Down↕", callback_data="key_UpGamepad"),
            ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard_cfg7():
    # Генерация клавиатуры.
    buttons = [
        types.KeyboardButton(text="spotify", callback_data="key_wb"),
        types.KeyboardButton(text="youtube", callback_data="key_yt"),
        types.KeyboardButton(text="off", callback_data="key_off"),
            ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard

comList = ['/html', '/start', '/hot', '/elitra', '/com', '/boor', '/kombat', '/ocr', '/game', '/elitra_SET']
























from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5447524006:AAHhMCErCFNEAU21AQBOpZUZtCUQj8UVj64')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=["kb"])
async def cmd_numbers(message: types.Message):
    await message.answer("список комманд", reply_markup=get_keyboard_cfg6())

@dp.message_handler(commands=["com"])
async def cmd_numbers(message: types.Message):
    await message.answer("список комманд", reply_markup=get_keyboard_cfg2())

@dp.message_handler(commands=["elitra"])
async def cmd_numbers(message: types.Message):   
    await message.answer("ниже понель упровления газом на элитре", reply_markup=get_keyboard_cfg1())

@dp.message_handler(commands=["elitra_SET"])
async def cmd_numbers(message: types.Message):
    try:
        L = int(message.text.split()[1])
        B = int(message.text.split()[2])
    except IndexError:
        print('BRUH')

    FILE = open('srt.txt', 'w')
    FILE.write(str(L) + '|' + str(B))
    await message.answer("вСЁ ГОТОВО К ПОЛЁТУ")



@dp.message_handler(commands=["hot"])
async def cmd_numbers(message: types.Message):
    await message.answer("эта кнопка начьнёт бурение", reply_markup=get_keyboard_cfg5())

@dp.message_handler(commands=["pan"])
async def cmd_numbers(message: types.Message):
    await message.answer("эта кнопка начьнёт бурение", reply_markup=get_keyboard_cfg7())

@dp.message_handler(commands=["boor"])
async def cmd_numbers(message: types.Message):
    await message.answer("эта кнопка начьнёт бурение", reply_markup=get_keyboard_cfg3())

@dp.message_handler(commands=["kombat"])
async def cmd_numbers(message: types.Message):
    await message.answer("панель для сражений", reply_markup=get_keyboard_cfg4())

@dp.message_handler(commands=["game"])
async def cmd_numbers(message: types.Message):
    await message.answer("панель для сражений", reply_markup=get_keyboard_cfg8())

@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    file_info = await bot.get_file(message.photo[-1].file_id)
    print(message)
    await message.photo[-1].download('file-0.jpg') # ++

    if dict(message).get('caption') == str('/') + 'ocr':

        await message.reply('📊OpenCV октивен, ожидайте...')
        try:
            if text_recognition(file_path='file-0.jpg') != '':
                pyautogui.write(file_path='file-0.jpg')
                await message.reply(text_recognition(file_path='file-0.jpg'))

            else:
                await message.reply('❌OpenCV не смог получить данные с картинки попробуйте вырезать текст❌')
            os.remove('file-0.jpg')
        except:
            if text_recognition(file_path='file-0.jpg') != '':
                pyautogui.write(file_path='file-0.jpg')
                await message.reply(text_recognition(file_path='file-0.jpg'))

            else:
                await message.reply('❌OpenCV не смог получить данные с картинки попробуйте вырезать текст❌')
            os.remove('file-0.jpg')


@dp.callback_query_handler()
async def callbacks_num(call: types.CallbackQuery):
    # Получаем текущее значение для пользователя, либо считаем его равным 0
    # Парсим строку и извлекаем действие, например `num_incr` -> `incr`
    action = call.data.split("_")[1]
    if action == "gm0":
        print('gm0')
        write('/gamemode survival')


    elif action == 'q':
        pyautogui.press('q')

    elif action == 'y':
        pyautogui.press('y')

    elif action == 'e':
        pyautogui.press('e')

    elif action == 'r':
        pyautogui.press('r')

    elif action == 't':
        pyautogui.press('t')

    elif action == 'y':
        pyautogui.press('y')

    elif action == 'u':
        pyautogui.press('u')

    elif action == 'o':
        pyautogui.press('o')

    elif action == 'p':
        pyautogui.press('p')

    elif action == 'a':
        pyautogui.press('a')

    elif action == 's':
        pyautogui.press('s')

    elif action == 'd':
        pyautogui.press('d')

    elif action == 'f':
        pyautogui.press('f')

    elif action == 'g':
        pyautogui.press('g')

    elif action == 'h':
        pyautogui.press('h')

    elif action == 'j':
        pyautogui.press('j')


    elif action == 'k':
        pyautogui.press('k')

    elif action == 'l':
        pyautogui.press('l')

    elif action == ';':
        pyautogui.press(';')

    elif action == 'z':
        pyautogui.press('z')

    elif action == 'x':
        pyautogui.press('x')

    elif action == 'w':
        pyautogui.press('w')

    elif action == 'c':
        pyautogui.press('c')

    elif action == 'v':
        pyautogui.press('v')

    elif action == 'b':
        pyautogui.press('b')

    elif action == 'n':
        pyautogui.press('n')

    elif action == 'm':
        pyautogui.press('m')

    elif action == ',':
        pyautogui.press(',')

    elif action == '.':
        pyautogui.press('.')

    elif action == '/':
        pyautogui.press('/')

    elif action == '⌫':
        pyautogui.press('backspace')






    elif action == "gm1":
        print('gm1')
        write('/gamemode creative')

    elif action == 'ctrl-a':
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')

    elif action == 'ctrl-z':
        pyautogui.keyDown('ctrl')
        pyautogui.press('z')
        pyautogui.keyUp('ctrl')
    
    elif action == 'ctrl-x':
        pyautogui.keyDown('ctrl')
        pyautogui.press('x')
        pyautogui.keyUp('ctrl')

    elif action == 'ctrl-c':
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')

    elif action == 'ctrl-v':
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')

    elif action == 'win-tab':
        pyautogui.keyDown('win')
        pyautogui.press('tab')
        pyautogui.keyUp('win')

    elif action == 'left':
        pyautogui.press('left')

    elif action == 'right':
        pyautogui.press('right')

    elif action == 'up':
        pyautogui.press('up')

    elif action == 'down':
        pyautogui.press('down')

    elif action == 'enter':
        pyautogui.press('enter')

    elif action == 'win-r':
        pyautogui.keyDown('win')
        pyautogui.press('r')
        pyautogui.keyUp('win')

    elif action == 'win-space':
        pyautogui.keyDown('win')
        pyautogui.press('space')
        pyautogui.keyUp('win')
    



    elif action == "Up-Gamepad":
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        gamepad.update()
        sleep(0.05)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        gamepad.update()
        print('Up')


    elif action == "L-Gamepad":
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        gamepad.update()
        sleep(0.05)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        gamepad.update()
        print('L')

    elif action == "R-Gamepad":
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.update()
        sleep(0.05)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.update()
        print('R')

    elif action == "Down-Gamepad":
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        sleep(0.05)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        print('DG')        





    elif action == "gm2":
        print('gm2')
        write('/gamemode spectator')

    elif action == "mleft":
        print('maus left')
        maus_left()

    elif action == "mright":
        print('maus right')
        maus_right()

    elif action == "hard":
        print('hard')
        Elitra.gas_hard()

    elif action == "medium":
        print('medium')
        Elitra.gas_medium()

    elif action == "soft":
        print('soft')
        Elitra.gas_eco()

    elif action == "egas":
        print('egas')
        Elitra.eGas()

    elif action == "gas":
        print('gas')
        Elitra.gas()

    elif action == "shild":
        print('gas')
        Kombat.ShildAnf()

    elif action == "msr":
        print('maus right sleep 2.5 seconds')
        maus_right_sleep()

    elif action == 'boring':
        print('bur start...')
        maus_left_loop()        

    elif action == 'off':
        print('off')
        os.system('shutdown -s')

    elif action == 'wb':
        print('open https://open.spotify.com/collection/tracks')
        import webbrowser as wb
        wb.open('https://open.spotify.com/collection/tracks')

    elif action == 'yt':
        print('open youtube')
        import webbrowser as wb
        wb.open('https://www.youtube.com/')

@dp.message_handler()
async def cmd_numbers(message: types.Message):
    try:
        L = message.text.split(' ')
        #del L[0]
        finL = ' '.join(L)
    except IndexError:
        print('BRUH')

    ms_l = message.text.split(' ')
    if L[0] not in comList:
        pyautogui.write(finL)
        await message.answer("текст введён")
    elif L[0] == '/html':
        try:
            L = message.text.split(' ')
            del L[0]
            finL = ' '.join(L)
        except IndexError:
            print('BRUH')

        file = open('stic.html', 'r')
        stic = file.read()
        stik = stic.split('<cut>')

        ms_l = message.text.split(' ')
        pyautogui.write(stik[0] + finL + stik[1])
        await message.answer("текст введён")



if __name__ == '__main__':
    executor.start_polling(dp)
