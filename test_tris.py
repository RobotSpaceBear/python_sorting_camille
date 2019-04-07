from andrei_sort import tri_andrei_bulle
from andrei_sort import tri_andrei_2
from camille_sort import tri_camille

def test_andrei_bulle():
    res = tri_andrei_bulle([1, 4, 3, 0])
    assert res == [0, 1, 3, 4]

    res = tri_andrei_bulle([1, 3, 4, 3, 0])
    assert res == [0, 1, 3, 3, 4]

    res = tri_andrei_bulle([])
    assert res == []

    res = tri_andrei_bulle([99])
    assert res == [99]

    res = tri_andrei_bulle([1, 4, -3, 0])
    assert res == [-3, 0, 1, 4]

    res = tri_andrei_bulle([1, 1, 1, 1])
    assert res == [1, 1, 1, 1]