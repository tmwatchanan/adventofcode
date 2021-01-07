from collections import Counter

def part1(pwds):
    ans = 0
    for r_min, r_max, c, pwd in pwds:
        print(r_min, r_max, c, pwd)
        counter = Counter(pwd)
        if r_min <= counter[c] and counter[c] <= r_max:
            ans += 1
    return ans

def part2(pwds):
    ans = 0
    for r_min, r_max, c, pwd in pwds:
        ans += (int(pwd[r_min-1] == c) + int(pwd[r_max-1] == c)) % 2
    return ans


def preprocess(x):
    print(x)
    r = x[0].split("-")
    r_min = int(r[0])
    r_max = int(r[1])
    c = x[1][:-1]
    return r_min, r_max, c, x[2]
        

txt = open("input").read().strip().split("\n")
pwds = [preprocess(x.split(" ")) for x in txt]
#print(part1(pwds))
print(part2(pwds))

