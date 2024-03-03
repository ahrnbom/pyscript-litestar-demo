from typing import Any, TypeVar
from pyscript import document, window
import asyncio
import msgspec

from demo.client.models import ExampleModel

T = TypeVar("T")

a = ExampleModel(text="some example text", number=123)

div = document.getElementById("output")
div.innerHTML = "Please wait..."


async def http_get(path: str, return_type: type[T]) -> T:
    """
    Performs an HTTP GET call, expecting JSON that can be converted to a given msgspec model
    """
    response = await window.fetch(path, cache="no-cache", method="GET")
    contents = await response.text()
    response_data = msgspec.json.decode(contents, type=return_type)
    return response_data


async def http_post(path: str, data: Any, return_type: type[T]) -> T:
    """
    Performs an HTTP POST call, expecting JSON that can be converted to a given msgspec model.
    The data argument should be an instance of some msgspec model, which will be provided
    as the body of the HTTP call, formatted as JSON.
    """
    json_bytes = msgspec.json.encode(data)
    json_str = json_bytes.decode("utf-8")

    """
    This call here is somewhat strange. 
    In Javascript, the corresponding fetch call would look like:
    fetch(path, {
        body: json_str,
        cache: "no-cache",
        method: "POST"
    });
    but Pyscript instead expects the options to be provided as kwargs.
    Changing this call below to provide the options as a dictionary will not work.
    To try this, you also need to modify the .pyi file, or disable mypy.
    """
    response = await window.fetch(
        path,
        body=json_str,
        cache="no-cache",
        method="POST",
    )

    contents = await response.text()
    response_data = msgspec.json.decode(contents, type=return_type)
    return response_data


async def example():
    ex = ExampleModel(text="F1RST POST LOL", number=147.963)
    out1 = await http_post("/post_example", ex, ExampleModel)
    out2 = await http_get("/get_example", ExampleModel)
    div.innerHTML = f"Output from POST: {out1.text} {out1.number:.2f}<br>Output from GET: {out2.text} {out2.number:.2f}"


asyncio.create_task(example())
