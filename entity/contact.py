from dataclasses import dataclass


@dataclass
class Contact:
    userName: str
    alias: str
    type: int
    remark: str
    nickName: str
    pYInitial: str
    remarkPYInitial: str
    smallHeadImgUrl: str
    bigHeadImgUrl: str
    exTraBuf: str
    labelName: str
    latestTalkTime: int