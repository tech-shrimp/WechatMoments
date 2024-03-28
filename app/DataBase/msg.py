import os.path
import random
import sqlite3
import threading
import traceback
db_path = "./app/Database/Msg/MSG.db"
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
class Msg:
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

    def get_contact(self, contacts):
        """这里查了一遍聊天记录，根据聊天记录最后一条按时间
           对联系人进行排序
        """
        if not self.open_flag:
            return None
        try:
            lock.acquire(True)
            sql = '''select StrTalker, MAX(CreateTime) from MSG group by StrTalker'''
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        finally:
            lock.release()
        res = {StrTalker: CreateTime for StrTalker, CreateTime in res}
        contacts = [list(cur_contact) for cur_contact in contacts]
        for i, cur_contact in enumerate(contacts):
            if cur_contact[0] in res:
                contacts[i].append(res[cur_contact[0]])
            else:
                contacts[i].append(0)
        contacts.sort(key=lambda cur_contact: cur_contact[-1], reverse=True)
        return contacts

    def get_messages_calendar(self, username_):
        sql = '''
            SELECT strftime('%Y-%m-%d',CreateTime,'unixepoch','localtime') as days
            from (
                SELECT MsgSvrID, CreateTime
                FROM MSG
                WHERE StrTalker = ?
                ORDER BY CreateTime
            )
            group by days
        '''
        if not self.open_flag:
            print('数据库未就绪')
            return None
        try:
            lock.acquire(True)
            self.cursor.execute(sql, [username_])
            result = self.cursor.fetchall()
        finally:
            lock.release()
        return [date[0] for date in result]

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

