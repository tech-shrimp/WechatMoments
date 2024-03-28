import time
import tkinter
import tkinter.ttk

import win32con
import win32gui

from helper.auto_scroll_single import AutoScrollSingle


class AutoScrollSingleGuide:

    def __init__(self, root):
        self.working_note = None
        self.auto_thread = None
        self.frame = tkinter.LabelFrame(root)

        self.guide = tkinter.Label(self.frame, text="请打开搜一搜窗口\n点击开始后不要操作键鼠")
        self.guide.pack()

        self.search_username = tkinter.Entry(self.frame, width=12)
        self.search_username.insert(0, '请输入好友昵称')
        self.search_username.config(fg='grey')
        self.search_username.bind('<FocusIn>', self.on_search_username_click)
        self.search_username.pack()

        image = tkinter.PhotoImage(file='resource/gui_pictures/open_search_guide.png')
        self.guide_image = tkinter.Label(self.frame, image=image)
        self.guide_image.image = image
        self.guide_image.pack()

        self.button_text = tkinter.StringVar()
        self.button_text.set("开始")

        self.button = tkinter.ttk.Button(self.frame, textvariable=self.button_text,
                                         command=self.switch_auto_scroll_single)
        self.button.pack(pady=5)

    def on_search_username_click(self, event):
        if self.search_username.get() == '请输入好友昵称':
            self.search_username.delete(0, tkinter.END)
            self.search_username.config(fg='black')

    def switch_auto_scroll_single(self):

        search_hwnd = win32gui.FindWindow('Chrome_WidgetWin_0', '微信')
        wechat_hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')

        search_username = self.search_username.get()

        if self.auto_thread is None:
            if search_username == '请输入好友昵称' or search_username == '':
                self.search_username.config(fg='red')
                return
            if search_hwnd != 0 and wechat_hwnd != 0:

                self.auto_thread = AutoScrollSingle(self, search_hwnd, search_username)
                self.working_note = tkinter.Label(self.frame, text="正在自动读取朋友圈数据......."
                                                                   "\n请不要遮挡搜一搜窗口")


                self.working_note.pack()
                self.auto_thread.start()
                self.button_text.set("停止")
            else:
                pass
        else:
            if self.auto_thread.scrolling:
                self.button_text.set("开始")
                self.auto_thread.set_scrolling(False)
                self.auto_thread = None
            else:
                self.button_text.set("停止")
                self.switch_auto_scroll_single()
