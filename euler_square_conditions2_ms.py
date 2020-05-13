import random
from collections import deque

class Cell():
    def __init__(self):
        self.letter = ""
        self.number = ""
        
    #def __init__(self, letter, number):
    #    self.letter = letter
    #    self.number = number

    def get_letter(self):
        return self.letter

    def get_number(self):
        return self.number

    def set_letter(self, letter):
        self.letter = letter

    def set_number(self, number):
        self.number = number
        
    # def __getitem__(self, index):
        # return self[index]

    def __eq__(self, other):
        if self.letter == other.letter and self.number == other.number:
            # raise ValueEqualityError
            return True
        else:
            return False

    def __str__(self):
        return f"{self.get_letter()}{self.get_number()}"
        
# class Error(Exception):
    # """Base class for exceptions in this module."""
    # pass
    
# class ValueEqualityError(Error):
    # """Exception raised for equal values in a grid."""
    # pass

class Grid():
    def __init__(self, n):
        self.n = n
        self.grid = [Cell() for i in range(n*n)]

    def print_grid(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[self.n*i+j], end=" ")
            print()
    
class EulerSquare(Grid):
    def __init__(self, n):
        super().__init__(n)
        self.letters = list("abcdefghijklmnopqrstuvwxyz")[:n]
        self.numbers = [str(i) for i in range(26)][:n]

    def print_alphabets(self):
        print(self.letters)
        print(self.numbers)

    def make_square(self):
        for i in range(self.n):
            random_letters = self.letters.copy()
            random.shuffle(random_letters)
            random_numbers = self.numbers.copy()
            random.shuffle(random_numbers)
            for j in range(self.n):
                letter = random_letters.pop()
                self.grid[self.n*i+j].set_letter(letter)
                number = random_numbers.pop()
                self.grid[self.n*i+j].set_number(number)
                
    def make_square_conditions_v3(self):
        column_list_letters = [[] for i in range(self.n)]
        column_list_numbers = [[] for i in range(self.n)]
        random_letters = self.letters.copy()
        random.shuffle(random_letters)
        random_numbers = self.numbers.copy()
        random.shuffle(random_numbers)
        random_letters = deque(random_letters)
        random_numbers = deque(random_numbers)
        for i in range(self.n):
            random_letters.rotate(1)
            random_numbers.rotate(1)
            while True:
                if random_letters[0] not in column_list_letters[0]:
                    for j in range(self.n):
                        self.grid[self.n*i+j].set_letter(random_letters[j])
                        column_list_letters[j].append(random_letters[j])
                    break
                else:
                    random_letters.rotate(1)
            while True:
                if random_numbers[0] not in column_list_numbers[0]:
                    for j in range(self.n):
                        # try:
                            # self.grid[self.n*i+j].set_number(random_numbers[j])
                            # column_list_numbers[j].append(random_numbers[j])
                        # except ValueEqualityError:
                            # random_numbers.rotate(1)
                        self.grid[self.n*i+j].set_number(random_numbers[j])
                        # if 1 != self.grid.count(self.grid[self.n*i+j]):
                            # random_numbers.rotate(1)
                            # break
                        column_list_numbers[j].append(random_numbers[j])
                    if 1 != self.grid.count(self.grid[self.n*i+j]):
                        random_numbers.rotate(1)
                        for sublist in column_list_numbers:
                            del sublist[i]
                        continue                      
                    break
                else:
                    random_numbers.rotate(1)
                        
                
    def make_square_conditions(self):
        column_list_letters = [[] for i in range(self.n)]
        column_list_numbers = [[] for i in range(self.n)]
        row_list_letters = [[] for i in range(self.n)]
        row_list_numbers = [[] for i in range(self.n)]
        for i in range(self.n):
            letters = self.letters.copy()
            numbers = self.numbers.copy()
            while True:
                for j in range(self.n):
                    for letter in letters:
                        if letter not in column_list_letters[j]:
                            self.grid[self.n*i+j].set_letter(letter)
                            column_list_letters[j].append(letter)
                            row_list_letters[i].append(letter)
                            letters.remove(letter)
                            break
                if len(row_list_letters[i]) < self.n:
                    letters = deque(self.letters.copy())
                    letters.rotate(-(self.n-1))
                    # letters = letters[-1:] + letters[:-1]
                    row_list_letters[i].clear()
                    for sublist in column_list_letters:
                        try:
                            del sublist[i]
                        except IndexError:
                            pass
                else:
                    break
            while True:
                for j in range(self.n):
                    for number in numbers:
                        if number not in column_list_numbers[j]:
                            self.grid[self.n*i+j].set_number(number)
                            if 1 != self.grid.count(self.grid[self.n*i+j]):
                                continue
                            column_list_numbers[j].append(number)
                            row_list_numbers[i].append(number)
                            numbers.remove(number)
                            break
                if len(row_list_numbers[i]) < self.n:
                    numbers = deque(self.numbers.copy())
                    numbers.rotate(-(self.n-1))
                    # numbers = numbers[-1:] + numbers[:-1]
                    row_list_numbers[i].clear()
                    for sublist in column_list_numbers:
                        try:
                            del sublist[i]
                        except IndexError:
                            pass
                else:
                    break

    def __check_diagonal__(self):
        left_diagonal = []
        right_diagonal = []
        for i in range(self.n):
            left_diagonal.append(self.grid[i+i*self.n])
            right_diagonal.append(self.grid[(self.n*i)+(self.n-1-i)])
        for letter, number in left_diagonal:
            if 1 != left_diagonal.count(letter) or 1 != left_diagonal.count(number):
                return False
        for cell in right_diagonal:
            if 1 != right_diagonal.count(letter) or 1 != right_diagonal.count(number):
                return False
        return True
        
    def is_valid(self):
        # self.__check_diagonal__()
        for i in range(self.n):
            for x in range(1, self.n-i):
                for j in range(self.n):
                    #print(x, i, j)
                    #if self.grid[self.n*i+j] == self.grid[(self.n*i+j)+1]:
                        #return False
                    if self.grid[self.n*i+j].get_letter() == self.grid[(self.n*(i+x)+j)].get_letter() or \
                        self.grid[self.n*i+j].get_number() == self.grid[(self.n*(i+x)+j)].get_number():
                        if i != self.n - 1:
                            return False
                    if 1 != self.grid.count(self.grid[self.n*i+j]):
                        return False
        return True

        
new_square = EulerSquare(23)
# while True:
    # new_square.make_square_conditions()
    # if new_square.is_valid():
        # print("found it!")
        # new_square.print_grid()
        # break
        
new_square.make_square_conditions_v3()
if new_square.is_valid():
    print("Found it!")
    new_square.print_grid()
else:
    print("Fix code!")
    new_square.print_grid()

# new_square.make_square()        
# new_square.print_grid()
# print(new_square)
        
# new_square.grid[0].set_letter("b")
# new_square.grid[1].set_letter("a")
# new_square.grid[2].set_letter("c")
# new_square.grid[3].set_letter("c")
# new_square.grid[4].set_letter("b")
# new_square.grid[5].set_letter("a")
# new_square.grid[6].set_letter("a")
# new_square.grid[7].set_letter("c")
# new_square.grid[8].set_letter("b")

