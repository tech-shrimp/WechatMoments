import os
from io import BytesIO
from pathlib import Path
from typing import Tuple, Optional
from PIL import Image
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

    @staticmethod
    def get_image(link: tuple) -> bytes:
        """ 向微信服务器请求图片
        """
        url, idx, token = link
        # 如果需要传递token
        if idx and token:
            url = f'{url}?idx={idx}&token={token}'
        response = requests.get(url)
        if response.ok:
            return response.content

    def save_image(self, link: tuple, img_type: str) -> str:
        """ 下载图片
        """
        file_name = uuid.uuid4()
        if not (img_type == 'image' or img_type == 'thumb'):
            raise Exception("img_type 参数非法")
        content = self.get_image(link)
        if content:
            with open(f'output/{self.dir_name}/{img_type}s/{file_name}.jpg', 'wb') as file:
                file.write(content)
            return f'{img_type}s/{file_name}.jpg'

    @staticmethod
    def get_image_thumb_and_url(media_item, content_style:int) -> Tuple[Tuple, Tuple]:
        """ 获取图片的缩略图与大图的链接
        """
        thumb = None
        url = None
        # 普通图片
        if media_item.type == "2":
            thumb = (media_item.thumb.text, media_item.thumb.enc_idx, media_item.thumb.token)
            url = (media_item.url.text, media_item.url.enc_idx, media_item.url.token)
        # 微信音乐
        if media_item.type == "5":
            thumb = (media_item.thumb.text, "", "")
            url = (media_item.thumb.text, "", "")
        # 超链接类型
        if content_style == 3:
            thumb = (media_item.thumb.text, "", "")
            url = (media_item.thumb.text, "", "")

        return thumb, url

    def get_images(self, msg: MomentMsg) -> list[Tuple]:
        """ 获取一条朋友圈的全部图像， 返回值是一个元组列表
            [(缩略图路径，原图路径)，(缩略图路径，原图路径)]
        """
        results = []
        if not msg.timelineObject.ContentObject.mediaList:
            return results

        media = msg.timelineObject.ContentObject.mediaList.media
        for media_item in media:
            thumb, url = self.get_image_thumb_and_url(media_item, msg.timelineObject.ContentObject.contentStyle)
            if thumb and url:
                thumb_path = None
                image_path = None
                # 主图内容
                image_content = self.get_image(url)
                # 如果拿不到主图数据
                if not image_content:
                    continue
                # 如果在腾讯服务器获取到jpg图片
                if image_content[:2] == b'\xff\xd8':
                    file_name = uuid.uuid4()
                    with open(f'output/{self.dir_name}/images/{file_name}.jpg', 'wb') as file:
                        file.write(image_content)
                    image_path = f'images/{file_name}.jpg'
                    # 缩略图内容
                    thumb_content = self.get_image(thumb)
                    file_name = uuid.uuid4()
                    with open(f'output/{self.dir_name}/thumbs/{file_name}.jpg', 'wb') as file:
                        file.write(thumb_content)
                    thumb_path = f'thumbs/{file_name}.jpg'
                # 如果图片已加密，进入缓存图片中匹配
                else:
                    # 获取2024-06格式的时间
                    month = msg.timelineObject.create_year_month
                    image_content = self.get_image(url)
                    thumb_content = self.get_image(thumb)
                    # 从缓存里找文件
                    image_file = Path((f"output/{self.dir_name}/images/{month}/"
                                       f"{len(image_content)}_{len(thumb_content)}.jpg"))
                    thumb_file = Path((f"output/{self.dir_name}/thumbs/{month}/"
                                       f"{len(image_content)}_{len(thumb_content)}.jpg"))
                    if image_file.exists():
                        image_path = image_file.resolve()
                    if thumb_file.exists():
                        thumb_path = thumb_file.resolve()

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
            thumb_path = self.save_image((media_item.thumbUrl, "", ""), 'thumb')
            return thumb_path
