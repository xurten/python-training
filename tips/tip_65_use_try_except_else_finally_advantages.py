# Tip 65 use try except else finally advantages
# try-finally allows cleaning operations in code
# block else minimalise the try block, in this block, we can add extra operation when there is success

import json

UNDEFINED = object()


def divide_json(path):
    print('Open file')
    handle = open(path, 'r+')
    try:
        print('Read data')
        data = handle.read()
        print('Read json data')
        op = json.loads(data)
        print('Processing')
    except ZeroDivisionError:
        print('Exception handling')
        return UNDEFINED
    else:
        print('Extra operations after success of try')
    finally:
        print('Always execute this block')
        handle.close()
