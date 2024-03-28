import math
import os
import re
from pathlib import Path
from entity.moment_msg import MomentMsg, Media


class VideoExporter:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        if not os.path.exists(f'output/{self.dir_name}/videos/'):
            os.mkdir(f'output/{self.dir_name}/videos/')


    def find_video_by_md5(self, md5):
        """
        使用MD5匹配视频
        """
        folder_path = Path(f'output/{self.dir_name}/videos/')
        pattern = re.compile(r'^(.*?)(?=_)')

        for file_path in folder_path.iterdir():
            match = pattern.search(file_path.name)
            if match:
                filename_md5 = match.group()
                if filename_md5 == md5:
                    return file_path.name

    def find_video_by_duration(self, duration):
        """
        使用视频时长匹配视频
        """
        folder_path = Path(f'output/{self.dir_name}/videos/')
        pattern = re.compile(r'_([0-9.]+)\.mp4')

        for file_path in folder_path.iterdir():
            match = pattern.search(file_path.name)
            if match:
                filename_duration = float(match.group(1))
                if math.isclose(filename_duration, duration, abs_tol=0.005):
                    return file_path.name

    def get_videos(self, msg: MomentMsg) -> list[str]:
        """ 获取一条朋友圈的全部视频， 返回值是一个文件路径列表
        """
        results = []
        if not msg.timelineObject.ContentObject.mediaList:
            return results

        media = msg.timelineObject.ContentObject.mediaList.media
        for media_item in media:
            if media_item.type == "6":
                duration = media_item.videoDuration
                rounded_duration = round(float(duration), 2)
                # 先用MD5匹配缓存中的视频
                # 如果找不到使用视频时长再次匹配
                video = self.find_video_by_md5(media_item.url.md5)
                if video:
                    results.append(f'videos/{video}')
                else:
                    video = self.find_video_by_duration(rounded_duration)
                    if video:
                        results.append(f'videos/{video}')

        return results
