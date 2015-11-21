import collections
import math
import random
from operator import mul

class Graph:
    '''
    A bipartite graph.
    n is the number of nodes on each side
    E is a list of edges, where each edge is a tuple (u, v)
    '''

    def __init__(self, n, E):
        '''
        Initiate the graph with n nodes on each side
        and the given set of edges
        '''
        self.n = n
        self.E = E
        self.X = [x + 1 for x in range(n)]
        self.Y = [y * -1 - 1 for y in range(n)]
        self.neighbors = {}
        for e in self.E:
            x, y = e
            self.neighbors[x] = self.neighbors.get(x, []) + [y]
            self.neighbors[y] = self.neighbors.get(y, []) + [x]

    def random_edge(self):
        '''
        Return a random edge from the graph.
        '''
        return random.sample(self.E, 1)[0]

    def construct_matching(self, k):
        '''returns a matching of size k'''
        M = Matching(k, [self.E[0]])
        while M.size() < k:
            # we will create an augmenting path that we can use to increase the size of our matching
            # R = unmatched nodes in the left side
            R = [node for node in [x + 1 for x in range(n)] if a not in M.X]
            T = []
            for node in R:
                # we want to find an unmatched edge that comes from here
                for edge in E:
                    if node in edge and edge not in M.E:
                        T.append(edge[1])
class Matching:
    '''
    A matching of size k between k nodes on the left and k nodes on the right
    '''

    def __init__(self, k, E):
        '''
        E is the set of edges in the matching
        k is the max size this matching can take
        '''
        self.k = k
        self.E = E
        self.update()

    def update(self):
        '''
        Store neighbor dictionaries for each node
        '''
        self.X_pair = {x:y for (x,y) in self.E}
        self.Y_pair = {y:x for (x,y) in self.E}

    def size(self):
        '''return the size of our matching'''
        return len(self.E)

    def transition(self, e):
        '''
        Consider transitioning M_k -> M_k-1
        or M_k-1 -> M_k-1 or M_k-1 -> M_k
        As defined in Sinclair's Algorithms for Random Generation & Counting and other works
        '''
        changed = False

        if self.size() == self.k:
            if e in self.E:
                self.E.remove(e)
                changed = True
        else:
            u,v = e
            if (u in self.X_pair) != (v in self.Y_pair):
                # XOR
                if u in self.X_pair:
                    self.E.remove((u, self.X_pair[u]))
                elif v in self.Y_pair:
                    self.E.remove((self.Y_pair[v], v))
                self.E.append(e)
                changed = True
            elif (u not in self.X_pair) and (v not in self.Y_pair):
                self.E.append(e)
                changed = True

        if changed:
            self.update()
            assert self.size() == self.k or self.size() == self.k-1

        return changed


class HopcroftKarp(object):
    '''
    Hopcroft-Karp algorithm for finding a matching of size k in a bipartite graph
    Adapted from Wikipedia and http://stackoverflow.com/questions/4697228/hopcroftkarp-algorithm-in-python
    '''

    INFINITY = -1

    def __init__(self, G):
        self.G = G

    def match(self, k):
        '''construct a matching of size k'''
        self.pair = {}
        self.dist = {}
        self.q = collections.deque()

        #init
        for v in self.G.X + self.G.Y:
            self.pair[v] = None
            self.dist[v] = HopcroftKarp.INFINITY

        matching = 0

        while matching < k and self.bfs():
            for v in self.G.X:
                if matching >= k:
                    break
                if self.pair[v] is None and self.dfs(v):
                    matching = matching + 1
                    #print matching, [(u, self.pair[u]) for u in self.pair.keys() if u > 0 and self.pair[u] is not None]
                    if matching == k:
                        break

        # construct matching object
        edges = [(u, self.pair[u]) for u in self.pair.keys() if u > 0 and self.pair[u] is not None]
        M = Matching(k, edges)

        return M

    def dfs(self, v):
        if v != None:
            for u in self.G.neighbors[v]:
                if self.dist[ self.pair[u] ] == self.dist[v] + 1 and self.dfs(self.pair[u]):
                    self.pair[u] = v
                    self.pair[v] = u

                    return True

            self.dist[v] = HopcroftKarp.INFINITY
            return False

        return True

    def bfs(self):
        for v in self.G.X:
            if self.pair[v] == None:
                self.dist[v] = 0
                self.q.append(v)
            else:
                self.dist[v] = HopcroftKarp.INFINITY

        self.dist[None] = HopcroftKarp.INFINITY

        while len(self.q) > 0:
            v = self.q.popleft()
            if v != None:
                for u in self.G.neighbors[v]:
                    if self.dist[ self.pair[u] ] == HopcroftKarp.INFINITY:
                        self.dist[ self.pair[u] ] = self.dist[v] + 1
                        self.q.append(self.pair[u])

        return self.dist[None] != HopcroftKarp.INFINITY


def main():
    n = 4
    g = Graph(n, [(1,-3), (1,-4), (2,-2), (3,-1), (4,-3), (4,-4)])
    hc = HopcroftKarp(g)
    for k in range(1, 5):
        for i in range(3):
            print k, hc.match(k).E

if __name__ == "__main__":
    main()


class MarkovChain:
    '''
    Markov Chain on a set of matchings of size k and k-1
    '''

    def __init__(self, k, G, M):
        '''
        M is the current state (a matching of size k or k-1)
        G is the underlying graph
        k is the max size of a matching
        '''
        self.k = k
        self.G = G
        self.M = M

    def run(self, num_transitions):
        '''Run the markov chain n steps'''
        for i in range(num_transitions):
            e = self.G.random_edge()
            self.M.transition(e)

class MonteCarloEstimator:
    '''
    Monte Carlo Estimator to estimate the ratio of matchings of size k and those of size k-1
    '''

    def __init__(self, G, k):
        self.G = G
        self.k = k

        hc = HopcroftKarp(G)
        self.M = hc.match(k)
        self.MC = MarkovChain(k, G, self.M)

    def estimate(self, num_transitions, num_samples):
        '''
        Estimate an r_k value for the given value of k of our estimator
        '''
        num_k = 0
        num_k_minus_1 = 0
        for i in range(num_samples):
            self.MC.run(num_transitions)
            if self.M.size() == self.k:
                num_k += 1
            elif self.M.size() == self.k - 1:
                num_k_minus_1 += 1

        return float(num_k) / num_k_minus_1

class Approximator:
    '''
    Main class for running our randomized approximation algorithm
    Can set the number of transitions per sampling and number of samplings per approximation
    '''

    def __init__(self, G, num_transitions="n ** 9", num_samples="n ** 5"):
        '''
        Input num_transitions and num_samples as a function of n
        '''
        self.G = G
        self.r = [len(G.E)]

        n = self.G.n
        self.num_transitions = eval(num_transitions)
        self.num_samples = eval(num_samples)
        #print self.num_transitions, self.num_samples

    def run(self):
        '''
        Run the approximation algorithm and return the product of the r values
        '''
        for k in range(2, self.G.n + 1):
            MCE = MonteCarloEstimator(self.G, k)
            self.r.append(MCE.estimate(self.num_transitions, self.num_samples))

        return reduce(mul, self.r, 1)

def main():
    '''
    Basic example
    '''
    n = 4
    g = Graph(n, [(1,-3), (1,-4), (2,-2), (3,-1), (4,-3), (4,-4)])

    a = Approximator(g)
    print a.run()

if __name__ == "__main__":
    main()
