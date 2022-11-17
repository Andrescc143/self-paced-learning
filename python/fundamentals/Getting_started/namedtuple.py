import statistics as st
from collections import namedtuple

def describe(sample):
    Desc = namedtuple("Desc", ["mean", "median", "mode"])
    return Desc(
        st.mean(sample),
        st.median(sample),
        st.mode(sample)
    )
desc = describe([1, 2, 4, 5, 6, 7, 7])
print(desc.mean)
