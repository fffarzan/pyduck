from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('./trnslt.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        with open('./trnslt-ja.txt', mode="w") as t_file:
            t_file.write(translation)

except FileNotFoundError as e:
    print('check your file path! ')