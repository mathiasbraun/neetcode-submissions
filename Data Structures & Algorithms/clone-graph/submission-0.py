class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copies = {node: Node(node.val, None)}   # Original -> Kopie
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val, None)
                    queue.append(neighbor)
                copies[curr].neighbors.append(copies[neighbor])

        return copies[node]
