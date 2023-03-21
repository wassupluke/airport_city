# TODO add feature in send planes
'''Here I have added functionality that will locate the game window and bring it into
focus before running subsequent lines of code. This will avoid the necessity of using
a sleep time while you click over to it. Disregard the find_focus feature if you plan
to continue using the 'q' keypress to activate your program from in-game.

The pydirectinput.click() feature works beatifully. Use this in tandem with your
pyautogui.LocateOnScreen function for best results.

The pyautogui documentation recommends enabling their failsafe feature to avoid the code
running a muck. Moving the mouse to any corner of the screen will abort the python
program.'''

import win32gui
import pyautogui
import pydirectinput
import cv2
from time import sleep


def main():
    print('running main')
    print('::::::::::::')
    find_focus()
    print('::::::::::::')
    find_suitcase()
    print('::::::::::::')
    find_coin()
    print('::::::::::::')
    send_planes()
    print('::::::::::::')
    guest_planes()
    print('::::::::::::')
    objective_complete()
    print('::::::::::::')
    collections()
    print('::::::::::::')
    congratulations()
    print('::::::::::::')


def find_focus():
    print('running find_focus')
    title = '🛩 Version 8.31.24 | SupportID: 20KPQFMVY ‎- Airport City'
    '''NOTE: Title may need revised if game version updates
    use the list_window_names function to see titles of all
    open windows'''
    hwnd = win32gui.FindWindow(None, title)  # locates game
    hwnd = win32gui.SetForegroundWindow(hwnd)  # focuses game


def find_suitcase():
    print('running find_suitcase')
    pngs = ['suitcase.png',
            'suitcase_sm.png',
            'suitcase_sm2.png',
            'suitcase_sm3.png']
    for png in pngs:
        print(f'finding {png}')
        suitcase = pyautogui.locateOnScreen(png, confidence=0.45)
        if suitcase is not None:
            pyautogui.moveTo(suitcase[0] + 8, suitcase[1] + 8)
            click()
            sleep(0.25)
            full = pyautogui.locateOnScreen('terminal_full.png', confidence=0.8)
            if full is not None:
                pyautogui.press('esc')
                break
            

def find_coin():
    print('running find_coin')
    pngs = ['coin.png',
            'coin_sm.png',
            'coin_sm1.png']
    for png in pngs:
        print(f'finding {png}')
        for _ in range(3):
            coin = pyautogui.locateOnScreen(png, confidence=0.5)
            if coin is not None:
                pyautogui.moveTo(coin[0] + 8, coin[1] + 8)
                click()
                sleep(0.3)
    

def send_planes():
    print('running send_planes')
    for _ in range(3):
        plane = pyautogui.locateOnScreen('ready_plane.png', confidence=0.65)
        if plane is not None:  # checks that a plane is ready to send
            pyautogui.moveTo(plane[0] + 7, plane[1] + 7)
            click()
            # FUTURE FEATURE: compares fuel/pass required to available supply
            depart = pyautogui.locateOnScreen('depart.png', confidence=0.8)
            if depart is not None:  # checks that plane can depart
                pyautogui.moveTo(depart[0] + 30, depart[1] + 30)
                click()
                bad_reqs = pyautogui.locateOnScreen('departure_reqs_not_met.png', confidence=0.7)
                if bad_reqs is not None:
                    pyautogui.press('esc')
                    sleep(0.2)
                    pyautogui.press('esc')
        # COLLECT PILOT CAPS
        print('finding caps')
        caps = ['pilot_cap.png', 'pilot_cap2.png', 'pilot_cap3.png']
        for c in caps:
            cap = pyautogui.locateOnScreen(c, confidence=0.75)
            if cap is not None:  # checks for pilot caps on landed planes
                pyautogui.moveTo(cap[0] + 5, cap[1] + 8)
                click()

    
def guest_planes():
    print('running guest_planes')
    # LAND GUEST PLANES
    tower = pyautogui.locateOnScreen('guest_planes_tower.png', confidence=0.9)
    if tower is not None:  # checks that guest tower shows
        pyautogui.moveTo(tower)
        click()
        sleep(0.4)
        for _ in range(2):
            reqs = pyautogui.locateOnScreen('landing_reqs.png', confidence=0.8)
            bad_reqs = pyautogui.locateOnScreen('landing_reqs_not_met.png', confidence=0.8)
            if reqs is not None:  # checks that planes can land
                pyautogui.moveTo(reqs[0] + 250, reqs[1] + 15)
                click()
                attn = pyautogui.locateOnScreen('land_planes_in_queue.png', confidence=0.8)
                if attn is not None:  # checks for full landing queue
                    pyautogui.press('esc')
            elif bad_reqs is not None:  # checks for unmet landing reqs and declines
                pyautogui.moveTo(bad_reqs[0] + 250, bad_reqs[1] + 75)
                click()
            else:  
                pyautogui.press('esc', presses=2)
                break


def objective_complete():
    print('looking for completed objectives')
    marks = ['quests_icon.png', 'checkmark.png']
    for mark in marks:
        check = pyautogui.locateOnScreen(mark, confidence=0.9)
        if check is not None:
            pyautogui.moveTo(check[0], check[1] + 10)
            click()
            sleep(0.5)
            for _ in range(2):
                take = pyautogui.locateOnScreen('take.png', confidence=0.6)
                if take is not None:
                    pyautogui.moveTo(take[0] + 60, take[1] + 20)
                    click()
                    congratulations()


def collections():
    print('running collections')
    icon = pyautogui.locateOnScreen('collections_icon.png', confidence=0.95)
    if icon is not None:
        pyautogui.moveTo(icon)
        click()
        sleep(0.5)
        buttons = ['collect.png', 'collect2.png']
        for button in buttons:
            collect = pyautogui.locateOnScreen(button, confidence=0.9)
            print(collect)
            if collect is not None:
                pyautogui.moveTo(collect[0] + 8, collect[1] + 8)
                click()

    
def congratulations():
    print('looking for congratulations')
    congrats = pyautogui.locateOnScreen('congratulations.png', confidence=0.9)
    if congrats is not None:
        pyautogui.press('esc')


def cargo_container():
    print('running cargo_container')
    cargo = pyautogui.locateOnScreen('cargo_container_icon.png', confidence=0.9)
    if cargo is not None:
        pyautogui.moveTo(cargo[0] + 8, cargo[1] + 8)
        click()
        container = pyautogui.locateOnScreen('cargo_container.png', confidence=0.8)
        if container is not None:
            pyautogui.moveTo(container)
            click()
            take = pyautogui.locateOnScreen('take_cargo.png', confidence=0.8)
            if take is not None:
                pyautogui.moveTo(take[0] + 40, take[1] + 10)
                click()
                sleep(5)
                congratulations()
                sleep(0.1)
                pyautogui.press('esc')
                

def click():
    print('running click')
    pydirectinput.mouseDown()  # clicks the mouse
    sleep(0.01)
    pydirectinput.mouseUp()


def list_window_names():  # Prints names of all active windows
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(f'{hex(hwnd)} "{win32gui.GetWindowText(hwnd)}"')
    win32gui.EnumWindows(winEnumHandler, None)


pyautogui.FAILSAFE = True
# fail-safe triggers from mouse moving to a corner of the screen
while True:
    for _ in range(10):
        main()
        pyautogui.press('esc')
    cargo_container()


    
