from dataclasses import dataclass


@dataclass
class Comment:
    from_user_name: str
    comment_type: int
    content: str
