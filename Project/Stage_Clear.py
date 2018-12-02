
from pico2d import *
import game_framework
import GamePlay_Stage1
import GamePlay_Stage2


name = "Stage_Clear"
image = None
logo_time=0.0

def enter():
    global image,bgm
    bgm = load_wav('Resource_Bgm\\Stage_Clear.wav')
    bgm.set_volume(64)
    bgm.play()
    image=load_image('Resource_Screen\\Stage_Clear.png')


    pass

def exit():
    global image
    del (image)
    pass

def handle_events():
    events = get_events()


    pass

def draw():
    global image
    clear_canvas()
    image.clip_draw(30, 100, 1020, 1020, 512, 450)
    update_canvas()
    pass

def update():
    global logo_time

    if (logo_time > 5.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(GamePlay_Stage2)
    delay(0.01)
    logo_time += 0.01
    pass


def pause():
    pass


def resume():
    pass







