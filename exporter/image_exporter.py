import os
import re
from typing import Tuple, Optional

from entity.moment_msg import MomentMsg, Media
import requests
import uuid


class ImageExporter:
    def __init__(self, dir_name: str):
        self.dir_name = dir_name
        if not os.path.exists(f'output/{self.dir_name}/thumbs/'):
            os.mkdir(f'output/{self.dir_name}/thumbs/')
        if not os.path.exists(f'output/{self.dir_name}/images/'):
            os.mkdir(f'output/{self.dir_name}/images/')

    def save_image(self, url: str, img_type: str) -> str:
        """ 下载图片
        """
        if not (img_type == 'image' or img_type == 'thumb'):
            raise Exception("img_type 参数非法")
        file_name = uuid.uuid4()
        response = requests.get(url)
        if response.ok:
            with open(f'output/{self.dir_name}/{img_type}s/{file_name}.jpg', 'wb') as file:
                file.write(response.content)
            return f'{img_type}s/{file_name}.jpg'

    def get_images(self, msg: MomentMsg, download_pic: int) -> list[Tuple]:
        """ 获取一条朋友圈的全部图像， 返回值是一个元组列表
            [(缩略图路径，原图路径)，(缩略图路径，原图路径)]
        """
        results = []
        if not msg.timelineObject.ContentObject.mediaList:
            return results

        media = msg.timelineObject.ContentObject.mediaList.media
        for media_item in media:
            if media_item.type == "2":
                if download_pic:
                    thumb_path = self.save_image(media_item.thumb.text, 'thumb')
                    image_path = self.save_image(media_item.url.text, 'image')
                else:
                    thumb_path = media_item.thumb.text
                    image_path = media_item.url.text
                if thumb_path and image_path:
                    results.append((thumb_path, image_path))

        return results

    def get_finder_images(self, msg: MomentMsg) -> Optional[str]:
        """ 获取视频号的封面图
        """
        results = None
        if not msg.timelineObject.ContentObject.finderFeed:
            return results

        if not msg.timelineObject.ContentObject.finderFeed.mediaList:
            return results

        media = msg.timelineObject.ContentObject.finderFeed.mediaList.media
        for media_item in media:
            thumb_path = self.save_image(media_item.thumbUrl, 'thumb')
            return thumb_path
