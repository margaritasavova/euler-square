import random
from collections import deque
import itertools

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

    def __eq__(self, other):
        if self.letter == other.letter and self.number == other.number:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.get_letter()}{self.get_number()}"


class Grid():
    def __init__(self, n):
        self.n = n
        self.grid = [Cell() for i in range(n*n)]
        # self.grid = [[Cell() for j in range(self.n)] for i in range(self.n)] 

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
        
    def shuffle_elements(self):
        random_letters = self.letters.copy()
        random.shuffle(random_letters)
        random_numbers = self.numbers.copy()
        random.shuffle(random_numbers)
        return random_letters, random_numbers

    def generate_random_square(self):
        # this function produces random squares, which are most of the time not valid,
        # but can be validated with the is_valid function
        # finds a valid function slower
        for i in range(self.n):
            random_letters, random_numbers = self.shuffle_elements()
            # random_letters = self.letters.copy()
            # random.shuffle(random_letters)
            # random_numbers = self.numbers.copy()
            # random.shuffle(random_numbers)
            for j in range(self.n):
                letter = random_letters.pop()
                self.grid[self.n*i+j].set_letter(letter)
                number = random_numbers.pop()
                self.grid[self.n*i+j].set_number(number)
                
    def generate_square(self):
        if self.n % 2 == 1:
            self.generate_odd_square()
        elif self.n % 2 == 0 and self.n != 0:
            self.generate_even_square()
        else:
            print("Input needs to be a positive integer.")
                    
    def generate_odd_square(self):
        # shorter version for odd squares
        letters, numbers = self.shuffle_elements()
        letters = deque(letters)
        numbers = deque(numbers)
        for i in range(self.n):
            letters.rotate(1)
            numbers.rotate(2)
            for j in range(self.n):
                self.grid[self.n*i+j].set_letter(letters[j])
                self.grid[self.n*i+j].set_number(numbers[j])
                
    def generate_even_square(self):
        if self.n % 8 == 0:
            self.eight_by_eight_square()
        elif self.n % 4 == 0:
            self.four_by_four_square()
        elif self.n == 6:
            print("Sorry, no known solution for n=6.")
        else:
            print("Sorry, no solution yet for multiples of 2.")    # needs to be fixed
        
    def swap_positions_v1(self, row): 
        row[0], row[1], row[2], row[3] = row[2], row[3], row[0], row[1] 
        return row
        
    def swap_positions_v2(self, row): 
        row[0], row[1], row[2], row[3] = row[1], row[0], row[3], row[2] 
        return row
        
    def swap_rows(self, index_row_1, index_row_2):
        for i in range(self.n):
            # self.grid[self.n*index_row_2+i].set_number(), self.grid[self.n*index_row_1+i].set_number() \
            # = self.grid[self.n*index_row_1+i].get_number(), self.grid[self.n*index_row_2+i].get_number()
            temp_number_1 = self.grid[self.n*index_row_1+i].get_number()
            temp_number_2 = self.grid[self.n*index_row_2+i].get_number()
            self.grid[self.n*index_row_2+i].set_number() = temp_number_1
            self.grid[self.n*index_row_1+i].set_number() = temp_number_2
                
    # def four_by_four_square(self):   # n = 4
        # letters, numbers = self.shuffle_elements()
        # row_list_letters = [[] for i in range(self.n)]
        # row_list_numbers = [[] for i in range(self.n)]
        # row_list_letters[0] = letters.copy()
        # row_list_letters[1] = self.swap_positions_v1(letters.copy())
        # row_list_letters[2] = self.swap_positions_v2(letters.copy())
        # row_list_letters[3] = self.swap_positions_v2(self.swap_positions_v1(letters.copy()))
        # row_list_numbers[0] = numbers.copy()
        # row_list_numbers[1] = self.swap_positions_v2(numbers.copy())
        # row_list_numbers[2] = self.swap_positions_v2(self.swap_positions_v1(numbers.copy()))
        # row_list_numbers[3] = self.swap_positions_v1(numbers.copy())
        # for i in range(self.n):
            # for j in range(self.n):
                # self.grid[self.n*i+j].set_letter(row_list_letters[i][j])
                # self.grid[self.n*i+j].set_number(row_list_numbers[i][j])
                
    def four_by_four_square(self, letters, numbers, quad_row=0, quad_col=0):   # n = 4
        if self.n == 4:
            letters, numbers = self.shuffle_elements()
            letters = deque(letters)
            numbers = deque(numbers)
        letters = deque(itertools.islice(letters, 4*quad_col, 4*quad_col+4))
        numbers = deque(itertools.islice(numbers, 4*quad_col, 4*quad_col+4))
        # letters = letters[4*quad_col : 4*quad_col+4]
        # numbers = numbers[4*quad_col : 4*quad_col+4]
        row_list_letters = []
        row_list_numbers = []
        row_list_letters.append(letters)
        row_list_letters.append(self.swap_positions_v1(letters.copy()))
        row_list_letters.append(self.swap_positions_v2(letters.copy()))
        row_list_letters.append(self.swap_positions_v2(self.swap_positions_v1(letters.copy())))
        row_list_numbers.append(numbers)
        row_list_numbers.append(self.swap_positions_v2(numbers.copy()))
        row_list_numbers.append(self.swap_positions_v2(self.swap_positions_v1(numbers.copy())))
        row_list_numbers.append(self.swap_positions_v1(numbers.copy()))
        # print(row_list_letters)
        # print(row_list_numbers)
        for i in range(4):
            for j in range(4):
                # print(self.n*(4*quad_row+i)+4*quad_col+j)
                self.grid[self.n*(4*quad_row+i)+4*quad_col+j].set_letter(row_list_letters[i][j])
                self.grid[self.n*(4*quad_row+i)+4*quad_col+j].set_number(row_list_numbers[i][j])
                
    # def row_of_quadrants(self):
        # for i in range(0, self.n//4):
            # batch_letters = letters[4*i : 4*i+4]
            # batch_numbers = numbers[4*i : 4*i+4]
            # self.four_by_four_square(i)
        
    def eight_by_eight_square(self):   # n = 8
        letters, numbers = self.shuffle_elements()
        # batches_letters = [letters[4*i : 4*i+4] for i in range(0, self.n/4]
        # batches_numbers = [numbers[4*i : 4*i+4] for i in range(0, self.n/4]
        # for batch in batches_letters:
        letters = deque(letters)
        numbers = deque(numbers)
        for i in range(0, self.n//4):
            for j in range(0, self.n//4):
                # batch_letters = letters[4*i : 4*i+4]
                # batch_numbers = numbers[4*i : 4*i+4]
                # batch_letters = deque(itertools.islice(letters, 4*i, 4*i+4))
                # batch_numbers = deque(itertools.islice(numbers, 4*i, 4*i+4))
                self.four_by_four_square(letters, numbers, quad_row=i, quad_col=j)
            letters.rotate(4)
            # numbers.rotate(8)
        self.swap_rows(4, 5)
        self.swap_rows(6, 7)
        
                
    def multiples_of_four_odd(self):   # n = 12, 20, 28, 36, 44, ...
        pass
        
    def multiples_of_eight_odd(self):   # n = 24, 40, 56, 72, ...
        pass
        
    def multiples_of_sixteen(self):   # n = 16, 48, 80, ...
        pass                            # use recursion ?
        
    def multiples_of_thirty_two(self):   # n = 32, 64, ...
        pass
        
    def is_valid(self):
        # self.__check_diagonal__()
        for i in range(self.n):
            for x in range(1, self.n-i):
                for j in range(self.n):
                    if self.grid[self.n*i+j].get_letter() == self.grid[(self.n*(i+x)+j)].get_letter() or \
                        self.grid[self.n*i+j].get_number() == self.grid[(self.n*(i+x)+j)].get_number():
                        if i != self.n - 1:
                            return False
                    if 1 != self.grid.count(self.grid[self.n*i+j]):
                        return False
        return True

        
new_square = EulerSquare(8)

new_square.generate_square()
if new_square.is_valid():
    print("Found it!\n")
    new_square.print_grid()
else:
    # if self.n == 6:
        # pass
    # else:
    print("Fix code!\n")
    new_square.print_grid()
    
# while True:
    # new_square.generate_random_square()
    # if new_square.is_valid():
        # print("found it!")
        # new_square.print_grid()
        # break


