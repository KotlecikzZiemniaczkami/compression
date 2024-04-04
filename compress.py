import math

def counting(texty):
    signes = []
    for text in texty:
        for i in text:
            if i not in signes:
                signes.append(i)
        return signes

# checking how many bits is needed
def power_of_2(num):
    power = 1
    bit_amount = 1
    while power < int(num):
        bit_amount += 1
        power *= 2
    return bit_amount

# generating the legend
def binary_genre(signes: list, amount):
    bits = math.ceil(math.log2(len(signes)))
    assignment = {}
    for i in range(len(signes)):
        new_bin = bin(i)[2:]
        while len(new_bin) < bits:
            new_bin = '0' + new_bin
        assignment[signes[i]] = new_bin
    return assignment

def amounty(texty):
    length = 0
    for text in texty:
        length += len(text)
    return length
def compress(texty):
    signes = counting(texty)
    amount = amounty(signes)
    legend = binary_genre(signes, amount)
    compressed = chr(amount) + ''.join(list(legend.keys()))
    befores = []
    for text in texty:
        before = ''
        for i in text:
            before += legend[i]
        befores.append(before)
    how_many = (8-(3+amounty(befores)*amount)%8)%8
    for i in range(how_many):
        befores[-1] = befores[-1] + '0'
    bin_how_many = "{0:b}".format(how_many)
    print(bin_how_many)
    while len(bin_how_many) != 3:
        bin_how_many = '0' + bin_how_many
    print('how_manu:' ,how_many)
    befores[0] = bin_how_many + befores[0]
    with open('compressed.txt', 'a', encoding='latin') as nfile:
        nfile.write(compressed)
        for before in befores:
            to_add = ''
            for i in before:
                to_add += i
                if len(to_add) % 8 == 0:
                    nfile.write(chr(int(to_add,2)))
                    # print(to_add)
                    to_add = ''



def main():
    path = input("enter the file name:")
    with open(path, 'r') as file:
        new = file.readlines()
        compress(new)


main()