import Levenshtein

# removing punctuations and numbers
sym_and_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", "."]

#removing stopwords


def tokenization(filename):
    total_words = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            for w in line:
                if w in sym_and_num:
                    line = line.replace(w, "")
            line = line.lower()
            words = line.split()
            total_words += words
    return total_words




def main():
    filename = "text.txt"
    total_words = tokenization(filename)
    print(total_words)



if __name__ == "__main__":
    main()