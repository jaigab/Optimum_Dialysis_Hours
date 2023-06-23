import random
import copy
width=int(input("How wide do you want your 2048 grid?"))

class game_2048:
    def __init__(self,dimension):
        self.dimension = dimension
        game_grid = []
        for height in range(self.dimension):
            line = []
            for width in range(self.dimension):
                if random.randint(0,(self.dimension**2))<int(0.2*(self.dimension**2)): line += [2]
                else: line.append('.')
            game_grid.append(line)
        two_count = 0
        for line in game_grid:
            for item in line:
                if item == 2: two_count += 1
        if two_count <= 2:
            for i in range(2): game_grid[width-1][i] = 2
        self.game_grid = game_grid
    
    def get_grid(self):
        strfield=[]
        for line in self.game_grid:
            str_line=[]
            for item in line: str_line += [str(item)]
            strfield.append(str_line)
        self.strfield = strfield
        for line in self.strfield: print(" ".join(line))
            
    def adding_numbers_in_move(self,LIST):
        function_LIST = copy.copy(LIST)
        if len(function_LIST) <= 1: return function_LIST
        elif len(function_LIST) == 2:
            if function_LIST[0] == function_LIST[1]: return [function_LIST[0] + function_LIST[1]]
            else: return function_LIST
        else:
            output_list = []
            while len(function_LIST) >= 2:
                if function_LIST[0] == function_LIST[1]:
                    output_list.append(function_LIST[0] + function_LIST[1])
                    function_LIST.pop(0)
                    function_LIST.pop(0)
                else: output_list.append(function_LIST.pop(0))
            if function_LIST != []: output_list.append(function_LIST[0])
            return output_list
        
    def move(self,direction):
        numbers_to_move = {}
        added_numbers = {}
        twos_to_add = {}
        direction_range = {}
        direction_range["u"],direction_range["l"],direction_range["d"], direction_range["r"] = [range(self.dimension),range(self.dimension),reversed(range(self.dimension)),reversed(range(self.dimension))]
        for i in range(self.dimension): numbers_to_move[i] = []
        for i in direction_range[direction]:
            for j in range(self.dimension):
                if type(self.game_grid[i][j]) == int: numbers_to_move[j].append(self.game_grid[i][j])
        for dim in range(self.dimension):
            added_numbers[dim] = self.adding_numbers_in_move(numbers_to_move[dim])
            if numbers_to_move[dim] == [] or added_numbers[dim] == []: twos_to_add[dim] = 0
            else: twos_to_add[dim] = len(numbers_to_go_up[dim]) - len(added_numbers[dim])
        self.added_numbers = added_numbers
        self.twos_to_add = twos_to_add
        self.set_grid(direction)
        self.get_grid()
        
    def set_grid(self,direction):
        game_grid = []
        for height in range(self.dimension):
            line = []
            for width in range(self.dimension):
                line.append('.')
            game_grid.append(line)
        for dim in range(self.dimension):
            if direction == "u":
                for num in range(len(self.added_numbers[dim])):
                    game_grid[num][dim] = self.added_numbers[dim][num]
                num_changes = False
                for num in range(self.twos_to_add[dim]):
                    game_grid[num-1][dim] = random.choice([2,4,8,16])
                    num_changes = True
                if num_changes == False:
                    game_grid[self.dimension-1][random.choice(list(range(self.dimension)))] = random.choice([".",2,".",4,"."])
            elif direction == "d":
                for num in range(len(self.added_numbers[dim])):
                    game_grid[self.dimension-1-num][dim] = self.added_numbers[dim][num]
                for num in range(self.twos_to_add[dim]):
                    game_grid[num][dim] = random.choice([2,4,8,16])
            elif direction == "l":
                for num in range(len(self.added_numbers[dim])):
                    game_grid[dim][num] = self.added_numbers[dim][num]
                for num in range(self.twos_to_add[dim]):
                    game_grid[dim][self.dimension-num-1] = random.choice([2,4,8,16])
            elif direction == "r":
                for num in range(len(self.added_numbers[dim])):
                    game_grid[dim][self.dimension-num-1] = self.added_numbers[dim][num]
                for num in range(self.twos_to_add[dim]):
                    game_grid[dim][num] = random.choice([2,4,8,16])
        self.game_grid = game_grid

new_game_2048 = game_2048(width)
new_game_2048.get_grid()

for i in range(200):
    input_move = input("What's your next move")
    new_game_2048.move(input_move)