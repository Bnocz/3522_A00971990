import file_handler


class Dictionary:

    @staticmethod
    def word_search(word_dict, word_search):
        for key, value in word_dict.items():
            if word_search == key:
                print(value)


def main():
    '''
    Creates a Dictionary object, calls load_data to populate dictionary from
    a file. Allows user to search for words and returns their definition.
    '''
    jdict_ = Dictionary()
    print(f"Enter the name of the file you would like to open")
    file_path = input(">")

    jdict_ = file_handler.FileHandler.load_data(file_path)
    search_word = ""
    print(f"Enter a word you would like to search the definition for, enter quitprogram to quit")
    while search_word != 'quitprogram':
        search_word = input(">")
        Dictionary.word_search(jdict_, search_word.lower())
        if search_word.lower not in jdict_:
            Dictionary.word_search(jdict_, search_word.upper())
        else:
            print("Sorry we don't have that definition")


if __name__ == '__main__':
    main()
