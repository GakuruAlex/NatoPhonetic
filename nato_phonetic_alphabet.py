import pandas as pd

class NatoPhonetic:
    def nato_phonetic(self)-> dict:
        """_Read the csv file and process the data into a dictionary of letter as key and code as value_

        Returns:
            dict: _A dictionary of letter code pair _
        """
        phonetic_data = pd.read_csv("nato_phonetic_alphabet.csv")

        phonetic_data_dict = {row.letter: row.code for (index,row) in phonetic_data.iterrows()}
        print(phonetic_data_dict)

        return phonetic_data_dict
    def code_given_word(self, word: str) -> list:
        """_Given a word , process and return equivalent phonetics for that word_

        Args:
            word (str): _Given word_

        Returns:
            list: _A list of the phonetic equivalent of given word_
        """
        data = self.nato_phonetic()
        coded = [data[letter] for letter in word]
        return coded
