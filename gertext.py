def gertext(filename: str) -> str:
    with open(filename,'r') as file:
            for line in file:
                yield line