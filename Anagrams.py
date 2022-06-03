import random
class anagrams:
    def main(self):
        valid = []
        letters = ["e","c","t","n","a","a"]
        #while len(valid) < 15:
        #letters = self.randomletters()
        wordset = self.load_word_set()
        valid = self.anagram_checker(letters,wordset)
        valid = (sorted(valid, key=len, reverse=True))
        for a in valid:
            print(a)

    def load_word_set(self):
        word_set = []
        with open("valid-words.txt", "r") as f:
            for line in f.readlines():
                word = line.strip().lower()
                word_set.append(word)

        return word_set

    def randomletters(self):
        letters = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        vowels = "euioa"
        vowelcount = random.randint(1, 3)
        for _ in range(vowelcount):
            vowel = random.randint(0, 4)
            letters.append(vowels[vowel])
        for _ in range(7 - len(letters)):
            letter = random.randint(0, 25)
            letters.append(alphabet[letter])
        return(letters)

    def anagram_checker(self, letters, wordbank):
        sol = set()

        def dfs(word, letts, wordbank):
            newbank = []
            for words in wordbank:
                if words in sol:
                    wordbank.remove(words)
                if words == word:
                    sol.add(word)
                elif words.startswith(word):
                    newbank.append(words)
            if not newbank:
                return

            for let in letts:
                temp = letts[:]
                temp.remove(let)
                dfs(word + str(let), temp, newbank)

        for a in letters:
            temporary = letters[:]
            temporary.remove(a)
            dfs(a, temporary, wordbank)

        return sol if sol else []

    def replacewords(self):
        word_set = []
        with open('valid-words.txt', 'r') as file:
            for line in file.readlines():
                word = line.strip().lower()
                if len(word) > 3:
                    word_set.append(word)
        with open('valid-words.txt', 'w') as files:
            new_line = '\n'.join(word_set)
            files.write(new_line)
sol = anagrams()
sol.main()




