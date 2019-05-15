import re
from collections import defaultdict


class Graph(object):
    nodes = []
    table = {}
    edges = defaultdict(list)

    def __init__(self, count, table: dict):
        self.table = table
        for i in range(count):
            self.nodes.append(int(i))
        for key in table.keys():
            a, b = key
            if (self.table[key] != -32768):
                self.edges[a].append(b)

    def getNeighors(self, node):
        return self.edges[node]


class DejkstraData(object):
    price: int
    previous: int

    def __init__(self, price: int, previous: int):
        self.previous = previous
        self.price = price


def main():
    map, count, start, finish = read()
    graph = Graph(count, map)
    list = dijkstra(graph, start, finish)
    list.reverse()
    with open('out.txt', 'w') as file:
        if (len(list) > 0):
            file.write('Y')
        else:
            file.write('N')
        file.write('\n')
        for i in list:
            file.write(str(i) + ' ')


def dijkstra(map: Graph, start: int, finish: int):
    notVisited = map.nodes;
    track = {}
    track[int(start)] = DejkstraData(0, -1)
    while 1 > 0:
        toOpen: int = -2
        bestPrise = 10000000;
        for node in notVisited:
            if (int(node) in track and track[node].price < bestPrise):
                bestPrise = track[node].price
                toOpen = node
        if (int(toOpen) == int(finish)):
            break
        if (toOpen == -2):
            break;
        for e in map.edges[toOpen]:
            currentPrice = track[toOpen].price + map.table[(toOpen, e)]
            if (int(e) not in track or track[e].price > currentPrice):
                track[e] = DejkstraData(currentPrice, toOpen)

        notVisited.remove(int(toOpen))

    result = []
    end = int(finish)
    if (end not in track):
        return []
    while (end != -1):
        result.append(end)
        end = track[end].previous
    return result


def read():
    with open('in.txt', 'r') as input_file:
        str = input_file.read()
    map = {}
    idx = 0
    values = re.split(r'(?: |\n|\s)\s*', str)
    count = int(values[0])
    for i in range(1, count ** 2):
        map[(idx // count, idx % count)] = int(values[i])
        idx += 1

    start = values[count ** 2 + 1]
    finish = values[count ** 2 + 2]
    return (map, count, start, finish)


if __name__ == '__main__':
    main()
