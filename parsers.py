class __Base(type):
    def _init__(cls, name, bases, attr, dict):
        print(cls)
        print(name)
        print(bases)
        print(attr_dict)
class BaseMetaClass








def __iter__(self):
    self.__cursor = 0
    return self

def __next__(self):
    if self.__cursor == len(self.__links):
        raise StopIteration
    try:
        return self.__links(self.__cursor)

    if __name__ = "__main__"

