f = open("input.txt","r",encoding="UTF_8")
data1 = f.read()
f.close()
lines1 = data1.split('\n')
#print(data1)
m = lines1[-2]
#print(m)
dict = {}
for i in lines1[:-2]:
    t = i.find(':')
    dict[int(i[:t])] = i[t+1:]
#print(dict[767])
ans_dict = {}
for i in dict.items():
    if int(m) % i[0] == 0:
        ans_dict[i[0]] = i[1]
#print(ans_dict)
ans_dict = sorted(ans_dict.items())
#print(ans_dict)
p = ""
for i in ans_dict:
    p += i[1]
#print(p)
if len(ans_dict) == 0:
    print(m)
else:
    print(p)
