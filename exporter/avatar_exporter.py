import io
import os
from pathlib import Path

from PIL import Image


class AvatarExporter:
    def __init__(self, dir_name: str):
        self.dir_name = dir_name
        # 头像是否已保存好 Key: userName value: True/False
        self._saved_map = {}
        if not os.path.exists(f'output/{self.dir_name}/avatars/'):
            os.mkdir(f'output/{self.dir_name}/avatars/')

    def get_avatar_path(self, userName) -> str:
        if userName in self._saved_map:
            return f'avatars/{userName}.png'

        from app.DataBase import misc_db
        blob_data = misc_db.get_avatar_buffer(userName)
        self._saved_map[userName] = True
        if blob_data:
            image = Image.open(io.BytesIO(blob_data))
            image.save(f'output/{self.dir_name}/avatars/{userName}.png', 'PNG')
            return f'avatars/{userName}.png'
        else:
            return f'icons/empty-avatar.jpg'
