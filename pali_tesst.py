class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word = word.lower()
        return list(word) == list(reversed(word))

print(Palindrome.is_palindrome('Deleveled'))