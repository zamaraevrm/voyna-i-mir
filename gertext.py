def gertext(filename: str) -> str:
    with open(filename) as file:
            for line in file:
                yield line