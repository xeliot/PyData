class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x for x in self.connectedTo.keys()])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(t, cost)

    def getVertices(self):
        return self.vertList.keys()

    def getEdges(self):
        result = ''
        for val in self.vertList.values():
            if len(val.connectedTo) > 0:
                for key in val.connectedTo.keys():
                    result = result + val.id + " -> " + key + "\n"
        print result

    def getToNeighbors(self, node):
        result = []
        for key in self.vertList.keys():
            if key == node:
                for name in self.vertList[key].connectedTo.keys():
                    result.append(name)
        return result

    def getFromNeighbors(self, node):
        result = []
        for key in self.vertList.keys():
            if self.vertList[key].connectedTo.has_key(node):
                if key not in result:
                    result.append(key)
        return result

    def getWeight(self, f, t):
        if (f not in self.vertList) or (t not in self.vertList):
            raise Exception('Nodes not in graph')
        else:
            for key in self.vertList.keys():
                if key == f:
                    return self.vertList[key].getWeight(t)

    def bfs(self, start, end):
        if (start not in self.vertList) or(end not in self.vertList):
            raise Exception('Nodes not in graph')
        visited = []
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            visited.append(node)
            if node == end:
                return path
            for adjacent in self.vertList[node].connectedTo.keys():
                if adjacent not in visited:
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)

    def dfs(self, start, end):
        if (start not in self.vertList) or(end not in self.vertList):
            raise Exception('Nodes not in graph')
        visited = []
        stack = []
        stack.append([start])
        while stack:
            #print stack
            path = stack.pop(-1)
            node = path[-1]
            visited.append(node)
            if node == end:
                return path
            #print self.vertList[node].connectedTo.keys()
            for adjacent in sorted(self.vertList[node].connectedTo, reverse=True):
                tmp = ("%s: %s" % (adjacent, self.vertList[node].connectedTo[adjacent]))[0]
                if tmp not in visited:
                    new_path = list(path)
                    new_path.append(tmp)
                    stack.append(new_path)

    def bfs_all(self, start, end):
        result =  []
        if (start not in self.vertList) or(end not in self.vertList):
            raise Exception('Nodes not in graph')
        visited = []
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            if len([x for x in path if path.count(x) >= 2]) > 0:
                break
            node = path[-1]
            visited.append(node)
            if node == end:
                result.append(path)
            for adjacent in self.vertList[node].connectedTo.keys():
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return result

    def dfs_all(self, start, end):
        if (start not in self.vertList) or(end not in self.vertList):
            raise Exception('Nodes not in graph')
        stack = []
        result = []
        stack.append([start])
        while stack:
            path = stack.pop(-1)
            if len([x for x in path if path.count(x) >= 2]) > 0:
                break
            node = path[-1]
            if node == end:
                result.append(path)
            for adjacent in sorted(self.vertList[node].connectedTo, reverse=True):
                tmp = ("%s: %s" % (adjacent, self.vertList[node].connectedTo[adjacent]))[0]
                new_path = list(path)
                new_path.append(tmp)
                stack.append(new_path)
        return result
        
a = Graph()
'''
a.addEdge('A', 'B', 5)
a.addEdge('C', 'A', 2)
a.addEdge('C', 'B', 3)
a.addEdge('B', 'D', 8)
a.addEdge('B', 'F', 3)
a.addEdge('F', 'E', 5)
a.addEdge('F', 'G', 6)
a.addEdge('D', 'G', 2)

'''
a.addEdge('A', 'B')
a.addEdge('A', 'D')
a.addEdge('A', 'E')
a.addEdge('B', 'C')
a.addEdge('B', 'H')
a.addEdge('C', 'F')
a.addEdge('F', 'G')
a.addEdge('H', 'G')
a.addEdge('E', 'G')
