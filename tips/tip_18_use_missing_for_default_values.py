# Tip 18 use __missing__() for default values


def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print('Cannot open file')
        raise


class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


path = 'profile_1234.png'
picture = Pictures()
handle = picture[path]
handle.seek(0)
image_data = handle.read()
