from typing import Iterable


def gertext(filename: str):
    with open(filename,'r',encoding='utf-8') as file:
            for line in file:
                yield line