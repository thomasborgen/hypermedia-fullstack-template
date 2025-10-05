from typing import Annotated

from fastapi import Depends
from hypermedia import Div, Element, Title

from server.components import get_html_base


def render_index_partial() -> Element:
    """Render only index form."""
    return Div("Hello world")


def render_index(
    partial: Annotated[Element, Depends(render_index_partial)],
    base: Annotated[Element, Depends(get_html_base)],
) -> Element:
    """Render the full page, with index form."""
    return base.extend("head", Title("My project Home")).extend(
        "main", partial
    )
