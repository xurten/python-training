# Tip 9 do not use else after for or while loop

def bad_example():
    for i in []:
        print('Empty')
    else:
        print('Else')


def next_bad_example():
    while False:
        print('Hello')
    else:
        print('Else')


bad_example()
next_bad_example()