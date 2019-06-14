with open('rosalind_rna.txt', 'r') as fin:
    string = fin.read()

result = ""
for letter in string:
    if letter == 'T':
        letter = 'U'
    result += letter
print(result)
