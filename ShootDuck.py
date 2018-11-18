import autopy
from time import sleep

duck_r = 255
duck_g = 119
duck_b = 99

def get_duck_position(startArea):
    screen_cap = autopy.bitmap.capture_screen()
    return screen_cap.find_color((duck_r,duck_g,duck_b), 0.03, ((startArea[0], startArea[1]), (800,300)))

def move_mouse_and_click(position):
    if position is not None:
        autopy.mouse.move(position[0], position[1])
        autopy.mouse.click()

def findGameArea():
    for i in range(100):
        screen = autopy.bitmap.capture_screen()
        pos = screen.find_color((0, 204, 255), 0.03)
        if pos:
            print("Game Area : " + str(pos))
            return pos

startArea = findGameArea()
for x in range(0, 1000):

    position = get_duck_position(startArea)
    move_mouse_and_click(position)