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
    search_word = input("Enter a word to search for: ")
    try:
        Dictionary_.word_search(jdict_, search_word)
        if search_word not in jdict_:
    except InvalidKeyError:

if __name__ == '__main__':
    main()