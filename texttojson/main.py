# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
import json
def textjson():
    filename = 'data.txt'

    # dictionary where the lines from
    # text will be stored
    dict1 = {}
    l = 1

    # creating dictionary
    with open(filename) as fh:
        for line in fh:
            print(line)
            # reads each line and trims of extra the spaces
            # and gives only the valid words
            command, description = line.strip().split(None,1)
            print(description)
            i = 0
            u = 'user' + str(1)
            dict2 = {}
            x = len(fh.readlines())
            while i < x:
                dict2[command[i]] = description.strip()
                i = i + 1
                print(i)
                print(dict2)
            dict1[u] = dict2
            print(dict1)
            l = l + 1


    out_file = open("test1.json", "w")
    json.dump(dict1, out_file, indent = 4)
    out_file.close()



import json

# the file to be converted to
# json format
def textjson():
    filename = 'data.txt'

    # dictionary where the lines from
    # text will be stored



    dict1 = {}
    out_file = open("test1.json", "w")
    fields = ['URL', 'Username', 'Password', 'Application']
    l = 1


    # creating dictionary
    with open(filename) as fh:
        for line in fh:

            #print(line)
            # reads each line and trims of extra the spaces
            # and gives only the valid words



            i = 0

            u = 'user' + str(l)
            dict2 ={}


            #if i < 2:
                #l = 1

            if ":" not in line:
                continue
            description = line.strip().split(':',1)
            #print(description[1])
            #dict1[command] = description[1]
            #while i < len(fields):
                # creating dictionary for each employee
            for i in range(len(fields)):
                dict2[fields[i]] = description[1]
                i+=1
                print(dict2)
            #print(dict2)
            dict1[u] = dict2
            #print(dict2)
            l += 1
            json.dump(dict2, out_file, indent=4)

            #print(dict2)


    #json.dump(dict2, out_file, indent=4)
    # creating json file
    # the JSON file is named as test1



    out_file.close()
    '''

import json
def textjson():
    filename = 'data.txt'
    dict1 = {}
    out_file = open("test1.json", "w")
    l = 1

    x = []
    y = []


    i = 0




    with open(filename) as fh:
        for line in fh:

                if ":" not in line:
                    continue

                description = line.strip().split(':', 1)
                #if "-" not in line:
                #
                x.append(description[0])
                y.append(description[1])

    z = len(x)
    z += 1
    for j in range (z):
        dict2 = {}
        for i in range(j):
            dict2[x[i]] = y[i]
        i += 1

            #print(dict2)
        if (i%4)==0:
            #print(i)
            u = 'user' + str(l)
            dict1[u] = dict2
            l+=1
    print(dict1)

    out_file = open("test1.json", "w")
    json.dump(dict1, out_file)
    out_file.close()



if __name__ == '__main__':
    textjson()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
