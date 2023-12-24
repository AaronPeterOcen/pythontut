from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open("./test.txt", mode="r") as file:
        text = file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("check your file path")
