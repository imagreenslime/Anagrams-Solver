from collections import deque
import numpy as np
import random
class gamepigeon:
    def main(self, letters, type):
        wordset = self.load_word_set()
        if type == "wordhunt":
            grid = self.wordhunt_maker(letters)
            valid = self.word_hunt_checker(grid,wordset)
        elif type == "anagrams":
            letters = self.anagram_maker(letters)
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
        letters = deque([])
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

    def wordhunt_maker(self, letters: str):
        grid = np.array([])
        for a in letters:
            grid = np.append(grid, [a])
        return (np.reshape(grid, (4, 4)))

    def anagram_maker(self, letters: str):
        return [letter for letter in letters]

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

    def word_hunt_checker(self, grid, wordbank):
        maxcol, maxrow = len(grid[0]), len(grid)
        sol = set()

        def dfs(word, col, row, wordbank, grid):
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

            newgrid = np.copy(grid)
            newgrid[col][row] = "0"
            neighbours = (col, row + 1), (col, row - 1), (col + 1, row), (col - 1, row), (col - 1, row - 1), (col + 1, row + 1), (col + 1, row - 1), (col - 1, row + 1)

            for a, b in neighbours:
                if 0 <= b < maxrow and 0 <= a < maxcol and newgrid[a][b] != "0":
                    dfs(word + newgrid[a][b], a, b, newbank, newgrid[:])

        for col in range(maxcol):
            for row in range(maxrow):
                dfs(grid[col][row], col, row, wordbank, grid)

        return sol
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




