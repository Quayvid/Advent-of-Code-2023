import re

file_input = open("input.txt", "r")

contents = file_input.read()
contents_list = contents.split("\n")
contents_list.pop()

red_list = []
green_list = []
blue_list = []

power_set_sum = 0
power_set_product = 0


min_red_count = 0
min_green_count = 0
min_blue_count = 0


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
    
    for i in range(len(red_list)):
        if i == 0:
            min_red_count = red_list[i]
        else:
            if red_list[i] > min_red_count:
                min_red_count = red_list[i]
                
    for j in range(len(green_list)):
        if j == 0:
            min_green_count = green_list[j]
        else:
            if green_list[j] > min_green_count:
                min_green_count = green_list[j]
                
    for k in range(len(blue_list)):
        if k == 0:
            min_blue_count = blue_list[k]
        else:
            if blue_list[k] > min_blue_count:
                min_blue_count = blue_list[k]
                
    power_set_product = min_red_count * min_green_count * min_blue_count
    power_set_sum += power_set_product
            
    
    red_list.clear()
    green_list.clear()
    blue_list.clear()


print(power_set_sum)