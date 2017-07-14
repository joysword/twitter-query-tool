import os.path


def exist(_type, _name):
    return os.path.isfile(os.path.join('static', 'json', _type, _name+'.json'))


def get_file(_type, _name):
    return os.path.join('static', 'json', _type,  _name+'.json')
