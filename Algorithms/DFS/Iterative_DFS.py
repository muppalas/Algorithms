'''notes 
How DFS Works 
Start at a node (e.g., "A").
Mark it as visited so you don’t visit it again.
Go to one of its neighbors (e.g., from "A" to "B").
Repeat the process for "B"—mark it visited and move to one of its neighbors.
If you get to a point where you can’t go further, you backtrack to the previous node 
and check for other unvisited neighbors.
Continue until all nodes have been visited.

Types of Graphs DFS Can Work On
Directed Graph: Edges have directions (like one-way streets).
Undirected Graph: Edges don’t have directions (like two-way streets).
Connected Graph: All nodes are connected by some path.
Disconnected Graph: Some nodes aren’t connected.

DFS Time Complexity:
O(V + E), where V is the number of nodes (vertices) and E is 
the number of edges. This is because each node and edge is visited once.

DFS Space Complexity:
Depends on the recursion depth or stack size.
O(V) in the worst case (for a very deep graph).

Recursive vs. Iterative:
Recursive is simpler but can cause stack overflow for very deep graphs.
Iterative avoids recursion limits but requires managing the stack explicitly.
 
IMPORTANT QUESTIONS!!!
1.Can DFS be used on both directed and undirected graphs?
ANS:Yes, DFS works on both types.

2.How does DFS detect cycles in a graph?
ANS:If a node is visited again during traversal (and it’s not the parent node in undirected graphs), there’s a cycle.

3.What happens if the graph is disconnected?
ANS:You need to run DFS separately for each connected component.

4.Can DFS find the shortest path?
ANS: No, DFS does not guarantee the shortest path. Use BFS for that.''' 

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# Iterative DFS function
def dfs_iterative(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    stack = [start_node]  # Stack to manage nodes to visit

    while stack:  # Run until there are no more nodes to visit
        node = stack.pop()  # Take the top node from the stack
        if node not in visited:
            visited.add(node)  # Mark it as visited
            print(node, end=" ")  # Process the node
            
            # Add unvisited neighbors to the stack (in reverse order for correct traversal)
            stack.extend(reversed(graph[node]))

# Run the DFS function
dfs_iterative(graph, 'A')
