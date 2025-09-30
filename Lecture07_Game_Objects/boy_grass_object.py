import random
from operator import truediv

from pico2d import *
import time

# from pygame.examples.go_over_there import balls

delta_time = 0.0
ballcount = 0
#시작
class Ball:
    def __init__(self):
        global ballcount
        self.x = random.randint(0,780)
        self.y = 599
        ballcount+=1
        if ballcount <= 10:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.speed = random.randint(2,25)
    def update(self):
        if self.y > 50:
            self.y -= self.speed
    def draw(self):
        self.image.draw(self.x,self.y)


class Zombie:
    def __init__(self):
        self.x = random.randint(-50,100)
        self.y = 170
        self.frame = random.randint(0, 10)
        self.image = load_image('zombie_run_animation.png')
    def update(self):
        self.frame  = (self.frame + 1) % 10
        self.x += 5
    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0 ,frame_width, frame_height,
                             self.x,self.y,frame_width // 2, frame_height // 2)

class Grass:
    def __init__(self):
        self.image = load_image("grass.png")

    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Boy:

    def __init__(self):
        self.x = random.randint(100,600)
        self.y = 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame =  (self.frame + 1)  % 8
        self.x += 5


# 전역 변수 선언
grass = None
running = True
team = []

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global last_time
    last_time = time.perf_counter()

    global world
    world = []
    grass = Grass()  # 인스턴스 생성
    world.append(grass)
    team = [Boy() for _ in range(11)]
    world+=team
    zombies = [Zombie() for _ in range(11)]
    world+=zombies
    balls = [Ball() for _ in range(20)]
    world+=balls

def update_world():
    global last_time
    global delta_time
    current_time = time.perf_counter()
    delta_time = current_time - last_time
    last_time = current_time
    for obj in world:
        obj.update()
    pass


def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()


open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()

#끝!