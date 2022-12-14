import random
from dictgenerate import dictgenerate 


class filegenerate():

    def __init__(self, dictionary: dict, outfilename: str):
        self.stat: dict = dictionary
        self.__outfilename: str = outfilename


    def __random_char(self, char: str) -> str:  # type: ignore
        seq = self.stat[char]
        rnd = random.randint(0, sum(seq.values()))
        total = 0
        for k, v in seq.items():
            total += v
            if rnd <= total:
                return k
    
    def outfilegenerate(self):
        with open(self.__outfilename, 'w',encoding='utf-8') as file:
            keys = list(self.stat.keys())
            char: str = str(random.choice(keys))  # type: ignore
            for i in range(1000):
                file.write(char)
                char = self.__random_char(char)
                          
        