import math


def binary_genre(signes: list):
    bits = math.ceil(math.log2(len(signes)))
    assignment = {}
    for i in range(len(signes)):
        new_bin = bin(i)[2:]
        while len(new_bin) < bits:
            new_bin = '0' + new_bin
        assignment[new_bin] = signes[i]
    return assignment

def decompress(filename):
   with open(filename, 'r', encoding='latin') as file:
       all = file.readlines()
       to_this = len(all) - 1
       counterek = 0
       for allek in all:
           bits = ''
           if counterek == 0:
               dict_length = int(ord(allek[0]))
               signes = allek[1:dict_length+1]
               legend = binary_genre(signes)
               pudding = bin(ord(allek[dict_length+1]))[2:]
               while len(pudding) < 8:
                   pudding = '0' + pudding
               bits=pudding[3:]
               pudding = pudding[:3]
               pudding = int(pudding, 2)
           for i in allek[dict_length+2:]:
               tempcokolwiek=bin(ord(i))[2:]
               while len(tempcokolwiek) < 8:
                   tempcokolwiek = '0' + tempcokolwiek
               bits += tempcokolwiek
           if counterek == to_this:
               bits = bits[:-pudding]
           with open('decompressed.txt', 'a', encoding='utf-8') as nfile:
               sign = ''
               for i in bits:
                   sign += i
                   if len(sign) % len(list(legend.keys())[0]) == 0:
                       nfile.write(legend[sign])
                       sign = ''
           counterek += 1



def main():
    path = input("enter the file name:")
    decompress(path)

    #decompress(all)
    '''
    print(len(new))
    with open('decompressed.txt', 'w', encoding='utf-8') as nfile:
        for i in new:
            nfile.write(i)
    '''

main()