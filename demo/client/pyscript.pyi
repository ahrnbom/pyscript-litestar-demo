from typing import Any, Optional

class Element:
    """
    Represents a HTML elements
    """

    innerHTML: str

class Document:
    """
    Represents an HTML document
    """

    def getElementById(self, s: str) -> Element:
        """
        Obtains an HTML element given an id
        """
        ...

class Response:
    """
    Represents a response from an HTTP request
    """

    ok: bool
    status: int
    async def text(self) -> str:
        """
        Obtains a string representation of a response
        """
        ...

class Window:
    """
    Represents the browser window and provides access to Web APIs
    """

    async def fetch(self, resource: str, options: Any) -> Response:
        """
        Performs an HTTP call
        """
        ...

document = Document()
window = Window()
