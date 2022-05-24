import random

bit = int(8)
num = int(2)

while bit != 8192:
        i = num**bit
        number = random.randint(0, i-1)
        print(bit,"-rand:",number)
        bit = bit * 2
        
