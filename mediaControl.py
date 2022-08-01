import pyautogui as pg

def playPause():
    #pg.press('space')
    pg.press('playpause')

def Next():
    pg.press('pagedown')

def Previous():
    pg.press('pageup')

def VolumeUp():
    pg.press('up')

def VolumeDown():
    pg.press('down')

def Fullscreen():
    pg.press('f')