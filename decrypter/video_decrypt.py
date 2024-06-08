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


class VideoDecrypter:

    def __init__(self, gui: 'Gui', file_path):
        self.file_path = file_path
        self.gui = gui
        self.sns_cache_path = file_path + "/FileStorage/Sns/Cache"

    @staticmethod
    def get_ffmpeg_path():
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # 这是到_internal文件夹
            resource_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            # 获取_internal上一级再拼接
            return os.path.join(os.path.dirname(resource_dir), 'resource', 'ffmpeg.exe')
        else:
            return os.path.join(os.getcwd(), 'resource', 'ffmpeg.exe')

    @staticmethod
    def get_ffprobe_path():
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # 这是到_internal文件夹
            resource_dir = getattr(sys, '_MEIPASS')
            # 获取_internal上一级文件夹再拼接
            return os.path.join(os.path.dirname(resource_dir), 'resource', 'ffprobe.exe')
        else:
            return os.path.join(os.getcwd(), 'resource', 'ffprobe.exe')

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

    def get_video_duration(self, video_path) ->float:
        """获取视频时长"""
        ffprobe_path = self.get_ffprobe_path()
        if not os.path.exists(ffprobe_path):
            log.LOG.error("Wrong ffprobe path:"+ffprobe_path)
            return 0
        ffprobe_cmd = f'"{ffprobe_path}"  -i "{video_path}" -show_entries format=duration -v quiet -of csv="p=0"'
        p = subprocess.Popen(
            ffprobe_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
        print(ffprobe_cmd)
        out, err = p.communicate()
        if len(str(err, 'gbk')) > 0:
            print(f"subprocess 执行结果：out:{out} err:{str(err, 'gbk')}")
            return 0
        if len(str(out, 'gbk')) == 0:
            return 0
        return float(out)

    def decrypt_videos(self, exporter, start_date, end_date, dir_name, convert_video) -> None:
        """将视频文件从缓存中复制出来，重命名为{md5}_{duration}.mp4
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
                if not exporter.stop_flag:
                    try:
                        file_type = filetype.guess(file.resolve())
                        if file_type and file_type.extension == "mp4":
                            print("Process Video: "+str(file.resolve()))
                            md5 = self.calculate_md5(file.resolve())
                            print("video md5: "+md5)
                            duration = self.get_video_duration(str(file.resolve()))
                            print("video duration: " + str(duration))
                            # 是否需要将视频转码
                            if convert_video:
                                input_path = str(file.resolve())
                                ffmpeg_path = self.get_ffmpeg_path()
                                output_path = self.get_output_path(dir_name, md5, duration)
                                print("ffmpeg_path: " + str(ffmpeg_path))
                                if os.path.exists(ffmpeg_path):
                                    cmd = f'''"{ffmpeg_path}" -loglevel quiet -i "{input_path}" -c:v libx264 "{output_path}"'''
                                    print("ffmpeg_path cmd:" + cmd)
                                    subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            else:
                                shutil.copy(file.resolve(), f"output/{dir_name}/videos/{md5}_{duration}.mp4")
                    except Exception:
                        traceback.print_exc()
                processed_files = processed_files + 1
                # 15%的进度作为处理视频使用 + 15%(处理图像)
                progress = round(processed_files / total_files * 15 + 15)
                self.gui.update_export_progressbar(progress)
