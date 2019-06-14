with open('rosalind_dna.txt', 'r') as fin:
    string = fin.read()

count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for letter in string.strip():
    count[letter] += 1
print(count['A'], count['C'], count['G'], count['T'])
