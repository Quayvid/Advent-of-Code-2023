import re

# 12 red cubes, 13 green cubes, and 14 blue cubes

file_input = open("input.txt", "r")

contents = file_input.read()
contents_list = contents.split("\n")
contents_list.pop()

game_no = 1
id_sum = 0

red_list = []
green_list = []
blue_list = []

is_over_limit = False

for game in contents_list:
    result = re.findall("...red|...green|...blue", game)
    for color in result:
        if "red" in color:
            color = int(re.sub("[^0-9]", "", color))
            red_list.append(color)
        elif "green" in color:
            color = int(re.sub("[^0-9]", "", color))
            green_list.append(color)
        else:
            color = int(re.sub("[^0-9]", "", color))
            blue_list.append(color)
    
    for r_num in red_list:
        if r_num > 12:
            is_over_limit = True
            break
    
    if is_over_limit != True:
        for g_num in green_list:
            if g_num > 13:
                is_over_limit = True
                break
    
    if is_over_limit != True:
        for b_num in blue_list:
            if b_num > 14:
                is_over_limit = True
                break
            
    if is_over_limit != True:
        id_sum += game_no
        
    game_no += 1
    
    red_list.clear()
    green_list.clear()
    blue_list.clear()

    is_over_limit = False

print(id_sum)
