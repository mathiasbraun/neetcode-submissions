from collections import deque

class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = []
        if dst not in self.adj:
            self.adj[dst] = []
        if dst not in self.adj[src]:
            self.adj[src] += [dst]

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj:
            return False
        if dst in self.adj[src]:
            self.adj[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst or dst in self.adj[src]:
            return True

        queue = deque()
        queue.append(src)
        visit = set()
        visit.add(src)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == dst:
                    return True

                for neighbor in self.adj[curr]:
                    if neighbor not in visit:
                        queue.append(neighbor)
                        visit.add(neighbor)
        
        return False