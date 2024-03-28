import random
import time
import threading
import pywintypes
import win32api
import win32con
import win32gui


class AutoScroll(threading.Thread):

    def __init__(self, gui, moments_hwnd):
        self.gui = gui
        self.moments_hwnd = moments_hwnd
        self.scrolling = False
        super().__init__()

    def run(self) -> None:
        self.scrolling = True
        while True:
            if self.scrolling:
                try:
                    rect = win32gui.GetWindowRect(self.moments_hwnd)
                    x = (rect[0] + rect[2]) // 2
                    y = (rect[1] + rect[3]) // 2
                    notch = 10
                    win32api.SendMessage(self.moments_hwnd, win32con.WM_MOUSEWHEEL,
                                         win32api.MAKELONG(0, -120 * notch), win32api.MAKELONG(x, y))

                    self.gui.flood_moments_note.pack()
                    random_sleep = random.uniform(0.7, 0.8)
                    time.sleep(random_sleep)
                except pywintypes.error as e:
                    self.moments_hwnd = win32gui.FindWindow("SnsWnd", '朋友圈')
                    self.gui.flood_moments_note.pack_forget()
                    time.sleep(1)
            else:
                self.gui.flood_moments_note.pack_forget()
                time.sleep(1)

    def set_scrolling(self, scrolling: bool) -> None:
        self.scrolling = scrolling