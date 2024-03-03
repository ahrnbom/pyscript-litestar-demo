from math import pi
from litestar import Litestar, get, post, Controller
from litestar.response import Redirect
from litestar.static_files import create_static_files_router

from demo.client.models import ExampleModel

storage = {}


class DemoController(Controller):
    @post(path="/post_example")
    async def post_example(self, data: ExampleModel) -> ExampleModel:
        storage["text"] = data.text

        return ExampleModel(text="Success", number=123.456)

    @get(path="/get_example")
    async def get_example(self) -> ExampleModel:
        return ExampleModel(
            text=storage.get("text", "No previous text found on the server"), number=pi
        )

    @get(path="/")
    async def redirect(self) -> Redirect:
        return Redirect("/demo/index.html")


static = create_static_files_router(path="/demo", directories=["demo/client"])
app = Litestar(route_handlers=[DemoController, static])
