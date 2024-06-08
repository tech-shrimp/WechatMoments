import json
from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime, timezone, timedelta

import xmltodict
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class Location:
    poiName: str = field(metadata=config(field_name="@poiName"), default="")
    longitude: str = field(metadata=config(field_name="@longitude"), default="")
    latitude: str = field(metadata=config(field_name="@latitude"), default="")
    country: str = field(metadata=config(field_name="@country"), default="")


@dataclass_json
@dataclass
class Url:
    type: str = field(metadata=config(field_name="@type"))
    text: str = field(metadata=config(field_name="#text"),  default="")
    md5: str = field(metadata=config(field_name="@md5"), default="")
    token: str = field(metadata=config(field_name="@token"), default="")
    enc_idx: str = field(metadata=config(field_name="@enc_idx"), default="")

@dataclass_json
@dataclass
class Thumb:
    type: str = field(metadata=config(field_name="@type"))
    text: str = field(metadata=config(field_name="#text"))
    token: str = field(metadata=config(field_name="@token"), default="")
    enc_idx: str = field(metadata=config(field_name="@enc_idx"), default="")


@dataclass_json
@dataclass
class Media:
    type: Optional[str] = None
    id: Optional[str] = None
    url: Optional[Url] | str = None
    thumb: Optional[Thumb] = None
    thumbUrl: Optional[str] = None
    videoDuration: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None

@dataclass_json
@dataclass
class MediaList:
    media: list[Media]



@dataclass_json
@dataclass
class FinderFeed:
    feedType: Optional[str] = ""
    nickname: Optional[str] = ""
    desc: Optional[str] = ""
    mediaList: Optional[MediaList] = None

@dataclass_json
@dataclass
class ContentObject:
    contentStyle: int
    contentUrl: Optional[str] = ""
    title: Optional[str] = ""
    description: Optional[str] = ""
    mediaList: Optional[MediaList] = None
    # 视频号消息
    finderFeed: Optional[FinderFeed] = None

@dataclass_json
@dataclass
class TimelineObject:
    username: str
    location: Location
    ContentObject: ContentObject
    createTime: int
    contentDesc: Optional[str] = ""

    @property
    def create_date(self):
        dt = datetime.fromtimestamp(self.createTime, timezone.utc)
        # 转换为北京时间（UTC+8）
        beijing_timezone = timezone(timedelta(hours=8))
        date = dt.astimezone(beijing_timezone).date()
        return date
    @property
    def create_time(self)->str:
        dt = datetime.fromtimestamp(self.createTime, timezone.utc)
        # 转换为北京时间（UTC+8）
        beijing_timezone = timezone(timedelta(hours=8))
        time_formatted = dt.astimezone(beijing_timezone).strftime('%Y-%m-%d %H:%M:%S')
        return time_formatted
    @property
    def create_year_month(self)->str:
        dt = datetime.fromtimestamp(self.createTime, timezone.utc)
        # 转换为北京时间（UTC+8）
        beijing_timezone = timezone(timedelta(hours=8))
        time_formatted = dt.astimezone(beijing_timezone).strftime('%Y-%m')
        return time_formatted


@dataclass_json
@dataclass
class MomentMsg:
    timelineObject: TimelineObject = field(metadata=config(field_name="TimelineObject"))




def test():

    xml = """
    """
    msg_dict = xmltodict.parse(xml.replace(chr(10), '').replace(chr(9), ''), force_list={'media'})
    msg_json = json.dumps(msg_dict, sort_keys=False, indent=2)
    momentMsg = MomentMsg.from_json(msg_json)
    print(momentMsg)

def test_time_convert():
    time = 1706592456
    dt = datetime.fromtimestamp(time, timezone.utc)
    # 转换为北京时间（UTC+8）
    beijing_timezone = timezone(timedelta(hours=8))
    beijing_time = dt.astimezone(beijing_timezone).strftime('%Y-%m-%d %H:%M:%S')
    print(beijing_time)

if __name__ == "__main__":
    test()
