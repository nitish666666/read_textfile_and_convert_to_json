import json
def textjson():
    filename = 'data.txt'
    dict1 = {}
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


