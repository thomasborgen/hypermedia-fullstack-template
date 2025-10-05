from enum import StrEnum

from hypermedia.models import BasicElement
from hypermedia.types.attributes import GlobalAttrs
from hypermedia.types.types import NoChildren, PrimitiveChildren
from typing_extensions import Unpack


class ToastLevel(StrEnum):
    SUCCESS = "success"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    NEUTRAL = "neutral"


class Toast(BasicElement[PrimitiveChildren, GlobalAttrs]):
    """Creates a Toast."""

    tag: str = "div"

    def __init__(
        self,
        *children: NoChildren,
        message: str,
        level: ToastLevel,
        **attributes: Unpack[GlobalAttrs],
    ) -> None:
        """Create a Toast that displays a message for 4 seconds."""
        attributes["class_"] = (
            attributes.get("class_", "")
            + f" alert alert-{level.value} px-2 text-wrap text-left"
        )
        attributes["_"] = attributes.get("_", "") + (
            "on load wait for 4s then transition opacity to 0 then remove me"
        )

        super().__init__(
            message,
            **attributes,
        )
