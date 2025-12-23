from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, StrEnum
from typing import Optional


class ItemType(StrEnum):
    BOOK = "book"
    MANGA = "manga"


class ReadStatus(StrEnum):
    UNREAD = "No leído"
    READING = "Leyendo"
    READ = "Leído"
    DROPPED = "Abandonado"


class CoverType(StrEnum):
    HARDCOVER = "Tapa dura"
    PAPERBACK = "Tapa blanda"
    VINYL = "Vinilo"
    DIGITAL = "Digital"
    OTHER = "Otro"


@dataclass(frozen=True, slots=True, kw_only=True)
class CollectionItem:
    title: str
    item_type: ItemType

    series: Optional[str] = None

    author: Optional[str] = None
    illustrator: Optional[str] = None
    editor: Optional[str] = None

    genre: Optional[str] = None
    subgenre: Optional[str] = None

    collection: Optional[str] = None
    publisher: Optional[str] = None
    edition: Optional[str] = None
    language: Optional[str] = None

    image: Optional[str] = None

    rating: Optional[float] = None
    read_status: Optional[ReadStatus] = None
    notes: Optional[str] = None
    cover: Optional[CoverType] = None

    tags: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not self.title or not self.title.strip():
            raise ValueError("title must be a non-empty string")

        if self.rating is not None and not (0 <= self.rating <= 10):
            raise ValueError("rating must be between 0 and 10")

    def with_tags(self, *tags: str) -> CollectionItem:
        normalized = tuple(t.strip() for t in tags if t and t.strip())
        merged = tuple(dict.fromkeys((*self.tags, *normalized)))
        return CollectionItem(**{**self.__dict__, "tags": merged})