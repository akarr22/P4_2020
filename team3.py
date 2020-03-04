####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

from random import *
import numpy as np

team_name = 'Team Betrayal' # Only 10 chars displayed.
strategy_name = 'Betray if pattern, otherwise collude'
strategy_description = 'First 5 collude; if pattern of 2 betray or collude in a row in the past 5 moves, betray; otherwise collude'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    # if len(my_history) < 5:
    #     return "c"
    # elif "cc" in their_history [-6: -1]:
    #     return "b"
    # elif "bb" in their_history [-6: -1]:
    #     return "b"
    # else:
    #     return "c"
    
    calls = ["c", "b"]
    weights = [0.5,0.5]
    call = ""
    print(my_history)
    
    if len(my_history) == 0 or len(my_history) == 1:
        pass
    if my_history[len(my_history)-2:len(my_history)] == "cc":
        weights = [0.4,0.6]
    elif my_history[len(my_history)-2:len(my_history)] == "cb":
        weights = [0.6, 0.4]
    elif my_history[len(my_history)-2:len(my_history)] == "bb":
        weights = [0.7, 0.3]
        
    if their_history[len(their_history)-2:len(their_history)] == "cc":
        weights = [0.6,0.4]
    elif their_history[len(their_history)-2:len(their_history)] == "cb":
        weights = [0.4, 0.6]
    elif their_history[len(their_history)-2:len(their_history)] == "bb":
        weights = [0.3, 0.7]
    else:
        weights= [0.5,0.5]
    
    call = np.random.choice(calls, p=weights)
    print(call)
        
    # if callNum == 0:
    #     call = "b"
    # if callNum == 1:
    #     call = "c"
        
    return call


    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print ('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             