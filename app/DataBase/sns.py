import os.path
import random
import sqlite3
import threading
import traceback
from typing import Optional

db_path = "./app/Database/Msg/Sns.db"
lock = threading.Lock()


def is_database_exist():
    return os.path.exists(db_path)


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner

@singleton
class Sns:
    def __init__(self):
        self.DB = None
        self.cursor = None
        self.open_flag = False
        self.init_database()

    def init_database(self, path=None):
        global db_path
        if not self.open_flag:
            if path:
                db_path = path
            if os.path.exists(db_path):
                self.DB = sqlite3.connect(db_path, check_same_thread=False)
                # '''创建游标'''
                self.cursor = self.DB.cursor()
                self.open_flag = True
                if lock.locked():
                    lock.release()

    def get_messages_in_time(self, start_time, end_time):
        if not self.open_flag:
            return None
        try:
            lock.acquire(True)
            sql = '''select UserName, Content, FeedId from FeedsV20  where CreateTime>=?
                  and  CreateTime<=? order by CreateTime desc'''
            self.cursor.execute(sql, [start_time, end_time])
            res = self.cursor.fetchall()
        finally:
            lock.release()

        return res

    def get_comment_by_feed_id(self, feed_id):
        if not self.open_flag:
            return None
        try:
            lock.acquire(True)
            sql = '''select FromUserName, CommentType, Content from CommentV20 where FeedId=?
                   order by CreateTime desc'''
            self.cursor.execute(sql, [feed_id])
            res = self.cursor.fetchall()
        finally:
            lock.release()
        return res

    def get_cover_url(self) -> Optional[str]:
        if not self.open_flag:
            return None
        try:
            lock.acquire(True)
            sql = '''select StrValue from SnsConfigV20 where Key="6"  '''
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                return result[0][0]
        finally:
            lock.release()
        return None


    def close(self):
        if self.open_flag:
            try:
                lock.acquire(True)
                self.open_flag = False
                self.DB.close()
            finally:
                lock.release()

    def __del__(self):
        self.close()


if __name__ == '__main__':
    pass
