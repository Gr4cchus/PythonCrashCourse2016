# Read entire file
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

# loop
print("\nloop through file object")
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())    # without rstrip invisible newlines print after each line

# Store list then work through list
print('\nStore as list to work through')
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
