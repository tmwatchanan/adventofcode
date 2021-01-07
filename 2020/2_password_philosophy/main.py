from collections import Counter

def solve(pwds):
    ans = 0
    for r, c, pwd in pwds:
        r = r.split("-")
        r_min = int(r[0])
        r_max = int(r[1])
        c = c[:-1]
        print(r_min, r_max, c, pwd, )
        counter = Counter(pwd)
        if r_min <= counter[c] and counter[c] <= r_max:
            ans += 1
    return ans
        

txt = open("input").read().strip().split("\n")
pwds = [x.split(" ") for x in txt]
print(solve(pwds))

