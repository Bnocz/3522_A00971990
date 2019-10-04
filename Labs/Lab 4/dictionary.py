import json
import file_handler
class Dictionary_:

    @staticmethod
    def testopen():
        with open("testdict.json", "r") as file:
            datastore = json.load(file)
            print(datastore)
    @staticmethod
    def word_search(word_dict, word_search):
        for key, value in word_dict.items():
            if word_search == key:
                print(value)

class InvalidKeyError(Exception):
    pass

def main():
    jdict_ = Dictionary_()
    jdict_ = file_handler.FileHandler.load_data("testdict.json")
    count = 0
    search_word = ""
    print(f"Enter a word you would like to search the definition for, enter quitprogram to quit")
    while search_word != 'quitprogram':
        search_word = input(">")
        Dictionary_.word_search(jdict_, search_word.lower())
        if search_word.lower not in jdict_:
            Dictionary_.word_search(jdict_, search_word.upper())
        else:
            print("Sorry, we don't have that definition.")


if __name__ == '__main__':
    main()