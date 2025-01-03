# avoid using Optional[SomeType]
# Instead use Union[SomeType, None]

from typing import Optional

def say_hi(name: Optional[str]):
    print(f"Hey {name}!")

say_hi(name= None)