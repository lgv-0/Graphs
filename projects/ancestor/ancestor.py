from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    graph = {}
    v = []
    target = starting_node

    for i in ancestors:
        if i[0] in graph:
            graph[i[0]].append(i[1])
        else:
            graph[i[0]] = [i[1]]
            v.append(i[0])

    longest = [0,0]
    count = 0

    for i in v:
        node = i

        def dfs(node, count, longest, graph):
            stack = Stack()
            stack.push(node)
            visited = set()

            while stack.size() > 0:
                vertex = stack.pop()
                if vertex == target:
                    if longest[0] < count:
                        longest[0] = count
                        longest[1] = i
                    if longest[0] == count:
                        longest[1] = min([i, longest[1]])
                    count = 0
                    break

                if vertex not in visited:
                    count += 1
                    visited.add(vertex)
                    if vertex in graph:
                        for next_vert in graph[vertex]:
                            stack.push(next_vert)
                    else:
                        count = 1

        count = 0
        dfs(node, count, longest, graph)

    if longest[1] == 0:
        return -1
    else:
        return longest[1]
