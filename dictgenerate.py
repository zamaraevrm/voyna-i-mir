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
                for c in chars:
                    if c in dictionary[char].keys():                    
                        dictionary[char][c] += line.count(char + c)
                    else:
                        dictionary[char][c] = line.count(char + c)
    return dictionary
    

    