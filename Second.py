#Dijkstra

s = int(input()) # num of try
for u in range(s):
    n = int(input()) #num of rows & cols

    Citys = list()
    Connections = list()
    for i in range(n):
        Connections.append([0]*n)

    for i in range(n): #create list
        Citys.append(input()) #name
        p = int(input()) # num of neighbors
        for j in range(p):
            a, b = map(int, input().split())
            Connections[i][a - 1] = b




    inf = 10000

    def Dijkstra (start, stop):
        check = list() #list for min path + used check
        Start = start
        Stop = stop

        for i in range(n):  #list default fill
            check.append([0] * 3)
            check[i][0] = i
            check[i][1] = inf
        check[start][1] = 0


        while Start != Stop:
            for i in range(n):
                if check[i][2] != 1: #if not used
                    if Connections[Start][i] != 0: # if has connection
                        j = check[i][1]
                        check[i][1] = int(Start) + int(Connections[Start][i])
                        p = check[i][1]
                        if j <= p: # check of minimal way
                            check[i][1] = j
            check[Start][2] = 1 #checked
            MinVal = 10000
            MinIndex = 100
            for i in range(n): #find index of min value (not used)
                if check[i][2] != 1:
                    if check[i][1] < MinVal:
                        MinVal = check[i][1]
                        MinIndex = i
            Start = MinIndex

        Start = start
        Stop = stop

        print(check[Stop][1])

    rpath = int(input()) #
    for i in range (rpath):
        star, sto = map(str, input().split())
        IxStart = 0
        IxStop = 0
        for j in range(n): #get index of city in list
            if Citys[j] == star:
                IxStart = j
            elif Citys[j] == sto:
                IxStop = j
        Dijkstra(IxStart, IxStop)









