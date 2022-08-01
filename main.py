import pyautogui as pg



#pyautogui.press('playpause')
func = pg.prompt(text='whith multimedia u want', title='Func' , default='func')
print(f'Entered text: {func}')
print(pg.KEYBOARD_KEYS)



def multimedia(text):
    pg.press(f'{text}')
    print(f'{text} func was used')


if __name__=='__main__':
    multimedia(func)
