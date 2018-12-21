test_list = [1,64,4,8,1,2,128,6,4,7,256]

print(test_list)
print("Các cặp số có tích là 256 :")

result = []

for i,m in enumerate(test_list):
    check = test_list[i+1:]
    for k, n in enumerate(check):
        if m*n == 256:
            print(m, "và",n, end="  ")
            print("có vị trí là : ", i, "và", k+i+1)