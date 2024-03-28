import tkinter
import tkinter.ttk

import win32gui

from entity.contact import Contact
from helper.auto_scroll import AutoScroll


class AutoScrollGuide:

    def __init__(self, root):
        self.flood_moments_note = None
        self.auto_thread = None
        self.frame = tkinter.LabelFrame(root)

        self.open_moments_guide = tkinter.Label(self.frame, text="请打开朋友圈窗口")
        self.open_moments_guide.pack()

        image = tkinter.PhotoImage(file='resource/gui_pictures/open_moments_guide.png')
        self.open_moments_guide_image = tkinter.Label(self.frame, image=image)
        self.open_moments_guide_image.image = image
        self.open_moments_guide_image.pack()

        self.auto_scroll_button_text = tkinter.StringVar()
        self.auto_scroll_button_text.set("开始")

        self.auto_scroll_button = tkinter.ttk.Button(self.frame, textvariable=self.auto_scroll_button_text,
                                                     command=self.switch_auto_scroll)
        self.auto_scroll_button.pack(pady=5)

    def switch_auto_scroll(self):

        if self.auto_thread is None:
            moments_hwnd = win32gui.FindWindow("SnsWnd", '朋友圈')
            if moments_hwnd != 0:
                self.auto_thread = AutoScroll(self, moments_hwnd)
                self.flood_moments_note = tkinter.Label(self.frame, text="正在自动读取朋友圈数据......."
                                                                         "\n可将窗口最小化，后台自动执行"
                                                                         "\n可随时查看进度，可随时停止")
                self.flood_moments_note.pack()
                self.auto_thread.start()
                self.auto_scroll_button_text.set("停止")
            else:
                pass
        else:
            if self.auto_thread.scrolling:
                self.auto_scroll_button_text.set("继续")
                self.auto_thread.set_scrolling(False)
            else:
                self.auto_scroll_button_text.set("停止")
                self.auto_thread.set_scrolling(True)
