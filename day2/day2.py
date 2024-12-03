count = 0
with open("input.txt") as file:
    for line in file: #read by line
        #cleanline = line.strip(" ")
        cleanline = list(map(int, line.split(" ")))


       
        if all(cleanline[i] < cleanline[i + 1] for i in range(len(cleanline) - 1)):  # check if the line is in ascending order
            if all(cleanline[j + 1] - cleanline[j] <=3 for j in range(len(cleanline) - 1)): # check if the numbers are increasing not more than by 3
                print(cleanline)
                count = count + 1

        # check if the line is in descending order
        if all(cleanline[i] > cleanline[i + 1] for i in range(len(cleanline) - 1)):
            if all(cleanline[j]-cleanline[j + 1] <=3 for j in range(len(cleanline) - 1)): # check if the numbers are decreasing not more than by 3
                print(cleanline)
                count = count + 1

#close file
file.close()

print(count)