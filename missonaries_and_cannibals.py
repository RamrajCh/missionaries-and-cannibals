class State(object):

    LEFT_BANK = 0
    RIGHT_BANK = 1
    GENERATED_STATES = [] 
    LIVE_STATES = []

    def __init__(self, missionaries:int, cannibals:int, bank:int) -> None:
        """
            missonaries -> no. of missonaries possible:{0, 1, 2, 3}
            cannibals -> no. of cannibals possible: {0, 1, 2, 3}
            bank -> left or right bank. 0 represent left bank, 1 represent right bank
        """
        self.missonaries = missionaries
        self.cannibals = cannibals
        self.bank = bank
        self.valid = self.is_state_valid()
        self.killed = self.is_state_killed()
        self.goal = self.is_goal_state()

        if self not in self.GENERATED_STATES and self.valid:
            self.GENERATED_STATES.append(self)
        
        if self not in self.LIVE_STATES and self.valid and not self.killed:
            self.LIVE_STATES.append(self)
    
    def is_state_valid(self) -> bool:
        if self in self.GENERATED_STATES:
            return False
        valid_missonaries = self.missonaries in [0, 1, 2, 3]
        valid_cannibals = self.cannibals in [0, 1, 2, 3]
        valid_bank = self.bank in [0,1]
        return valid_bank and valid_cannibals and valid_missonaries
    
    def is_state_killed(self) -> bool:
        # check for right bank
        right_bank_mask = self.cannibals > self.missonaries and self.missonaries > 0
        
        # check for left bank
        left_bank_mask = self.missonaries > self.cannibals and self.missonaries < 3
        return right_bank_mask or left_bank_mask
    
    def children_states(self) -> list:
        children = []
        op = -1 if self.bank is self.LEFT_BANK else 1

        for m in range(3):
            for c in range(3):
                if m+c < 1 or m+c > 2:
                    continue
                child = State(self.missonaries + op * m, self.cannibals + op * c, self.bank - op)
                if child.valid:
                    children.append([child, [m, c, op]])
        
        self.LIVE_STATES.remove(self)
        return children
    
    def is_initial_state(self) -> bool:
        return self.missonaries == 3 and self.cannibals == 3 and self.bank == 0
    
    def is_goal_state(self) -> bool:
        return self.missonaries == 0 and self.cannibals == 0 and self.bank == 1

    def __eq__(self, __o: object) -> bool:
        eq_missonaries = self.missonaries == __o.missonaries
        eq_cannibals = self.cannibals == __o.cannibals
        eq_bank = self.bank == __o.bank 
        return eq_bank and eq_cannibals and eq_missonaries

    def __repr__(self) -> str:
        return f"{self.missonaries, self.cannibals, self.bank}"


class Node(object):

    def __init__(self, parent_node:object, state:State, action:list) -> None:
        self.parent_node = parent_node
        self.state = state
        self.action = action

    @property
    def label(self) -> str:
        return f"{self.state}"
    
    @property
    def edge_label(self) -> str:
        if self.action:
            return f"[{self.action[0]}, {self.action[1]}, {self.action[2]}]"
    
    def __str__(self) -> str:
        if self.parent_node:
            return f"{self.state} <- {self.parent_node}"
        return f"{self.state}"


if __name__ == "__main__":
    A = State(3,3,0)
    N = Node(None, A, None)
    