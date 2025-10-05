from hypermedia import Element, I


def icon(*, name: str, size: str = "24px", classes: str = "") -> Element:
    """Create a I(italic) element with a material icon."""
    return I(
        name,
        classes=["material-icons", "flex", classes],
    )


def icon_outlined(
    *, name: str, size: str = "24px", classes: str = ""
) -> Element:
    """Create a I(italic) element with a material icon."""
    return I(
        name,
        classes=["material-symbols-outlined", "flex"],
    )
