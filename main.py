from nato_phonetic_alphabet import NatoPhonetic

def main()-> None:
    nato_phonetic = NatoPhonetic()
    user_name = input("Enter Name: ").upper()
    coded = nato_phonetic.code_given_word(user_name)
    print(coded)
    

if __name__ == "__main__":
    main()