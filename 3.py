from itertools import *

cnt = 0
for i in product("ПОЛИНА", repeat=7):
    st = "".join(i)
    if (st.count("П") == 1) and (st.count("А") == 1) and (st[0] != "А"):
        cnt += 1
print(cnt)