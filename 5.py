f = open("5.txt")
st = f.readline()
st = st.replace("A", "*")
st = st.replace("O", "*")
st = st.split("*")

cnt = 0
max_cnt = 0
for i in range(len(st) - 1):
    if len(st[i]) == 2:
        cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
print(max_cnt)
