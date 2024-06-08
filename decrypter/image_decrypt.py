import hashlib
import os
import shutil
import subprocess
import sys
import traceback
from datetime import date
from pathlib import Path
import filetype

import log


class ImageDecrypter:

    def __init__(self, gui: 'Gui', file_path):
        self.file_path = file_path
        self.gui = gui
        self.sns_cache_path = file_path + "/FileStorage/Sns/Cache"

    @staticmethod
    def get_output_path(dir_name, md5, duration):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # 这是到_internal文件夹
            resource_dir = getattr(sys, '_MEIPASS')
            # 获取_internal上一级文件夹再拼接
            return os.path.join(os.path.dirname(resource_dir), 'output', dir_name, 'videos', f'{md5}_{duration}.mp4')
        else:
            return os.path.join(os.getcwd(), 'output', dir_name, 'videos', f'{md5}_{duration}.mp4')

    @staticmethod
    def calculate_md5(file_path):
        with open(file_path, "rb") as f:
            file_content = f.read()
        return hashlib.md5(file_content).hexdigest()

    @staticmethod
    def get_all_month_between_dates(start_date, end_date) -> list[str]:
        result = []
        current_date = start_date
        while current_date <= end_date:
            # 打印当前日期的年份和月份
            result.append(current_date.strftime("%Y-%m"))
            year = current_date.year + (current_date.month // 12)
            month = current_date.month % 12 + 1
            # 更新current_date到下个月的第一天
            current_date = date(year, month, 1)
        return result

    @staticmethod
    def decode(magic, buf):
        return bytearray([b ^ magic for b in list(buf)])

    @staticmethod
    def guess_image_encoding_magic(buf):
        header_code, check_code = 0xff, 0xd8
        # 微信图片加密方法对字节逐一“异或”，即 源文件^magic(未知数)=加密后文件
        # 已知jpg的头字节是0xff，将0xff与加密文件的头字节做异或运算求解magic码
        magic = header_code ^ list(buf)[0] if buf else 0x00
        # 尝试使用magic码解密，如果第二字节符合jpg特质，则图片解密成功
        _, code = ImageDecrypter.decode(magic, buf[:2])
        if check_code == code:
            return magic

    def decrypt_images(self, exporter, start_date, end_date, dir_name) -> None:
        """将图片文件从缓存中复制出来，重命名为{主图字节数}_{缩略图字节数}.jpg
        duration单位为秒
        """
        months = self.get_all_month_between_dates(start_date, end_date)

        total_files = 0
        processed_files = 0
        for month in months:
            source_dir = self.sns_cache_path + "/" + month
            total_files = total_files + len(list(Path(source_dir).rglob('*')))

        for month in months:
            source_dir = self.sns_cache_path + "/" + month
            for file in Path(source_dir).rglob('*'):
                # 排除缩略图
                if not exporter.stop_flag and file.is_file() and not file.name.endswith('_t'):
                    try:
                        with open(file, 'rb') as f:
                            buff = bytearray(f.read())
                        magic = self.guess_image_encoding_magic(buff)
                        if magic:
                            os.makedirs(f"output/{dir_name}/images/{month}/", exist_ok=True)
                            os.makedirs(f"output/{dir_name}/thumbs/{month}/", exist_ok=True)
                            main_file_size = file.stat().st_size
                            thumb_file_size = 0
                            # 找到对应缩略图
                            thumb_file = Path(f'{source_dir}/{file.name}_t')
                            if thumb_file.exists():
                                thumb_file_size = thumb_file.stat().st_size
                                # 读缩略图加密
                                with open(thumb_file, 'rb') as f:
                                    thumb_buff = bytearray(f.read())

                                # 写缩略图
                                thumb_destination = (f"output/{dir_name}/thumbs/{month}/"
                                                     f"{main_file_size}_{thumb_file_size}.jpg")
                                with open(thumb_destination, 'wb') as f:
                                    new_thumb_buff = self.decode(magic, thumb_buff)
                                    f.write(new_thumb_buff)

                            destination = (f"output/{dir_name}/images/{month}/"
                                           f"{main_file_size}_{thumb_file_size}.jpg")
                            with open(destination, 'wb') as f:
                                new_buf = self.decode(magic, buff)
                                f.write(new_buf)
                    except Exception:
                        traceback.print_exc()
                processed_files = processed_files + 1
                # 15%的进度作为处理图片使用
                progress = round(processed_files / total_files * 15)
                self.gui.update_export_progressbar(progress)
