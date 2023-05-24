from search import *

class WolfGoatCabbage(Problem):

    # Initialize states.
    def __init__(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal=frozenset({})):
        super().__init__(initial, goal)
    
    # Test if state is goal state.
    def goal_test(self, state):
        return state == self.goal
    
    # Get result state of a given action.
    def result(self, state, action):

        new_state = set(state)

        # Perform the given action.
        if 'F' in new_state:
            if action == {'F'}:
                new_state.remove('F')
            elif action == {'F', 'W'}:
                new_state.remove('F')
                new_state.remove('W')
            elif action == {'F', 'G'}:
                new_state.remove('F')
                new_state.remove('G')
            elif action == {'F', 'C'}:
                new_state.remove('F')
                new_state.remove('C')
        elif 'F' not in new_state:
            if action == {'F'}:
                new_state.add('F')
            elif action == {'F', 'W'}:
                new_state.add('F')
                new_state.add('W')
            elif action == {'F', 'G'}:
                new_state.add('F')
                new_state.add('G')
            elif action == {'F', 'C'}:
                new_state.add('F')
                new_state.add('C')
        
        return frozenset(new_state)

    # Get possible actions for the current state.
    def actions(self, state):

        # All possible actions.
        possible_actions = [{'F'}, {'F', 'W'}, {'F', 'G'}, {'F', 'C'}]

        if 'F' in state:
            if 'G' in state: # If G is on the left side.
                if 'W' in state and 'C' in state: # If G is with W and C.
                    possible_actions.remove({'F'})
                    possible_actions.remove({'F', 'W'})
                    possible_actions.remove({'F', 'C'})
                elif 'W' in state: # If G is with W.
                    possible_actions.remove({'F'})
                    possible_actions.remove({'F', 'C'})
                elif 'C' in state: # If G is with C.
                    possible_actions.remove({'F'})
                    possible_actions.remove({'F', 'W'})
                else: # If G is not with W or C.
                    possible_actions.remove({'F', 'W'})
                    possible_actions.remove({'F', 'C'})
            elif 'G' not in state: # If G is not on the left side.
                possible_actions.remove({'F', 'G'})
                if 'W' not in state: # If G is with W.
                    possible_actions.remove({'F', 'W'})
                if 'C' not in state: # If G is with C.
                    possible_actions.remove({'F', 'C'})
                
        elif 'F' not in state:
            if 'G' not in state: # If G is on the right side.
                if 'W' not in state and 'C' not in state: # If G is with W and C.
                    possible_actions.remove({'F'})
                    possible_actions.remove({'F', 'W'})
                    possible_actions.remove({'F', 'C'})
                elif 'W' not in state: # If G is with W.
                    possible_actions.remove({'F'})
                    possible_actions.remove({'F', 'C'})
                elif 'C' not in state: # If G is with C.
                    possible_actions.remove({'F'})
                    possible_actions.remove({'F', 'W'})
                else: # If G is not with W or C.
                    possible_actions.remove({'F', 'W'})
                    possible_actions.remove({'F', 'C'})
            elif 'G' in state: # If G is on the left side.
                possible_actions.remove({'F', 'G'})
                if 'W' in state: # If G is with W.
                    possible_actions.remove({'F', 'W'})
                if 'C' in state: # If G is with C.
                    possible_actions.remove({'F', 'C'})
        
        # Return list of possible actions.
        return possible_actions

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)