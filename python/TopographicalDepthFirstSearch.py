def recursiveDFS(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(f"Processing Node {node}, with visited as {visited}")  # Process the current node

        for neighbor in graph[node]:
            print(f"Neighbour is {neighbor} for node {graph[node]}")
            recursiveDFS(graph, neighbor, visited)

# Example usage with an adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# graph = { 'A': ['B', 'C'], 'B': ['A'], 'C': ['A'], 'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['X'] }
visited = set()
# recursiveDFS(graph, 'A', visited)

print(f"FInal visited {visited}")

#---------------------------------------------------------------------------------------------------------------------\\
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(f"Processing Node {node}, with visited as {visited}")
            # Push neighbors in reverse to mimic recursive DFS order
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

    print(f"\nFinal visited set: {visited}")

dfs_iterative(graph, 'A')
