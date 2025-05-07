from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: Union[str, None] = None  # add = None to make it optional
    price: float = None
    tax: Union[float, None] = None


items = {
    1: Item(id=1, name="Foo", description="A very nice Item", price=10.00, tax=1.00),
    2: Item(id=2, name="Bar", description="A very nice Item", price=10.00, tax=1.00),
}
