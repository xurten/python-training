# Tip 20 use exceptions than none value


def bad_example():
    def careful_divide(a, b):
        try:
            return True, a / b
        except ZeroDivisionError:
            return False, None

    success, result = careful_divide(10, 0)
    if not success:
        print('Bad input data')

    _, result = careful_divide(150, 10)
    if not success:
        print('Bad input data')


def good_example():
    def careful_divide(a: float, b: float) -> float:
        try:
            return a / b
        except ZeroDivisionError as e:
            raise ValueError('Bad input data')

    try:
        result = careful_divide(10, 0)
    except ValueError:
        print('Do not divide by 0')
    print(result)


bad_example()
good_example()
