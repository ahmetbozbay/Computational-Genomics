import random
file = open("inputt.txt", 'r')
# format dna as lines and make all uppercase
dna = [line.strip() for line in file]
dna = [seq.upper() for seq in dna]


def randomkmer(kmer):
    genom=["A","G","C","T"]
    randomgeneratedstring=""
    for i in range(kmer):
        temp = random.choice(genom)
        randomgeneratedstring = randomgeneratedstring+temp
    print(randomgeneratedstring)
    return randomgeneratedstring

def medianstringsearch(dna, kmer):
    iterations = []
    startpos = 0
    score = 0
    while True:
        if (len(dna) - startpos + 1) == len(kmer):
            break
        for i in range(len(kmer)):
            if dna[i+startpos] == kmer[i]:
                score+=1
        startpos+=1
        iterations.append(score)
        score = 0
    return iterations


def control():
    for i in range(len(dna)):
        print(dna[i])
        print (medianstringsearch(dna[i],randomkmer(10)))
        print("--------------------")

control()