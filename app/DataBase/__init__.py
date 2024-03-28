# -*- coding: utf-8 -*-
"""
@File    : __init__.py.py
@Author  : Shuaikang Zhou
@Time    : 2023/1/5 0:10
@IDE     : Pycharm
@Version : Python3.10
@comment : ···
"""
from .micro_msg import MicroMsg
from .misc import Misc
from .msg import Msg
from .sns import Sns

misc_db = Misc()
msg_db = Msg()
micro_msg_db = MicroMsg()
sns_db = Sns()


__all__ = ['misc_db', 'micro_msg_db', 'msg_db', "sns_db"]
