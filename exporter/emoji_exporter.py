import re


class EmojiExporter:
    def __init__(self):
        pass

    @staticmethod
    def replace_emoji(text: str):
        replacement_rules = [
            {
                "pattern": re.compile(r'\[微笑\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_1@2x.png" id="微笑" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[发呆\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_4@2x.png" id="发呆" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[撇嘴\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_2@2x.png" id="撇嘴" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[色\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_3@2x.png" id="色" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[发呆\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_4@2x.png" id="发呆" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[得意\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_5@2x.png" id="得意" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[流泪\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_6@2x.png" id="流泪" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[害羞\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_7@2x.png" id="害羞" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[闭嘴\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_8@2x.png" id="闭嘴" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[睡\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_9@2x.png" id="睡" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[大哭\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_10@2x.png" id="大哭" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[尴尬\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_11@2x.png" id="尴尬" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[发怒\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_12@2x.png" id="发怒" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[调皮\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_13@2x.png" id="调皮" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[呲牙\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_14@2x.png" id="呲牙" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[惊讶\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_15@2x.png" id="惊讶" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[难过\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_16@2x.png" id="难过" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[抓狂\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_19@2x.png" id="抓狂" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[吐\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_20@2x.png" id="吐" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[偷笑\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_21@2x.png" id="偷笑" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[愉快\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_22@2x.png" id="愉快" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[白眼\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_23@2x.png" id="白 眼" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[傲慢\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_24@2x.png" id="傲慢" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[困\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_26@2x.png" id="困" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[惊恐\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_27@2x.png" id="惊恐" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[憨笑\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_29@2x.png" id="憨笑" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[悠闲\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_30@2x.png" id="悠闲" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[咒骂\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_32@2x.png" id="咒骂" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[疑问\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_33@2x.png" id="疑问" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[嘘\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_34@2x.png" id="嘘" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[晕\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_35@2x.png" id="晕" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[衰\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_37@2x.png" id="衰" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[骷髅\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_38@2x.png" id="骷髅" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[敲打\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_39@2x.png" id="敲打" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[再见\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_40@2x.png" id="再见" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[擦汗\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_41@2x.png" id="擦汗" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[抠鼻\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_42@2x.png" id="抠鼻" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[鼓掌\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_43@2x.png" id="鼓掌" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[坏笑\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_45@2x.png" id="坏笑" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[右哼哼\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_47@2x.png" id="右哼哼" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[鄙视\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_49@2x.png" id="鄙视" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[委屈\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_50@2x.png" id="委屈" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[快哭了\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_51@2x.png" id="快哭了" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[阴险\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_52@2x.png" id="阴险" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[亲亲\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_53@2x.png" id="亲亲" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[可怜\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_55@2x.png" id="可怜" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[Whimper\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_55@2x.png" id="可怜" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[笑脸\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Happy.png" id="笑脸" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[生病\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Sick.png" id="生病" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[脸红\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Flushed.png" id="脸红" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[破涕为笑\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Lol.png" id="破涕为笑" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[恐惧\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Terror.png" id="恐惧" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[失望\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/LetDown.png" id="失望" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[无语\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Duh.png" id="无语" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[嘿哈\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_04.png" id="嘿哈" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[捂脸\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_05.png" id="捂脸" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[奸笑\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_02.png" id="奸笑" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[机智\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_06.png" id="机智" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[皱眉\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_12.png" id="皱眉" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[耶\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_11.png" id="耶" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[吃瓜\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Watermelon.png" id="吃瓜" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[加油\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Addoil.png" id="加油" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[汗\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Sweat.png" id="汗" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[天啊\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Shocked.png" id="天啊" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[Emm\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Cold.png" id="Emm" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[社会社会\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Social.png" id="社会社会" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[旺柴\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Yellowdog.png" id="旺柴" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[好的\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/NoProb.png" id="好的" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[打脸\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Slap.png" id="打脸" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[哇\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Wow.png" id="哇" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[翻白眼\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Boring.png" id="翻白眼" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[666\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/666.png" id="666" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[让我看看\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/LetMeSee.png" id="让我看看" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[叹气\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Sigh.png" id="叹气" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[苦涩\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Hurt.png" id="苦涩" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[難受\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Hurt.png" id="苦涩" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[裂开\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Broken.png" id="裂开" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[嘴唇\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_66@2x.png" id="嘴唇" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[爱心\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_67@2x.png" id="爱心" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[心碎\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_68@2x.png" id="心碎" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[拥抱\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_79@2x.png" id="拥抱" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[强\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_80@2x.png" id="强" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[弱\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_81@2x.png" id="弱" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[握手\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_82@2x.png" id="握手" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[胜利\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_83@2x.png" id="胜利" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[抱拳\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_84@2x.png" id="抱拳" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[勾引\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_85@2x.png" id="勾引" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[拳头\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_86@2x.png" id="拳头" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[OK\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_90@2x.png" id="OK" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[合十\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Worship.png" id="合十" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[啤酒\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_58@2x.png" id="啤酒" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[咖啡]\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_61@2x.png" id="咖啡" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[蛋糕\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_69@2x.png" id="蛋糕" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[玫瑰\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_64@2x.png" id="玫 瑰" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[凋谢\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_65@2x.png" id="凋谢" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[菜刀\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_56@2x.png" id="菜刀" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[炸弹\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_71@2x.png" id="炸弹" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[便便\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_75@2x.png" id="便便" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[月亮\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_76@2x.png" id="月亮" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[太阳\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_77@2x.png" id="太阳" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[庆 祝\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Party.png" id="庆祝" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[礼物\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_78@2x.png" id="礼物" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[红包\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_09.png" id="红包" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[發\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_16.png" id="發" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[福\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/2_15.png" id="福" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[烟花\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Fireworks.png" id="烟花" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[爆竹\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/newemoji/Firecracker.png" id="爆竹" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[猪头\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_63@2x.png" id="猪头" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[跳跳\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_93@2x.png" id="跳跳" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[发抖\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_94@2x.png" id="发抖" class="emoji_img">'
            },
            {
                "pattern": re.compile(r'\[转圈\]'),
                "replacement": '<img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.2.8/assets/Expression/Expression_96@2x.png" id="转圈" class="emoji_img">'
            }]

        for rule in replacement_rules:
            pattern = rule.get("pattern")
            text = re.sub(pattern,  rule.get("replacement"), text)
        return text