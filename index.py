with open('file.txt', 'a') as file:
    while True:
        text = input('> ')
        file.write(text)
        if text == 'quit':
            break

print('bye !')
