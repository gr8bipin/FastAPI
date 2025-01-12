from typing import Annotated

def say_hello(name: Annotated[str,"this is just metadata"], number: Annotated[int, 65] ) -> str:
    print(type(name))
    return f"Hello {name}"

print("Bipin")