import antigravity

# mutable arguments
def append_to_list[T](value: T, my_list: list[T]= []) -> list[T]:
    my_list.append(value)
    return my_list


first_result = append_to_list(1)
print(first_result)


second_result = append_to_list(2)
print(second_result)

