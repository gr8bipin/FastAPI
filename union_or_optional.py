from typing import Optional

# Using Optional
def say_hi(name: Optional[str]):
    print(f"Hey {name}!")

say_hi(name= None)

# Using Union
def say_hi(name: str | None):
    print(f"Hey {name}!")

say_hi(name= None)