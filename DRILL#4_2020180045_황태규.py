from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')
idle_animation = load_image('idle_animation.png')

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
speed = 5
dx, dy = 0, 0
direction = None
row = -1
running = True
is_moving = False

def handle_events():
    global running, x, y, direction, is_moving

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                direction = 'RIGHT'
                is_moving = True
            elif event.key == SDLK_LEFT:
                direction = 'LEFT'
                is_moving = True
            elif event.key == SDLK_UP:
                direction = 'UP'
                is_moving = True
            elif event.key == SDLK_DOWN:
                direction = 'DOWN'
                is_moving = True
        elif event.type == SDL_KEYUP:
            direction = None
            is_moving = False

while running:
    x += dx * speed
    y += dy * speed

    x = clamp(50, x, TUK_WIDTH - 50)  # 50은 캐릭터의 너비의 절반
    y = clamp(150, y, TUK_HEIGHT - 150)  # 50은 캐릭터의 높이의 절반

    if direction == 'RIGHT' and x < TUK_WIDTH - 50:
        x += 10
        row = 1
    elif direction == 'LEFT' and x > 50:
        x -= 10
        row = 2
    elif direction == 'UP' and y < TUK_HEIGHT - 50:
        y += 10
        row = 0
    elif direction == 'DOWN' and y > 50:
        y -= 10
        row = 3

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if is_moving:
        character.clip_draw(frame * 100, 100 * row, 100, 100, x, y)
        frame = (frame + 1) % 6
    else:
        idle_animation.clip_draw(frame * 170, 0, 170, 170, x, y, 100, 100)
        frame = (frame + 1) % 5

    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    delay(0.05)

close_canvas()
