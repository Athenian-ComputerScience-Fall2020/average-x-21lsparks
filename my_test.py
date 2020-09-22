from my_code import avg

def test_avg():
    assert 3 == avg([1,5,2,3,4])
    assert 25.77777777777778 == avg([10, 25, 12, 3, 1, 0, -22, 176, 27])
    assert 5.033333333333334 == avg([1.6, 16.5, -2.5, 7, 3.6, 4])
