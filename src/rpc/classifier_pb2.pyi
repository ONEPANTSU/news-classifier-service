from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class NewsClassificationRequest(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class NewsClassificationReply(_message.Message):
    __slots__ = ("categories",)
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, categories: _Optional[_Iterable[str]] = ...) -> None: ...
