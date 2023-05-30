my_list = ['apple', 'banana', 'orange', 'grape', 'mango', 'peach', 'kiwi']
result = ' '.join(my_list[:5])
result2="".join(my_list[:5])
char_count = len(result)
print(result)
print(char_count) # output: 31
print(result2)
print(len(result2))

for i in my_list:
    print(len(i))
