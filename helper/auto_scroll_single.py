import math
import threading
import time
import traceback
import pyautogui
import pyperclip
import win32con
import win32gui
from retry import retry
from win32api import GetSystemMetrics

import log


class AutoScrollSingle(threading.Thread):

    def __init__(self, gui, search_hwnd, friend_name):
        self.gui = gui
        self.search_hwnd = search_hwnd
        self.friend_name = friend_name
        self.scrolling = False
        self.resolutions = ['', '1920', '1600', '2560_125', '2560_175', '2560_100', '1366']
        super().__init__()

    @retry(tries=5, delay=2)
    def find_moments_tab(self):
        result = None
        for resolution in self.resolutions:
            try:
                result = pyautogui.locateCenterOnScreen(f'resource/auto_gui/{resolution}/moments_tab.png',
                                                        grayscale=True, confidence=0.8)
                break
            except Exception as e:
                log.LOG.warn("Can't find_moments_tab in resolution: " + resolution)
                pass

        if result is None:
            raise Exception("Can 't find_moments_tab")

        return result

    @retry(tries=5, delay=2)
    def find_search_button(self):

        element = None
        for resolution in self.resolutions:
            try:
                element = pyautogui.locateOnScreen(f'resource/auto_gui/{resolution}/search_button.png',
                                          grayscale=True, confidence=0.8)
                break
            except Exception as e:
                log.LOG.warn("Can't find_moments_tab in resolution: " + resolution)
                pass

        if element is None:
            raise Exception("Can 't search_button")

        return element

    @retry(tries=5, delay=2)
    def find_friends(self):
        result = None

        for resolution in self.resolutions:
            try:
                result = pyautogui.locateCenterOnScreen(f'resource/auto_gui/{resolution}/friends.png',
                                                        grayscale=True, confidence=0.8)
                break
            except Exception as e:
                log.LOG.warn("Can't find_friends in resolution: " + resolution)
                pass

        if result is None:
            raise Exception("Can 't find_friends")

        return result

    @retry(tries=5, delay=2)
    def find_complete(self):

        result = None

        for resolution in self.resolutions:
            try:
                result = pyautogui.locateCenterOnScreen(f'resource/auto_gui/{resolution}/complete.png',
                                                        grayscale=True, confidence=0.8)
                break
            except Exception as e:
                log.LOG.warn("Can't find_complete in resolution: " + resolution)
                pass

        if result is None:
            raise Exception("Can 't find_complete")

        return result

    def run(self) -> None:
        self.scrolling = True

        try:
            search_hwnd = win32gui.FindWindow('Chrome_WidgetWin_0', '微信')
            wechat_hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')

            # 先把微信主窗口放置前台
            win32gui.SetForegroundWindow(wechat_hwnd)
            win32gui.ShowWindow(wechat_hwnd, win32con.SW_SHOWNORMAL)
            win32gui.SetWindowPos(wechat_hwnd, None, 100, 100, 0, 0, win32con.SWP_NOSIZE)
            time.sleep(0.3)
            # 先把搜一搜窗口放前台
            win32gui.SetForegroundWindow(search_hwnd)
            win32gui.ShowWindow(search_hwnd, win32con.SW_SHOWNORMAL)
            win32gui.SetWindowPos(search_hwnd, None, 50, 50, 0, 0, win32con.SWP_NOSIZE)


            # 点击朋友圈三个字
            x, y = self.find_moments_tab()
            pyautogui.click(x, y)
            time.sleep(0.1)

            # 点击搜索按钮左侧
            element = self.find_search_button()
            pyautogui.click(element.left - 100, element.top + element.height / 2)
            time.sleep(0.25)

            # 输入字符
            pyautogui.write('1')
            time.sleep(0.25)

            # 搜索
            pyautogui.click(element.left + element.width / 2, element.top + element.height / 2)
            time.sleep(1.5)

            # 展开朋友
            x, y = self.find_friends()
            pyautogui.click(x, y)
            time.sleep(0.5)

            # 搜索好友
            pyperclip.copy(self.friend_name)
            time.sleep(0.25)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)

            # 回车
            pyautogui.press('enter')
            time.sleep(0.5)

            # 点击完成
            x, y = self.find_complete()
            pyautogui.click(x, y)
            time.sleep(0.25)

            # 点击搜索按钮左侧
            element = self.find_search_button()
            pyautogui.click(element.left - 100, element.top + element.height / 2)
            time.sleep(0.25)

            pyautogui.press('backspace')
            time.sleep(0.1)
            pyautogui.press('backspace')
            time.sleep(0.25)
            pyperclip.copy('？')
            time.sleep(0.25)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.25)



            element = self.find_search_button()
            pyautogui.click(element.left + element.width / 2, element.top + element.height / 2)
            time.sleep(1.0)

            while self.scrolling:

                element = self.find_search_button()
                right_bottom = (element.left + element.width, element.top + element.height + 300)
                pyautogui.scroll(-120)
                pyautogui.click(right_bottom)
                time.sleep(0.2)

                search_hwnd = win32gui.FindWindow('Chrome_WidgetWin_0', '微信')
                moments_hwnd = win32gui.FindWindow('SnsWnd', '朋友圈')

                if search_hwnd and moments_hwnd:
                    # 调整位置朋友圈不要遮挡
                    width = GetSystemMetrics(0)
                    win32gui.SetWindowPos(moments_hwnd, None, 50, 50, 0, 0, win32con.SWP_NOSIZE)
                    win32gui.SetWindowPos(search_hwnd, None, 50, 50, 0, 0, win32con.SWP_NOSIZE)


        except Exception:
            traceback.print_exc()

    def set_scrolling(self, scrolling: bool) -> None:
        self.scrolling = scrolling
        if not self.scrolling:
            self.gui.working_note.pack_forget()
        if self.scrolling and self.gui.working_note:
            self.gui.working_note.pack()
