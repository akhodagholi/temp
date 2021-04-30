list_n_and_m = input().split(" ")
n = int(list_n_and_m[0])
m = int(list_n_and_m[1])
list_roats = list()

for i in range(0, m):
    list_masir = input().split(" ")
    list_roats.append(list_masir)

print(list_roats)

def check_is_ok(i, list, size):
    for num in range(0, size):
        if list[num][0] == i:
            return check_is_ok(list[num][1], list, size) + i;
        elif list[num][1] == i:
            return check_is_ok(list[num][0], list, size)



   



        