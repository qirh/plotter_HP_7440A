s = "A"
for _ in range(0,5):
    ns = ""
    for c in s:
        if c == "A":
            ns += "-BF+AFA+FB-"
        elif c == "B":
            ns += "+AF-BFB-FA+"
        else:
            ns += c
    s = ns

print("PU;SP1;PA3000,5000;PD;")

angle = 0
moves = ["PR 100,0;", "PR 0,100;", "PR -100,0;", "PR0,-100;"]
for c in s:
    if c == "+":
        angle = (angle+1)%4
    elif c == "-":
        angle = (angle-1)%4
    elif c == "F":
        print(moves[angle])
print("SP0;")
