import pyautogui
import curses
import sys

def move_cursor(stdscr):

    x, y = pyautogui.position()

    # Define the edges of the box
    box_width = 300
    box_height = 200
    top_left = (x, y)
    top_right = (x + box_width, y)
    bottom_left = (x, y + box_height)
    bottom_right = (x + box_width, y + box_height)

    while True:

        for i in range(top_left[0], top_right[0]):
            pyautogui.moveTo(i, top_left[1], duration=0.01)
            check_pause(stdscr)

        for i in range(top_right[1], bottom_right[1]):
            pyautogui.moveTo(top_right[0], i, duration=0.01)
            check_pause(stdscr)

        for i in range(bottom_right[0], bottom_left[0], -1):
            pyautogui.moveTo(i, bottom_right[1], duration=0.01)
            check_pause(stdscr)

        for i in range(bottom_left[1], top_left[1], -1):
            pyautogui.moveTo(top_left[0], i, duration=0.01)
            check_pause(stdscr)

def check_pause(stdscr):
    # Check for keyboard input
    stdscr.nodelay(1) 
    key = stdscr.getch()
    if key == ord('p') or key == ord('P'):
        stdscr.addstr("Pause\n")
        stdscr.refresh()
        while stdscr.getch() == -1:
            pass
        stdscr.addstr("Resume\n")
        stdscr.refresh()
    elif key == ord('q') or key == ord("Q"):
        stdscr.addstr("Quit\n")
        sys.exit()
        
# Initialize curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

try:
    move_cursor(stdscr)
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()
