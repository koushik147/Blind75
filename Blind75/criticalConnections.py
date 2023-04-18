class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        self.criticalConnections = [] # 
        self.arrival = [0]*n # storing the arrival time
        self.lowest = [0]*n # storing the lowest time
        self.visited = [False]*n # storing the visited value
        self.adj = {}

        for i,j in connections: # craeting the adjacency matrix to store the graph
            # i to j
            if i in self.adj:
                self.adj[i].append(j)
            else:
                self.adj[i] = [j]

            # j to i
            if j in self.adj: # doing it twice because of undirected graph
                self.adj[j].append(i)
            else:
                self.adj[j] = [i]

        self.dfs(0,-1,-1) #node, parent, time
        return self.criticalConnections # returning the critical connections

    def dfs(self,node,parent,time):
        self.visited[node] = True # changing the visited to true
        time+=1

        self.arrival[node] = time # storing the time to incoming node
        self.lowest[node] = time # storing the time to incoming node

        for nchild in self.adj[node]:
            if nchild != parent: # if child is not parent
                if not self.visited[nchild]: # if not visited then call dfs function
                    self.dfs(nchild,node,time) 
                    # check for critical connections
                    # if nchild's lowest time > node arrival time , which means there is no cyclicity between them,
                    # connection between nchild and node is CRITICAL
                    if self.lowest[nchild] > self.arrival[node]: #
                        self.criticalConnections.append([nchild,node])

                # carry the lowest point, this will check if there is a cycle
                self.lowest[node] = min(self.lowest[node],self.lowest[nchild])