class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        # Initialize Graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for pair in prerequisites:
            graph[pair[1]] = graph.get(pair[1], [])
            graph[pair[1]].append(pair[0])
            graph[pair[0]] = graph.get(pair[0], [])

        # Initialize Stack (checks for cycle)
        stack = []

        # Initialize visited
        # -1: unvisited
        #  0: visited & pushed to stack
        #  1: visited & popped from stack
        visited = [-1] * numCourses

        # Initialize Ordering, indexes added from the back topologically
        ordering = [0] * numCourses
        index = numCourses - 1

        # Loop through all nodes to makes sure its a DAG
        for course in graph.keys():
            # If course is not visited, use DFS to find all of its requisite courses
            if (visited[course] == -1):
                # Save index so the next node can take over where the last started
                index = self.dfs(index, course, stack,
                                 visited, graph, ordering)
                # If there is a cycle passed up from the recursion (in this case -infinity), return False
                if (index == float('-inf')):
                    return []

        return ordering

    def dfs(self, index, course, stack, visited, graph, ordering):
        # Add course to stack and set visited to 'pushed to stack'
        stack.append(course)
        visited[course] = 0

        # DFS through all neighbors
        for neighborCourse in graph[course]:
            # If neighbor is not visited, recurse
            if (visited[neighborCourse] == -1):
                index = self.dfs(index, neighborCourse, stack,
                                 visited, graph, ordering)
                # If cycle exists, pass it up
                if index == float('-inf'):
                    return float('-inf')
            # If cycle exists, pass it up
            elif (visited[neighborCourse] == 0):
                return float('-inf')

        # If we've reached a dead end, pop from stack and set visited to 1
        stack.pop()
        visited[course] = 1

        # Update topological ordering and return the current place in the array to add requisite courses
        ordering[index] = course
        return index - 1
