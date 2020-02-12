from datetime import datetime
Btime = datetime.timestamp(datetime.now())

file = open(r'C:\Users\LFRCAKE\Desktop\listes\liste2.txt', 'r')
my_list = file.read()
file.close()
y = []

string = ''
for x in my_list:

    if x == " ":
        y.append(string)
        string = ''
    else:
        string += x

my_list = []
for z in y:
    if z != '':
        my_list.append(z)


# Bubble
def bubble():
    sort = 1
    while sort != 0:
        sort = 0
        i=0
        while i < len(my_list)-1:
            if int(my_list[i]) > int(my_list[i+1]):
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                sort += 1
            i += 1
    return my_list

listing = print(bubble())

# Rapide
# pivot = len(my_list)//2
# liste = []
#
# for x in range(0, len(my_list)):
#     if int(my_list[x]) > int(my_list[pivot]):
#         liste.append(my_list[x])
#
# print(liste)
# print(my_list)

Etime = datetime.timestamp(datetime.now())
time = round(Etime - Btime, 2)
print("\ndurée du tri: "+str(time)+"s")