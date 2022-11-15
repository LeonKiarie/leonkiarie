import copy

graph = {
    'SportsComplex': {'Siwaka': 450},
    'Siwaka': {'Ph.1A': 10, 'Ph.1B': 230},
    'Ph.1A': {'Ph.1B':100, 'Mada':850},
    'Ph.1B': {'Phase2':112, 'STC':50},
    'Phase2': {'J1':600, 'STC':50, 'Phase3':500},
    'STC': {'ParkingLot': 250},
    'Phase3': {'ParkingLot':350},
    'ParkingLot': {'Mada': 700}
}



def ucs(start,final):
    path=[]
    priorityQueue = [[[start], 0]]
    visited = []
    while priorityQueue!=[]:
        path.append(priorityQueue.pop(0))
        node=path[-1][0][-1]
        visited.append(node)
        if node == final:
            finalPath = copy.deepcopy(path[-1])
            print("final", finalPath)
            return "Found"
        for neighbor,cost in graph[node].items():
            if neighbor not in visited:
                newpath=copy.deepcopy(path[-1])
                newpath[0].append(neighbor)
                newpath[1]+=cost
                priorityQueue.append(newpath)


        priorityQueue.sort(key=lambda x:x[1])


ucs('SportsComplex','ParkingLot')