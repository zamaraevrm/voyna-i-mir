from gertext import gertext 

class dictgenerate(): 

    def __init__(self, filename: str):
        self.filename = filename
        self.__dictionary = dict()
        

    def __readfile(self):
        self.__dictionary = {' ' : {' ' :  0}}
        ger = gertext(self.filename)
        for line in ger:
            chars =  set(line) 
            for char in chars:
                if char not in self.__dictionary.keys():
                    self.__dictionary[char] = {c: line.count(char + c) for c in chars}
                else:
                    self.__dictionary[char] += {c: line.count(char + c) for c in chars}
    

    