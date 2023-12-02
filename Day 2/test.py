import re

# 3 red, 5 green, 4 blue                          (fake)
string_1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
string_2 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
string_3 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
string_4 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
string_5 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

strings_to_search = ["...red", "...green", "...blue"]
result = re.findall("...red|...green|...blue", string_1)

red_list = []
green_list = []
blue_list = []

is_over_limit = False

result = re.findall("...red|...green|...blue", string_2)
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
'''
for r_num in red_list:
    if "12" in r_num:
        is_over_limit = True
        break

if is_over_limit != True:
    for g_num in green_list:
        if "13" in g_num:
            is_over_limit = True
            break

if is_over_limit != True:
    for b_num in blue_list:
        if "14" in b_num:
            is_over_limit = True
            break
'''

print(red_list)
print(green_list)
print(blue_list)

'''
print(result)
print(red_list)
print(green_list)
print(blue_list)
'''