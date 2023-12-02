import re


cali_sum = 0

first_num = 0
second_num = 0
new_num = 0

file_input = open("input.txt", "r")

contents = file_input.read()
contents_list = contents.split("\n")

for i in contents_list:
    num_only = re.sub("[^0-9]", "", i)
    if(len(num_only) > 0):
        first_num = num_only[0]
        second_num = num_only[-1]
        new_num = int(str(first_num) + str(second_num))
        cali_sum += new_num

print(cali_sum)