from ipylab.generators import chunks, moving_average, moving_median

def test_chunks_basic():
    data = [1,2,3,4,5]
    out = list(chunks(data, 2))
    assert out == [[1,2],[3,4],[5]]

def test_moving_average_and_median():
    avg = moving_average(3); next(avg)
    med = moving_median(3); next(med)
    seq = [1,10,3,8]
    avgs, meds = [], []
    for x in seq:
        avgs.append(avg.send(x))
        meds.append(med.send(x))
    assert avgs[:3] == [1.0, 5.5, 4.666666666666667]
    assert meds[:3] == [1, 5.5, 3]
    assert isinstance(meds[-1], (int, float))
