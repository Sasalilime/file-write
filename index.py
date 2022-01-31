from translate import Translator

translator = Translator(to_lang="ru", from_lang="fr", encoding='utf-8')

with open('file.txt', 'a') as file:
    while True:
        text = input('> ')
        if text == 'quit':
            break
        file.write(translator.translate(text) + '\n')
        file.flush()


print('bye !')
