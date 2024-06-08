import os
import tkinter
import tkinter.font
import tkinter.ttk
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
import tkcalendar
from decrypter.db_decrypt import DatabaseDecrypter
from decrypter.image_decrypt import ImageDecrypter
from decrypter.video_decrypt import VideoDecrypter
from gui.auto_scroll_guide import AutoScrollGuide
from gui.auto_scrolls_single_guide import AutoScrollSingleGuide
from gui.tool_tip import ToolTip
from entity.contact import Contact
from exporter.html_exporter import HtmlExporter
from gui.listbox_with_search import ListboxWithSearch


class Gui:
    def __init__(self):

        self.restart_note1 = None
        self.restart_note2 = None
        self.auto_scroll_single_guide = None
        self.auto_scroll_guide = None
        self.auto_scroll_frame = None
        self.search_username = None
        self.open_search_guide_image = None
        self.open_search_guide = None
        self.auto_scroll_button_single = None
        self.auto_scroll_button_single_text = None
        self.convert_video = None
        self.convert_video_var = None
        self.html_exporter_thread = None
        self.confirm_button_text = None
        self.succeed_label_2 = None
        self.succeed_label = None
        self.auto_scroll_button_text = None
        self.warning_label = None
        self.root = None
        self.waiting_label = None
        self.listbox = None
        self.begin_calendar = None
        self.end_calendar = None
        self.end_calendar_label = None
        self.begin_calendar_label = None
        self.confirm_button = None
        self.decrypt_progressbar = None
        self.export_progressbar = None
        self.next_step_button = None
        self.decrypter = None
        self.auto_scroll_button = None
        self.auto_scrolling_thread = None
        self.decrypt_note = None
        self.decrypt_note_text = None
        self.account_info = None
        self.video_decrypter = None
        self.image_decrypter = None
        self.export_dir_name = None
        self.exporting = False
        # 1: 自动滚动数据 2: 解密数据库 3: 导出
        self.page_stage = 1

    def run_gui(self):
        self.root = tkinter.Tk()
        self.root.geometry('650x650')
        self.root.title('朋友圈导出')

        self.waiting_label = tkinter.ttk.Label(self.root, text="正在连接微信....",
                                               font=("微软雅黑", 16), anchor='center')
        self.waiting_label.place(relx=0.5, rely=0.05, anchor='center')

        self.root.mainloop()

    def wechat_logged_in(self, account_info):

        self.account_info = account_info
        self.waiting_label.config(text="微信已登录")

        self.auto_scroll_button_text = tkinter.StringVar()
        self.auto_scroll_button_text.set("自动浏览全部朋友圈")
        self.auto_scroll_button = tkinter.ttk.Button(self.root, textvariable=self.auto_scroll_button_text,
                                                     command=self.open_auto_scroll_guide)
        self.auto_scroll_button.place(relx=0.35, rely=0.15, anchor='center')

        self.auto_scroll_button_single_text = tkinter.StringVar()
        self.auto_scroll_button_single_text.set("自动浏览单个朋友")
        self.auto_scroll_button_single = tkinter.ttk.Button(self.root, textvariable=self.auto_scroll_button_single_text,
                                                            command=self.switch_auto_scroll_single)
        self.auto_scroll_button_single.place(relx=0.655, rely=0.15, anchor='center')

        self.next_step_button = tkinter.ttk.Button(self.root, text="下一步", command=self.next_step)
        self.next_step_button.place(relx=0.65, rely=0.8)



    def open_auto_scroll_guide(self):

        if self.auto_scroll_single_guide and self.auto_scroll_single_guide.frame:
            self.auto_scroll_single_guide.frame.place_forget()

        self.auto_scroll_guide = AutoScrollGuide(self.root)
        self.auto_scroll_guide.frame.place(relx=0.5, rely=0.5, anchor='center')

    def switch_auto_scroll_single(self):

        if self.auto_scroll_guide and self.auto_scroll_guide.frame:
            self.auto_scroll_guide.frame.place_forget()

        self.auto_scroll_single_guide = AutoScrollSingleGuide(self.root)
        self.auto_scroll_single_guide.frame.place(relx=0.5, rely=0.5, anchor='center')


    def next_step(self):

        if self.page_stage == 1:

            if self.auto_scroll_guide and self.auto_scroll_guide.auto_thread:
                self.auto_scroll_guide.auto_thread.set_scrolling(False)

            if self.auto_scroll_single_guide and self.auto_scroll_single_guide.auto_thread:
                self.auto_scroll_guide.auto_thread.set_scrolling(False)

            self.auto_scroll_button.place_forget()
            self.auto_scroll_button_single.place_forget()

            if self.auto_scroll_guide and self.auto_scroll_guide.frame:
                self.auto_scroll_guide.frame.place_forget()

            if self.auto_scroll_single_guide and self.auto_scroll_single_guide.frame:
                self.auto_scroll_single_guide.frame.place_forget()

            self.restart_note1 = tkinter.Label(self.root, text="请关闭微信客户端", fg="red")
            self.restart_note1.place(relx=0.5, rely=0.2, anchor='center')
            self.restart_note2 = tkinter.Label(self.root, text="然后点击下一步")
            self.restart_note2.place(relx=0.5, rely=0.3, anchor='center')

        if self.page_stage == 2:

            self.restart_note1.place_forget()
            self.restart_note2.place_forget()
            self.waiting_label.place_forget()

            self.decrypter = DatabaseDecrypter(self, self.account_info.get("filePath"), self.account_info.get("key"))

            self.decrypt_note_text = tkinter.StringVar()
            self.decrypt_note_text.set("正在复制数据.....")

            self.decrypt_note = tkinter.Label(self.root, textvariable=self.decrypt_note_text)
            self.decrypt_note.place(relx=0.5, rely=0.2, anchor='center')
            self.decrypt_progressbar = tkinter.ttk.Progressbar(self.root)
            self.decrypt_progressbar.place(relx=0.5, rely=0.3, anchor='center')

            # 进度值最大值
            self.decrypt_progressbar['maximum'] = 100
            # 进度值初始值
            self.decrypt_progressbar['value'] = 0
            # 解密过程禁用下一步按钮
            self.next_step_button.config(state=tkinter.DISABLED)
            self.decrypter.decrypt()
        if self.page_stage == 3:
            self.decrypt_note.place_forget()
            self.decrypt_progressbar.place_forget()
            self.init_export_page()
            # 不再有下一步按钮
            self.next_step_button.place_forget()
            # 初始化视频导出器
            self.video_decrypter = VideoDecrypter(self, self.account_info.get("filePath"))
            # 初始化图片导出器
            self.image_decrypter = ImageDecrypter(self, self.account_info.get("filePath"))


        self.page_stage = self.page_stage + 1

    def init_export_page(self):

        from app.DataBase import micro_msg_db
        contact_datas = micro_msg_db.get_contact()

        contacts = []
        for c in contact_datas:
            contact = Contact(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10], c[11])
            contacts.append(contact)

        def validate_contact(this_contact: Contact):
            c_type = this_contact.type
            user_name: str = this_contact.userName

            # 不是其他号码
            is_misc_account = c_type == 1 or c_type == 33 or c_type == 513
            # 不是公众号
            is_gh_account = user_name.startswith("gh_")
            # 不是聊天群
            is_chatroom = user_name.endswith("@chatroom")
            # 不是文件传输助手
            is_filehelper = this_contact.userName == "filehelper"
            return (not is_misc_account) and (not is_gh_account) and (not is_chatroom) and (not is_filehelper)

        filtered = filter(validate_contact, contacts)
        contacts = list(filtered)

        self.listbox = ListboxWithSearch(self.root, contacts)
        self.listbox.frame.place(relx=0.05, rely=0.03)

        self.begin_calendar_label = tkinter.ttk.Label(text="开始日期")
        self.begin_calendar_label.place(relx=0.65, rely=0.15)

        # 默认开始时间是100天前
        current_date = datetime.now()
        half_year_ago = current_date - timedelta(days=100)
        self.begin_calendar = tkcalendar.DateEntry(master=self.root, locale="zh_CN", year=half_year_ago.year,
                                                   month=half_year_ago.month, day=half_year_ago.day,
                                                   maxdate=datetime.now())
        self.begin_calendar.place(relx=0.65, rely=0.2)

        self.end_calendar_label = tkinter.ttk.Label(text="截止日期")
        self.end_calendar_label.place(relx=0.65, rely=0.25)
        self.end_calendar = tkcalendar.DateEntry(master=self.root, locale="zh_CN", maxdate=datetime.now())
        self.end_calendar.place(relx=0.65, rely=0.3)


        self.convert_video_var = tkinter.IntVar(value=0)
        self.convert_video = tkinter.ttk.Checkbutton(self.root, text='视频转码', variable=self.convert_video_var)
        self.convert_video.place(relx=0.65, rely=0.45)
        ToolTip(self.convert_video,
                "视频原始格式为H265,只支持\nChrome浏览器播放，勾选后\n将视频转码为H264,支持大\n部分浏览器，但导出速度变慢")

        self.confirm_button_text = tkinter.StringVar()
        self.confirm_button_text.set("开始导出")

        self.confirm_button = tkinter.ttk.Button(self.root, textvariable=self.confirm_button_text,
                                                 command=self.confirm_export)
        self.confirm_button.place(relx=0.65, rely=0.6)

        # 导出成功的提示
        self.succeed_label = tkinter.Label(self.root, text="导出结束")
        self.succeed_label_2 = tkinter.Label(self.root, text="打开文件夹", fg="#0000FF", cursor="hand2")
        self.succeed_label_2.bind("<Button-1>", self.open_target_folder)

        # 进度条
        self.export_progressbar = tkinter.ttk.Progressbar(self.root, length=150)

    def confirm_export(self):

        if self.html_exporter_thread and not self.html_exporter_thread.stop_flag:
            self.html_exporter_thread.stop()
        else:
            if not self.warning_label:
                self.warning_label = tkinter.Label(self.root, fg="red")
                self.warning_label.place(relx=0.65, rely=0.55)

            self.warning_label.config(text="")
            contacts = self.listbox.get_contacts()
            if not contacts:
                self.warning_label.config(text=f"请选择至少一个联系人")
                return

            if self.begin_calendar.get_date() > self.end_calendar.get_date():
                self.warning_label.config(text=f"开始时间必须小于截止时间")
                return

            self.export_progressbar.place(relx=0.64, rely=0.68)
            # 进度值最大值
            self.export_progressbar['maximum'] = 100
            # 进度值初始值
            self.export_progressbar['value'] = 0

            current_time = datetime.now()
            self.export_dir_name = current_time.strftime("%Y_%m_%d_%H%M%S")
            contact_map = {contact.userName: contact for contact in contacts}

            self.confirm_button_text.set("停止导出")
            self.succeed_label.place_forget()
            self.succeed_label_2.place_forget()

            # 导出线程
            self.html_exporter_thread = HtmlExporter(self, self.export_dir_name, contact_map,
                                                     self.begin_calendar.get_date(), self.end_calendar.get_date(),
                                                     self.convert_video_var.get())
            self.html_exporter_thread.start()

    def update_decrypt_progressbar(self, progress):
        self.decrypt_progressbar['value'] = progress
        self.root.update()

    def update_export_progressbar(self, progress):
        self.export_progressbar['value'] = progress
        self.root.update()

    def export_succeed(self):
        self.confirm_button_text.set("开始导出")
        self.succeed_label.place(relx=0.64, rely=0.75)
        self.succeed_label_2.place(relx=0.76, rely=0.75)

    def open_target_folder(self, event):
        folder_path = Path(f"output/{self.export_dir_name}/")
        # 转换为绝对路径
        absolute_path = folder_path.resolve()
        os.startfile(absolute_path)
