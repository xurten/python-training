from typing import Union, List


def get_user_name(user_id: int) -> Union[str, None]:
    user_data = {
        1: "Alice",
        2: "Bob"
    }
    return user_data.get(user_id)


def convert_to_string(value: Union[int, float, bool]) -> str:
    return str(value)


def greet(name: Union[str, None] = None) -> str:
    if name is None:
        return "Hello, Stranger!"
    return f"Hello, {name}!"


def process_response(response: Union[str, List[str]]) -> List[str]:
    if isinstance(response, str):
        return [response]
    return response


if __name__ == '__main__':
    print(get_user_name(1))  # Output: "Alice"
    print(get_user_name(3))  # Output: None
    print(convert_to_string(10))  # Output: "10"
    print(convert_to_string(3.14))  # Output: "3.14"
    print(convert_to_string(True))  # Output: "True"
    print(greet())  # Output: "Hello, Stranger!"
    print(greet("Alice"))  # Output: "Hello, Alice!"
    print(process_response("Single response"))  # Output: ["Single response"]
    print(process_response(["Response 1", "Response 2"]))  # Output: ["Response 1", "Response 2"]
