class Solution(object):

    def topSort(self, numCourses, prerequisites):
        # Initialize Graph
        graph = {}
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

        # Loop through all nodes to makes sure its a DAG
        for course in graph.keys():
            # If course is not visited, use DFS to find all of its requisite courses
            if (visited[course] == -1):
                # Save index to check if there is a cycle
                index = self.dfs(course, stack, visited, graph)
                # If there is a cycle passed up from the recursion (in this case -1), return False
                if (index == -1):
                    return False

        return True

    def dfs(self, course, stack, visited, graph):
        # Add course to stack and set visited to 'pushed to stack'
        stack.append(course)
        visited[course] = 0

        # DFS through all neighbors
        for neighborCourse in graph[course]:
            # If neighbor is not visited, recurse
            if (visited[neighborCourse] == -1):
                index = self.dfs(neighborCourse, stack, visited, graph)
                # If cycle exists, pass it up
                if (index == -1):
                    return -1
            # If cycle exists, pass it up
            elif (visited[neighborCourse] == 0):
                return -1

        # If we've reached a dead end, pop from stack and set visited to 1
        stack.pop()
        visited[course] = 1

        # Return 0 for 'all clear'
        return 0
