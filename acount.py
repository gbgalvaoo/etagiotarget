def a_count(string):
    a_counter = 0
    for char in string:
        if char == 'a':
            a_counter += 1
    if a_counter == 0:
        return False
    else:
        return a_counter
    
string = input("Type a word: ")
result = a_count(string)
if result:
    print(f"The word {string} contains {result} a's")
else:
    print(f"The word {string} does not contains a's")
