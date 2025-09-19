graph = {
    # Start fan-out
    "S": ["A", "B", "C"],

    # Self-loops + back edges
    "A": ["S", "A", "D"],           # A → A (self-loop)
    "B": ["S", "C", "E"],
    "C": ["S", "B", "C", "F"],      # C → C (self-loop)

    "D": ["A", "G"],
    "E": ["B", "E", "F"],           # E → E (self-loop)
    "F": ["C", "E", "H", "I"],

    "G": ["D", "J"],
    "H": ["F", "H", "K", "P"],      # H → H (self-loop)
    "I": ["F", "M"],

    "J": ["G", "N"],
    "K": ["H", "O"],
    "M": ["I", "Q"],
    "N": ["J"],

    # Back-edges to create big cycles through S
    "O": ["K", "S"],
    "P": ["H", "S"],

    # Narrow corridor to the goal, with a 2-cycle trap (R↔T)
    "Q": ["M", "R"],
    "R": ["Q", "T"],
    "T": ["R", "U"],                # R ↔ T forms a 2-cycle
    "U": ["T", "GOAL"],

    "GOAL": []
}



class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

class Queue():
    
    def __init__(self):
        self.frontier = []
        self.checked = []

    def add(self, node):
        self.frontier.append(node)

    def is_in_frontier(self, node):
        for visited in self.frontier:
            if node.state == visited.state:
                return False
        return True
            
    def remove(self):
        if self.frontier:
            x = self.frontier.pop(0)
            self.checked.append(x.state)
            return x
        else:
            raise ValueError("No Solution")






def solve(start=list(graph)[0], end=list(graph)[-1]):
    queue = Queue()
    root_node = Node(start)
    queue.add(root_node)

    while True:
        node = queue.remove()
        letter = node.state
        if letter == end:
            return node
        
        for i in graph[letter]:
            addednode = Node(i, node)
            if addednode not in queue.checked:
                queue.frontier.append(addednode)
            
            
def reconstruct_path(goal_node):
    path = []
    current = goal_node
    while current.parent is not None:
        path.append(current.state) 
        current = current.parent
    path.append(current.state)
    path.reverse()
    return path


z = (input("Pick the first State: ")).upper()
y = (input("Pick the second State: ")).upper()
x = solve(z, y)

print(reconstruct_path(x))


        
