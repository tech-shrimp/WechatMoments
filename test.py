import datetime

from decrypter.image_decrypt import ImageDecrypter
from decrypter.video_decrypt import VideoDecrypter
import threading
from time import sleep
from pywxdump import read_info
from gui.gui import Gui


def stage_3():
    gui = Gui()
    gui_thread = threading.Thread(target=gui.run_gui)
    gui_thread.start()
    gui.init_export_page()

    gui.begin_calendar.set_date(datetime.date(2024, 5, 6))
    gui.end_calendar.set_date(datetime.date(2024, 5, 6))

    # 后台读取微信信息
    # 请等待完全接入微信再进行UI操作
    while True:
        sleep(0.5)
        result = read_info(None, is_logging=True)
        # 如果解密失败，读取到报错信息
        if isinstance(result, str):
            gui.waiting_label.config(text="请启动微信....")
            pass
        elif isinstance(result, list) and result[0].get("key") == "None":
            gui.waiting_label.config(text="请登陆微信....")
        else:
            gui.account_info = result[0]
            gui.waiting_label.config(text="微信已登录")
            # 初始化视频导出器
            gui.video_decrypter = VideoDecrypter(gui, gui.account_info.get("filePath"))
            gui.image_decrypter = ImageDecrypter(gui, gui.account_info.get("filePath"))
            gui.waiting_label.place_forget()
            break

if __name__ == "__main__":
    stage_3()
