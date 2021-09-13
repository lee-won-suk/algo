arr= [input() for _ in range(5)]
l=[len(arr[i]) for i in range(5)]


for i in range(15):
    for j in range(5):
        if i<l[j]:
            print(arr[j][i], end='')

