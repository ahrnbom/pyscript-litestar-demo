from msgspec import Struct


class ExampleModel(Struct):
    """
    Demonstration of a data model used both in the server and client
    """

    text: str
    number: float
