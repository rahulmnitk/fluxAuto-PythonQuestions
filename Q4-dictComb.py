# Program to list all the combinations 
# of the elements from a dictionary 
# using itertools module
import itertools

# Function to form pairs of elements 
# using the itertools.product method
def combos(Dict):
    l = []
    for pair in itertools.product(*[Dict[i] for i in sorted(Dict.keys())]):
        l.append("".join(pair))
    return l

x = {'1':['a','b'], '2':['c','d']}
comb_x = combos(x)
print(comb_x)

y = {'1':['a', 'b', 'c'], '2':['c', 'd', 'e'], '3': ['f', 'g', 'h']}
comb_y = combos(y)
print(comb_y)


