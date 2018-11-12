import random

font = 'Comic Sans MS'
menu_click_sound = 'Sounds/click.wav'
click_sounds = ('Sounds/click1.wav', 'Sounds/click2.wav', 'Sounds/click3.wav')
win_sound = 'Sounds/winning.wav'

def get_random_click_sound():
    sound_number = random.randint(0, len(click_sounds) - 1)
    return click_sounds[sound_number]