#https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
import string


def top_3_words(text: str):
    def remove_redundant(txt: str):
        filtered = filter(lambda x: x if x in "'-" or x not in string.punctuation else False, txt)
        return ''.join(filtered).lower()

    def to_dictionary(txt: str):
        filtered = remove_redundant(txt).split()
        return dict((word, filtered.count(word)) for word in filtered
                    if any(x.isalpha() for x in word))

    dictionary = to_dictionary(text)
    return sorted(dictionary, key=dictionary.get, reverse=True)[:3]


def test():
    sample = "Ugh, heck-darn why won't my code run?"
    result = top_3_words(sample)
    print(f"result -> {result}")
    print("valid" if result == ["a", "of", "on"] else "invalid")


if __name__ == '__main__':
    test()
