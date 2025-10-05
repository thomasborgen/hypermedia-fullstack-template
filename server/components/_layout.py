import json
from typing import Annotated

from fastapi import Depends
from hypermedia import (
    Anchor,
    Body,
    Details,
    Div,
    Doctype,
    Element,
    ElementList,
    Head,
    Html,
    Link,
    ListItem,
    Main,
    Meta,
    SafeString,
    Script,
    Span,
    Summary,
    Title,
    UnorderedList,
)

from server.components import icon


def get_body() -> Body:
    """Create page base."""
    return Body(
        Div(id="indicator"),
        Div(id="toast_container", class_="toast toast-start toast-middle"),
        Main(id="main", slot="main"),
        hx_indicator="#indicator",
        hx_history="false",
        class_="h-full",
    )


def get_header_elements() -> SafeString:
    htmx_config = {
        "defaultSwapStyle": "innerHTML",
        "globalViewTransitions": True,
        "history": True,
        "refreshOnHistoryMiss": True,
        "allowNestedOobSwaps": True,
        # "historyCacheSize": 0,
    }

    return ElementList(
        Meta(charset="UTF-8"),
        Meta(
            name="viewport",
            content="width=device-width, initial-scale=1.0",
        ),
        Meta(name="htmx-config", content=json.dumps(htmx_config)),
        Link(rel="icon", href="/static/favicon.svg"),
        Link(
            href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css",
            rel="stylesheet",
            type="text/css",
        ),
        Script(src="https://cdn.tailwindcss.com"),
        Script(src="/static/javascript/htmx.min.js"),
        Script(src="/static/javascript/hx-json-form.js"),
        Script(src="/static/javascript/sounds.js"),
        Script(src="/static/javascript/hyperscript.js"),
    ).dump()


def get_html_base(body: Annotated[Body, Depends(get_body)]) -> Element:
    """Create the base page."""
    return ElementList(
        Doctype(),
        Html(
            Head(
                Title("my project - home"),
                slot="head",
            ),
            body,
            lang="no-nb",
            data_theme="cupcake",  # type: ignore
        ),
    )


def menu() -> UnorderedList:
    return UnorderedList(
        menu_item(
            title="Home",
            href="/",
            icon_name="house",
        ),
        class_="menu bg-base-200 w-72 sm:h-full md:h-[calc(100%-4rem)]",
    )


def menu_item(title: str, href: str, icon_name: str | None = None) -> Element:
    return ListItem(
        Anchor(
            icon(name=icon_name) if icon_name else "",
            Span(title),
            hx_get=href,
            hx_push_url="true",
            hx_target="#main",
            _="on click wait 100ms then call #close-drawer.click()",
        )
    )


def menu_group(title: str, icon_name: str, items: list[Element]) -> Element:
    return ListItem(
        Details(
            Summary(
                icon(name=icon_name),
                Span(title),
            ),
            UnorderedList(*items),
        ),
    )
