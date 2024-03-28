import threading
import tkinter
import traceback
from time import sleep
from pywxdump import read_info

def main():
    from gui.gui import Gui

    gui = Gui()
    gui_thread = threading.Thread(target=gui.run_gui)
    gui_thread.start()

    info = ""
    while True:
        try:
            info = read_info(None, is_logging=True)
        except:
            traceback.print_exc()
        # 如果解密失败，读取到报错信息
        if isinstance(info, str):
            gui.waiting_label.config(text="请启动微信....")
            sleep(0.5)
        elif isinstance(info, list) and info[0].get("key") == "None":
            gui.waiting_label.config(text="请登陆微信....")
            sleep(0.5)
        else:
            break

    gui.wechat_logged_in(info[0])


if __name__ == "__main__":
    main()
