# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    stack = util.Stack()
    stack.push((start, []))
    visited = []
    while  stack.isEmpty()==False:
        node, allactions = stack.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return allactions
            for node2, action, x in problem.getSuccessors(node):
                to_act = allactions + [action]
                stack.push((node2,to_act))
    util.raiseNotDefined()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    q = util.Queue()
    q.push((start, []))
    visited = []
    while q.isEmpty()==False:
        node, allactions = q.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return allactions
            for node2, action, x in problem.getSuccessors(node):
                to_act = allactions + [action]
                q.push((node2, to_act))


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    q2 = util.PriorityQueue()
    q2.push((start, [],0),0)
    visited = []
    while q2.isEmpty()==False:
        node, allactions, cost1 = q2.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return allactions
            for node2, action, x in problem.getSuccessors(node):
                to_act = allactions + [action]
                cost2 = cost1 + x
                q2.push((node2, to_act, cost2),cost2)


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    q2 = util.PriorityQueue()
    q2.push((start, [],0),0)
    visited = []
    while q2.isEmpty()==False:
        node, allactions, cost1 = q2.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return allactions
            for node2, action, x in problem.getSuccessors(node):
                to_act = allactions + [action]
                cost2 = cost1 + x
                h = cost2 + heuristic(node2,problem)
                q2.push((node2, to_act, cost2),h)






    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
