import logging
import os
import sys
import time

filename = time.strftime("%Y-%m-%d", time.localtime(time.time()))

try:
    if not os.path.exists('log'):
        os.mkdir('log')
    log_file = f'log/{filename}-log.log'
    console_file = f'log/{filename}-output.log'
except:
    log_file = f'{filename}-log.log'
    console_file = f'{filename}-output.log'

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # pyinstaller 输出日志到文件
    f = open(console_file, 'a')
    sys.stdout = f
    sys.stderr = f

file_handler = logging.FileHandler(log_file, encoding='utf-8')
logging.basicConfig(level='DEBUG', format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logging.getLogger().addHandler(file_handler)
LOG = logging.getLogger("WechatMoments")

