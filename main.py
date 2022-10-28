import random
from dictgenerate import dictgenerate
from filegenerate import filegenerate
from gertext import gertext 


def main():
    g = gertext('voyna-i-mir.txt')
    d = dictgenerate(g)
    f = filegenerate(d, 'out.txt')
    f.outfilegenerate()


if __name__ == '__main__' :
    main()



