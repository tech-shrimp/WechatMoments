import os
import sqlite3
import tkinter
import traceback

from pywxdump import decrypt
from log import LOG


class DatabaseDecrypter:

    def __init__(self, gui: 'Gui', db_path, key):
        self.db_path = db_path
        self.key = key
        self.gui = gui
        # 指定需要解密的数据库
        self.db_list = ["MicroMsg.db", "Misc.db", "MSG.db", "Sns.db"]
        self.db_list.extend([f"MSG{i}.db" for i in range(0, 50)])

    def merge_databases(self, source_paths, target_path):
        # 创建目标数据库连接
        target_conn = sqlite3.connect(target_path)
        target_cursor = target_conn.cursor()
        try:
            # 开始事务
            target_conn.execute("BEGIN;")
            for i, source_path in enumerate(source_paths):
                if not os.path.exists(source_path):
                    continue
                db = sqlite3.connect(source_path)
                db.text_factory = str
                cursor = db.cursor()
                try:
                    sql = '''
                        SELECT TalkerId,MsgsvrID,Type,SubType,IsSender,CreateTime,Sequence,StrTalker,StrContent,DisplayContent,BytesExtra,CompressContent
                        FROM MSG;
                    '''
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    # 附加源数据库
                    target_cursor.executemany(
                        "INSERT INTO MSG "
                        "(TalkerId,MsgsvrID,Type,SubType,IsSender,CreateTime,Sequence,StrTalker,StrContent,DisplayContent,"
                        "BytesExtra,CompressContent)"
                        "VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        result)
                except:
                    LOG.error(f'{source_path}数据库合并错误:\n{traceback.format_exc()}')
                cursor.close()
                db.close()
            # 提交事务
            target_conn.execute("COMMIT;")

        except Exception as e:
            # 发生异常时回滚事务
            target_conn.execute("ROLLBACK;")
            raise e

        finally:
            # 关闭目标数据库连接
            target_conn.close()

    def decrypt(self):

        output_dir = 'app/DataBase/Msg'
        os.makedirs(output_dir, exist_ok=True)
        tasks = []
        if os.path.exists(self.db_path):
            for root, dirs, files in os.walk(self.db_path):
                for file in files:
                    if '.db' == file[-3:] and file in self.db_list:
                        in_path = os.path.join(root, file)
                        output_path = os.path.join(output_dir, file)
                        tasks.append([self.key, in_path, output_path])
        for i, task in enumerate(tasks):
            flag, result = decrypt(*task)
            if not flag:
                LOG.error(result)
            progress = round((i+1) / len(tasks) * 100)
            self.gui.update_decrypt_progressbar(progress)

        target_database = "app/DataBase/Msg/MSG.db"
        # 源数据库文件列表
        source_databases = [f"app/DataBase/Msg/MSG{i}.db" for i in range(0, 50)]
        import shutil
        if os.path.exists(target_database):
            os.remove(target_database)
        try:
            shutil.copy2("app/DataBase/Msg/MSG0.db", target_database)  # 使用一个数据库文件作为模板
        except FileNotFoundError:
            LOG.error(traceback.format_exc())
        # 合并数据库
        try:
            self.merge_databases(source_databases, target_database)
        except FileNotFoundError:
            LOG.error(traceback.format_exc())
            LOG.error("数据库不存在\n请检查微信版本是否为最新")

        # 解密完成 放开下一步按钮
        self.gui.decrypt_note_text.set("复制成功，请点击下一步")
        self.gui.next_step_button.config(state=tkinter.NORMAL)


