"""
expense report:
1721
979
366
299
675
1456

-> sum to 2020 = 1721 + 299
1721 * 200 = 514579 = ANSWER!!
"""

reports = open("./input", "r").read().split()
reports = map(lambda x: int(x), reports)
sorted_reports = sorted(reports)

for a in sorted_reports:
    b = 2020 - a
    if b in sorted_reports:
        break

print(a * b)
