# TODO add feature in send planes
'''Here I have added functionality that locates the game window and brings it
into focus before running subsequent lines of code. This will avoid the
necessity of using a sleep time while you click over to it.

The pydirectinput click feature works beatifully. Use this in tandem with your
pyautogui.LocateOnScreen function for best results.

The pyautogui documentation recommends enabling their failsafe feature to avoid
the code running a muck. Moving the mouse to any corner of the screen will
abort the python program.'''

import win32gui
import pyautogui
import pydirectinput
import cv2
from time import sleep


def main():
    find_focus()
    # find_suitcase()
    neighbor()
    find_coin()
    end()
    send_planes()
    end()
    fix_planes()
    end()
    guest_planes()
    end()
    collections()
    congratulations()
    end()


def find_focus():
    title = '🛩 Version 8.31.24 | SupportID: 20NNHCHM5 ‎- Airport City GI'
    '''NOTE: Title may need revised if game version updates
    use the list_window_names function to see titles of all
    open windows'''
    hwnd = win32gui.FindWindow(None, title)  # locates game
    hwnd = win32gui.SetForegroundWindow(hwnd)  # focuses game


def find_suitcase():
    pngs = ['suitcase.png',
            'suitcase_sm.png',
            'suitcase_sm2.png',
            'suitcase_sm3.png']
    for png in pngs:
        suitcase = pyautogui.locateOnScreen(png, confidence=0.8)
        if suitcase is not None:
            pyautogui.moveTo(suitcase[0] + 8, suitcase[1] + 8)
            click()
            sleep(0.25)
            full = pyautogui.locateOnScreen('terminal_full.png',
                                            confidence=0.8)
            if full is not None:
                pyautogui.press('esc')
                break


def find_coin():
    pngs = ['coin.png',
            'coin_sm.png',
            'coin_sm1.png',
            'coin_sm2.png']
    for png in pngs:
        for _ in range(4):
            coin = pyautogui.locateOnScreen(png, confidence=0.5)
            if coin is not None:
                pyautogui.moveTo(coin[0] + 8, coin[1] + 8)
                click()
                sleep(0.1)


def send_planes():
    pngs = ['ready_plane.png',
            'ready_plane2.png',
            'ready_plane3.png',
            'ready_plane4.png',
            'ready_plane5.png',
            'ready_plane6.png']
    for png in pngs:
        sleep(0.1)
        plane = pyautogui.locateOnScreen(png, confidence=0.65)
        if plane is not None:
            sleep(0.1)
            pyautogui.moveTo(plane[0] + 7, plane[1] + 7)
            click()
            depart = pyautogui.locateOnScreen('depart.png', confidence=0.8)
            if depart is not None:
                pyautogui.moveTo(depart[0] + 30, depart[1] + 30)
                click()
                bad_reqs = pyautogui.locateOnScreen('departure_reqs_not_met.png',
                                                    confidence=0.7)
                if bad_reqs is not None:
                    pyautogui.press('esc')
                    sleep(0.2)
                    pyautogui.press('esc')
    # COLLECT PILOT CAPS
    caps = ['pilot_cap.png',
            'pilot_cap2.png',
            'pilot_cap3.png',
            'pilot_cap4.png',
            'pilot_cap5.png',
            'pilot_cap6.png']
    for c in caps:
        cap = pyautogui.locateOnScreen(c, confidence=0.75)
        if cap is not None:  # checks for pilot caps on landed planes
            pyautogui.moveTo(cap[0] + 5, cap[1] + 8)
            click()


def guest_planes():
    # LAND GUEST PLANES
    tower = pyautogui.locateOnScreen('guest_planes_tower.png', confidence=0.9)
    if tower is not None:  # checks that guest tower shows
        pyautogui.moveTo(tower)
        click()
        sleep(0.4)
        for _ in range(2):
            reqs = pyautogui.locateOnScreen('landing_reqs.png', confidence=0.8)
            bad_reqs = pyautogui.locateOnScreen('landing_reqs_not_met.png',
                                                confidence=0.8)
            if reqs is not None:  # checks that planes can land
                pyautogui.moveTo(reqs[0] + 350, reqs[1] + 15)
                click()
                attn = pyautogui.locateOnScreen('land_planes_in_queue.png',
                                                confidence=0.8)
                """if attn is not None:  # checks for full landing queue
                    pyautogui.press('esc')
            elif bad_reqs is not None:  # checks for unmet landing reqs
                pyautogui.moveTo(bad_reqs[0] + 350, bad_reqs[1] + 75)
                click()"""
            else:
                pyautogui.press('esc', presses=2)
                break


def collections():
    icon = pyautogui.locateOnScreen('collections_icon.png', confidence=0.95)
    if icon is not None:
        pyautogui.moveTo(icon)
        sleep(1)
        click()
        sleep(0.5)
        buttons = ['collect.png',
                    'collect2.png',
                    'collect3.png']
        for button in buttons:
             collect = pyautogui.locateOnScreen(button, confidence=0.9)
             if collect is not None:
                pyautogui.moveTo(collect[0] + 8, collect[1] + 8)
                click()
                sleep(0.8)
                pyautogui.press('esc')


def congratulations():
    congrats = pyautogui.locateOnScreen('congratulations.png', confidence=0.9)
    if congrats is not None:
        pyautogui.press('esc')


def click():
    pydirectinput.mouseDown()  # clicks the mouse
    sleep(0.01)
    pydirectinput.mouseUp()


def list_window_names():  # Prints names of all active windows
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(f'{hex(hwnd)} "{win32gui.GetWindowText(hwnd)}"')
    win32gui.EnumWindows(winEnumHandler, None)


def end():
    pyautogui.press('esc')
    comfirm_end = pyautogui.locateOnScreen('quit.png', confidence=0.8)
    if comfirm_end is not None:
        pyautogui.press('esc')


def neighbor():
    neighbor = pyautogui.locateOnScreen('neighbor.png', confidence=0.8)
    if neighbor is not None:
        pyautogui.moveTo(neighbor[0] + 10, neighbor[1] + 10)
        click()


def fix_planes():
    pngs = ['fix_plane1.png',
            'fix_plane2.png',
            'fix_plane3.png',
            'fix_plane4.png',
            'fix_plane5.png']
    for png in pngs:
        fix = pyautogui.locateOnScreen(png, confidence=0.65)
        if fix is not None:
            pyautogui.moveTo(fix[0] + 7, fix[1] + 7)
            click()
            sleep(1)
            repair = pyautogui.locateOnScreen('repair.png', confidence=0.8)
            if repair is not None:
                pyautogui.moveTo(repair[0] + 8, repair[1] + 8)
                click()
                sleep(1)
                speedup = pyautogui.locateOnScreen('speedup.png', confidence=0.8)
                if speedup is not None:
                    pyautogui.moveTo(speedup[0] + 8, speedup[1] + 8)
                    click()


pyautogui.FAILSAFE = True
# fail-safe triggers from mouse moving to the top left corner of the screen
while True:
    for _ in range(10):
        main()
