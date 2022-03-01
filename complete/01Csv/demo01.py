import os

# open csv file named "demo01.csv"
# sort the data by the first column
# print the first 5 lines




# The "with" keyword will automatically close the file
with open("demo01.csv", "r") as f:
    # read the file into a list of lines
    lines = f.readlines()

    # sort the lines by the first column
    lines.sort(key=lambda line: line.split(",")[0])

    # print the first 5 lines
    for line in lines[:5]:
        print(line, end="")