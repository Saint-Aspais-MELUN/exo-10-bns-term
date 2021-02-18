from exercices.exercice2 import *

def test_positif():
    assert positif([-1,0,5,-3,4,-6,10,9,-8 ]) == [0, 5, 4, 10, 9]

