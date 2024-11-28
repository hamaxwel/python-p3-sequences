# sequences.py

def print_fibonacci(n):
    if n == 0:
        print([])
        return
    elif n == 1:
        print([0])
        return
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    print(fib_sequence)


my_list = [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]

try:
    my_list.remove('f')
except ValueError:
    print("'f' not in list.")

print(my_list)

my_list.sort()

print(my_list)

sliced_list = my_list[3:8]
print(sliced_list)

print(my_list.count(3))
print(my_list.index(2))

my_list.append(8)
my_list.insert(0, 9)
print(my_list)

my_list.remove(9)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

words = ['z', 'Word', 'This is a long sentence']
words.sort()
print(words)

people = [('Steve', 1), ('John', 2), ('Joe', 3)]
people.sort(key=lambda x: x[1])
print(people)

mixed_list = [1, 2, 3, 3, 4, 5, 6, 9, 4]
mixed_list.sort()
print(mixed_list)

mixed_types_list = [1, 2, 3, 3, 'e', 4, 5, 6, 9, 4]
try:
    mixed_types_list.sort()
except TypeError:
    print("Error: Cannot sort a list with mixed data types.")

print(mixed_types_list)

fib_sequence = print_fibonacci(10)
print(fib_sequence)
