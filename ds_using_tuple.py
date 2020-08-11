zoo = ('python', 'elephant', 'penguin')
print(zoo)
print('Number of animals in the zoo', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print(new_zoo)

print('Number of cages in the new zoo', len(new_zoo))
print('Animals brought from the old zoo', new_zoo[2])
print('Last animal bought from old zoo', new_zoo[2][2])
print('Number of animals in the zoo is', len(new_zoo) - 1 + len(new_zoo[2]))
