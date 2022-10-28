from gertext import gertext 
       
def dictgenerate(generator) -> dict:
    ger = generator
    dictionary = dict()
    for line in ger:
        chars =  set(line) 
        for char in chars:
            if char not in dictionary.keys():
                dictionary[char] = {c: line.count(char + c) for c in chars}
            else:
                dictionary[char] = {c: line.count(char + c) for c in chars}
    return dictionary
    

    